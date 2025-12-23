// https://code.earthengine.google.com/
// The code for downloading MODIS image data allows you to modify the target year or month at the corresponding position as needed.
var region = ee.FeatureCollection('projects/ee-ipicturesque1616/assets/yrd_rect');
var BANDS = ['sur_refl_b01', 'sur_refl_b02', 'sur_refl_b03', 'sur_refl_b04', 'sur_refl_b05', 'sur_refl_b06', 'sur_refl_b07'];
var years = ee.List.sequence(2000, 2024);

years.evaluate(function (yearsArray) {
    yearsArray.forEach(function (year) {
        var months = (year === 2000) ? ee.List.sequence(3, 12) : ee.List.sequence(1, 12);
        months.evaluate(function (monthsArray) {
            monthsArray.forEach(function (month) {
                var start = ee.Date.fromYMD(year, month, 1);
                var image = ee.ImageCollection('MODIS/061/MOD09GA')
                    .filterDate(start, start.advance(1, 'month'))
                    .filterBounds(region)
                    .select(BANDS)
                    .median()
                    .clip(region);
                Export.image.toDrive({
                    image: image,
                    description: 'MODIS_YRD_' + ('0' + month).slice(-2) + '-' + year,
                    folder: 'MODIS_YRD',
                    region: region.geometry(),
                    scale: 500,
                    maxPixels: 1e13,
                    fileFormat: 'GeoTIFF'
                });
            })
        });

    });
});

print('Export tasks created. View and run them in the Tasks panel.');