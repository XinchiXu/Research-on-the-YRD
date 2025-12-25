# Research on the Yellow River Delta (YRD) 🌊🌱

This repository provides source codes and example data for generating a **Monthly water–soil–vegetation fractional abundance time series of the Yellow River Delta (2000–2024)** using medium-resolution satellite imagery (MODIS/061/MOD09GA).

The project focuses on fractional surface composition retrieval to support **long-term, process-oriented remote sensing analysis** in highly heterogeneous and human-regulated delta environments.

---

## 📦 Dataset Overview

**Dataset title:**  
**Monthly Water–Soil–Vegetation Fractional Abundance Time Series of the Yellow River Delta (2000–2024)**

- **Spatial extent:** Yellow River Delta, China  
- **Temporal coverage:** 2000–2024 (monthly)  
- **Spatial resolution:** Medium resolution (MODIS-based)  
- **Variables:**  
  - Water fractional abundance
  - Soil (bare land) fractional abundance
  - Vegetation fractional abundance

⚠️ **Note:**  
The `data/` directory in this repository only contains **example data for the 12 months of 2024**.  
To obtain the complete long-term dataset (2000–2024), users need to **run the provided Google Earth Engine (GEE) and Python scripts locally**.

---

## 📁 Project Structure

```text
Research-on-the-YRD/
├── data/
│   ├── MODIS_YRD/        # Example MODIS data (2024 only)
│   ├── YRD_shp/          # Yellow River Delta boundary shapefile
│   └── YRD_rect_shp/     # Rectangular extent shapefile
├── model/
│   └── rf_model.pkl      # The trained random forest model
├── predict/
│   ├── abundance_tif/    # Output fractional abundance GeoTIFFs
│   └── abundance_preview/# Quick-look visualization images
├── main.py               # Python script for abundance prediction
├── modis_downloader.js   # GEE script for MODIS data download
└── README.md
```

---

## 🐍 Python Environment Setup

**Python version:** `Python 3.10` (recommended)

### Required Python libraries

```python
import numpy as np
import geopandas as gpd
import joblib
import rasterio
from rasterio.mask import mask
import matplotlib.pyplot as plt
```

### Install dependencies

```bash
pip install numpy geopandas joblib rasterio matplotlib
```

> 💡 Tip: Using a virtual environment (e.g., `conda` or `venv`) is strongly recommended.

---

## 🌍 Google Earth Engine (GEE) Data Download

The file `modis_downloader.js` is a **Google Earth Engine JavaScript script** used to download MODIS imagery over the Yellow River Delta.

### How to run

1. Open the [Google Earth Engine Code Editor](https://code.earthengine.google.com/)
2. Copy the content of `modis_downloader.js` into the editor
3. Set your export parameters (time range, extraction area,  output folder, etc.)
4. Run the script and export the data to Google Drive

Downloaded data can then be placed into the `data/MODIS_YRD/` directory for local processing.

---

## 🚀 Fractional Abundance Prediction

After preparing the MODIS data:

```bash
python main.py
```

The script will:
- Load the trained Random Forest model
- Predict water, soil, and vegetation fractional abundance
- Export results as GeoTIFF files
- Generate quick-look preview figures

---

## 📊 Output Products

- **GeoTIFF files:** Monthly fractional abundance maps  
- **Preview images:** PNG visualizations for rapid inspection  

These outputs are stored in the `predict/` directory.

---

## 🏫 Affiliation

🏛️ **Aerospace Information Research Institute, Chinese Academy of Sciences (AIRCAS)**  ([aircas.ac.cn](http://www.aircas.cn/))  
🎓 **University of Chinese Academy of Sciences (UCAS)**  ([ucas.edu.cn](https://www.ucas.edu.cn/))

---

## 📮 Contact

For questions, collaboration, or additional data requests, please contact:

**Xinchi Xu**  
📧 Email: **xuxinchi25@mails.ucas.ac.cn**

More advanced analyses or extended datasets can be made available upon reasonable request 😊

---

## 📜 License & Usage

This repository is intended for **academic research and educational use**.  
If you use this code or dataset in your research, please consider citing the corresponding study.

🌟 Star the repo if you find it useful!
