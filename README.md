# Rheumatoid Arthritis Biomarker Identification Web App

## Overview
This project is a **Streamlit-based web application** designed to identify potential **biomarkers associated with Rheumatoid Arthritis (RA)**. It implements a **Python pipeline** integrating data preprocessing, statistical filtering, enrichment analysis, and network-based approaches to assist researchers in exploring relevant biological markers.

The app allows interactive exploration of datasets, statistical filtering based on log fold change and p-value, gene-set enrichment, and visualization of results.

---

## Features
- **Data Loading:** Import RA datasets using `pandas`.
- **Filtering:** Perform **log fold change (logFC)** and **p-value based filtering**.
- **Visualization:**
  - Bar charts, volcano plots, and heatmaps using `matplotlib` and `seaborn`.
  - Network visualization using `networkx`.
- **Enrichment Analysis:** Conduct pathway and gene set enrichment analysis using **GSEApy** and **Enrichr API**.
- **Interactive UI:** Streamlit interface for real-time data filtering, visualization, and download of results.

---

## Technologies & Tools
- **Python Libraries:**
  - `pandas`, `numpy` – Data manipulation
  - `matplotlib`, `seaborn` – Data visualization
  - `gseapy` – Gene set enrichment analysis
  - `networkx` – Network construction
  - `streamlit` – Web app interface

- **Custom Modules:**
  - `data_loader` – Load and preprocess input datasets
  - `filtering` – Statistical filtering based on logFC and p-value
  - `plots` – Generate bar charts, heatmaps, and volcano plots
  - `enrichr` – Enrichment analysis
  - `network` – Build and visualize gene networks

```bash
RA_Biomarker_App/
│
├── app.py # Main Streamlit app
├── modules/
│ ├── data_loader.py # Data loading & preprocessing
│ ├── filtering.py # LogFC & p-value filtering
│ ├── plots.py # Visualizations
│ ├── enrichr.py # Enrichment analysis
│ └── network.py # Network construction & visualization
│
├── data/
│ ├── raw/ # Original datasets
│ └── processed/ # Filtered/cleaned data
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
## Installation
Clone the repository:
```bash
git clone https://github.com/JFarooq02/RA-Biomarker-Pipeline.git
cd RA-Biomarker-Pipeline

```
--

Install dependencies:

```bash
pip install -r requirements.txt
```
--- 
Launch the Streamlit app:

```bash
streamlit run app.py
```
