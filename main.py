import numpy as np
import geopandas as gpd
import joblib
import rasterio
from rasterio.mask import mask
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial'
rf = joblib.load('./model/rf_model.pkl')
gdf = gpd.read_file('./data/YRD_shp/yrd.shp')
geoms = [geom for geom in gdf.geometry]


def get_modis_path(year, month):
    return f'./data/MODIS_YRD/MODIS_YRD_{month:02d}-{year}.tif'


def abundance_extraction(year, month, data_full=True, save_preview=False, save_tif=False):
    with rasterio.open(get_modis_path(year, month)) as src:
        clip_data, transform = mask(
            src,
            geoms,
            crop=True,
            nodata=np.nan
        )
        height, width = clip_data.shape[1], clip_data.shape[2]
        flat_data = clip_data.reshape(clip_data.shape[0], -1).T
        mask_valid = ~np.any(np.isnan(flat_data), axis=1)
        data_valid = flat_data[mask_valid]
        if data_valid.shape[0] > 0:
            abundance_valid = rf.predict_proba(data_valid)
            abundance_full = np.full(
                (flat_data.shape[0], abundance_valid.shape[1]),
                np.nan
            )
            abundance_full[mask_valid] = abundance_valid
            abundance_full = abundance_full.T.reshape(len(rf.classes_), height, width)
        else:
            abundance_full = np.full((len(rf.classes_), height, width), np.nan)
        if save_tif:
            profile = src.profile.copy()
            profile.update({
                'count': len(rf.classes_),
                'height': height,
                'width': width,
                'transform': transform,
                'nodata': np.nan
            })
            with rasterio.open(f'./predict/abundance_tif/{month:02d}-{year}.tif', 'w', **profile) as dst:
                for idx, class_id in enumerate(rf.classes_):
                    class_names = {0: 'water', 1: 'soil', 2: 'vegetation'}
                    dst.write(abundance_full[idx], idx + 1)
                    dst.set_band_description(idx + 1, class_names[class_id])
        if save_preview:
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            titles = ['Water Abundance', 'Soil Abundance', 'Vegetation Abundance']
            for i in range(3):
                ax = axes[i]
                im = ax.imshow(abundance_full[i], cmap='viridis', vmin=0, vmax=1)
                ax.set_title(titles[i])
                ax.axis('off')
                fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
            plt.suptitle(f'Yellow River Delta Abundance Maps {month:02d}-{year}', fontsize=16)
            plt.tight_layout()
            plt.savefig(f'./predict/abundance_preview/{month:02d}-{year}.png', dpi=300)
        return abundance_full if data_full else abundance_valid


if __name__ == '__main__':
    years = [y for y in range(2000, 2025)]
    for y in years:
        months = [m for m in range(1, 13)] if y != 2000 else [m for m in range(3, 13)]
        for m in months:
            abundance_extraction(y, m, save_tif=True)
