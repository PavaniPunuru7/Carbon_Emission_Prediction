# 🌍 CO₂ Emission Visualization App

An interactive web application built with **Streamlit** to visualize carbon dioxide (CO₂) emissions by country using historical global data. Users can upload a dataset, clean and process it automatically, and view the top emitting countries in an interactive bar chart.

---

## 📊 Features

- 📁 Upload an Excel dataset of CO₂ emissions
- 🧹 Automatic data cleaning (removes unused columns, handles missing data)
- 📈 View top N emitting countries using a dynamic slider
- 📊 Interactive bar graph showing total emissions per country
- 💡 Simple, browser-based UI powered by Streamlit

---

## 🚀 Live Demo

👉 (https://your-deployed-url.streamlit.app)


## 🖼️ Screenshot

![CO₂ Emissions Graph](screenshot.png)

---

## 📁 Dataset Format

The Excel file should:
- Contain a sheet named `"Data"`
- Include columns like:
  - `Country`, `SCALE`, `Series code`, `2000`, `2001`, ..., `2020`
- Avoid merged cells and ensure numeric values for emission data

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)
- [XLRD](https://xlrd.readthedocs.io/)

---

## 🧪 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Carbon_Emission_Prediction.git
   cd Carbon_Emission_Prediction
