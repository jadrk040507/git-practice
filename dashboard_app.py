import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Economic Observatory Dashboard", layout="wide")

# Title
st.title("📊 Economic Observatory Dashboard")
st.markdown("### Mexican Economic Indicators")

# Sidebar
st.sidebar.header("Filters")
st.sidebar.markdown("Use the controls below to filter data")

# Load GDP data
try:
    gdp_data = pd.read_csv('data/growth/gdppc.csv')
    gdp_data['date'] = pd.to_datetime(gdp_data['date'])

    st.header("1. GDP Per Capita")
    st.markdown("GDP per capita in Mexican pesos")

    fig_gdp = px.line(gdp_data, x='date', y='gdppc',
                      title='GDP Per Capita Over Time',
                      labels={'gdppc': 'GDP Per Capita (MXN)', 'date': 'Date'})
    fig_gdp.update_traces(line_color='#970639')
    st.plotly_chart(fig_gdp, use_container_width=True)

except Exception as e:
    st.warning(f"Could not load GDP data: {e}")

# Load sexenios GDP data
try:
    sexenios_data = pd.read_csv('data/growth/sexenios_gdp.csv')

    st.header("2. Economic Growth by Presidential Term")
    st.markdown("Average GDP growth by Mexican presidential administration")

    fig_sexenios = px.bar(sexenios_data, x='mean_growth', y='sexenio',
                          orientation='h',
                          title='Average GDP Growth by Presidential Term',
                          labels={'mean_growth': 'Average Growth (%)', 'sexenio': 'Presidential Term'})
    fig_sexenios.update_traces(marker_color='#970639')
    st.plotly_chart(fig_sexenios, use_container_width=True)

except Exception as e:
    st.warning(f"Could not load presidential term data: {e}")

# Footer
st.markdown("---")
st.markdown("**Data Source:** INEGI (Instituto Nacional de Estadística y Geografía)")
st.markdown("**Dashboard created for educational purposes** - Economic Observatory Project")
