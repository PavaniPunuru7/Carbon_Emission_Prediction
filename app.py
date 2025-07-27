import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🌍 CO₂ Emissions by Country")

# File uploader
uploaded_file = st.file_uploader("Upload CO₂ Emissions Excel File", type=["xlsx"])

if uploaded_file:
    data_sheet = "Data"  # Name of the sheet inside your Excel file
    data_orig = pd.read_excel(uploaded_file, sheet_name=data_sheet)

    st.write("### Raw Dataset")
    st.dataframe(data_orig.head())

    # Data cleaning
    data_clean = data_orig[data_orig['SCALE'] != "Text"]
    data_clean = data_clean.drop(['Country name', 'Series code', 'SCALE', 'Decimals'], axis='columns')
    data_clean.iloc[:, 2:] = data_clean.iloc[:, 2:].replace({'': np.nan, '..': np.nan})
    data_clean2 = data_clean.applymap(lambda x: pd.to_numeric(x, errors='ignore'))

    # Calculate total emissions for each country
    emission_sums = data_clean2.iloc[:, 2:].sum(axis=1)
    countries = data_clean2.iloc[:, 0]

    # Slider for top N
    top_n = st.slider("Top N Countries by Emission", min_value=5, max_value=20, value=10)
    top_emitters = pd.DataFrame({'Country': countries, 'Total Emission': emission_sums})
    top_emitters = top_emitters.sort_values(by="Total Emission", ascending=False).head(top_n)

    st.write("### Top Emitting Countries")
    st.dataframe(top_emitters)

    # Plot bar graph
    fig, ax = plt.subplots()
    ax.bar(top_emitters['Country'], top_emitters['Total Emission'])
    plt.xticks(rotation=90)
    st.pyplot(fig)
