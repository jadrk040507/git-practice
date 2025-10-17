"""
Economic Observatory Dashboard
A simple Streamlit dashboard for visualizing economic indicators
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Economic Observatory Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Economic Observatory Dashboard")
st.markdown("### Visualización de Indicadores Económicos de México")
st.markdown("---")

@st.cache_data
def load_gdp_data():
    """Load GDP data from CSV"""
    df = pd.read_csv('data/gdp/mexico_gdp_sample.csv', comment='#')
    df['date'] = pd.to_datetime(df['date'])
    return df

@st.cache_data
def load_inflation_data():
    """Load inflation data from CSV"""
    df = pd.read_csv('data/inflation/mexico_inflation_sample.csv', comment='#')
    df['date'] = pd.to_datetime(df['date'])
    return df

@st.cache_data
def load_unemployment_data():
    """Load unemployment data from CSV"""
    df = pd.read_csv('data/unemployment/mexico_unemployment_sample.csv', comment='#')
    df['date'] = pd.to_datetime(df['date'])
    return df

# Load all data
try:
    gdp_data = load_gdp_data()
    inflation_data = load_inflation_data()
    unemployment_data = load_unemployment_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar filters
st.sidebar.header("Filtros")
indicator = st.sidebar.selectbox(
    "Selecciona un indicador:",
    ["PIB", "Inflación", "Desempleo", "Todos"]
)

# Date range filter
min_date = min(gdp_data['date'].min(), inflation_data['date'].min(), unemployment_data['date'].min())
max_date = max(gdp_data['date'].max(), inflation_data['date'].max(), unemployment_data['date'].max())

date_range = st.sidebar.date_input(
    "Rango de fechas:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# KPIs at the top
col1, col2, col3 = st.columns(3)

with col1:
    latest_gdp = gdp_data.iloc[-1]
    st.metric(
        label="PIB Reciente",
        value=f"${latest_gdp['value']/1e6:.1f}B MXN",
        delta=f"{latest_gdp['growth_rate']:.1f}%"
    )

with col2:
    latest_inflation = inflation_data.iloc[-1]
    st.metric(
        label="Inflación Anual",
        value=f"{latest_inflation['inflation_rate']:.1f}%",
        delta=f"{latest_inflation['inflation_rate'] - inflation_data.iloc[-13]['inflation_rate']:.1f}pp"
    )

with col3:
    latest_unemployment = unemployment_data.iloc[-1]
    st.metric(
        label="Tasa de Desempleo",
        value=f"{latest_unemployment['unemployment_rate']:.1f}%",
        delta=f"{latest_unemployment['unemployment_rate'] - unemployment_data.iloc[-13]['unemployment_rate']:.1f}pp"
    )

st.markdown("---")

# Display charts based on selection
if indicator in ["PIB", "Todos"]:
    st.header("📈 Producto Interno Bruto (PIB)")

    # Filter by date
    filtered_gdp = gdp_data[
        (gdp_data['date'] >= pd.to_datetime(date_range[0])) &
        (gdp_data['date'] <= pd.to_datetime(date_range[1]))
    ]

    # Create GDP chart
    fig_gdp = go.Figure()

    # Add GDP value bars
    fig_gdp.add_trace(go.Bar(
        x=filtered_gdp['date'],
        y=filtered_gdp['value'] / 1e6,
        name='PIB (Billones MXN)',
        marker_color='lightblue',
        yaxis='y'
    ))

    # Add growth rate line
    fig_gdp.add_trace(go.Scatter(
        x=filtered_gdp['date'],
        y=filtered_gdp['growth_rate'],
        name='Tasa de Crecimiento (%)',
        marker_color='darkblue',
        yaxis='y2',
        line=dict(width=3)
    ))

    # Update layout
    fig_gdp.update_layout(
        title='PIB y Tasa de Crecimiento Trimestral',
        xaxis=dict(title='Fecha'),
        yaxis=dict(title='PIB (Billones MXN)', side='left'),
        yaxis2=dict(title='Crecimiento (%)', side='right', overlaying='y'),
        hovermode='x unified',
        height=400
    )

    st.plotly_chart(fig_gdp, use_container_width=True)

    # Show summary statistics
    with st.expander("Ver estadísticas del PIB"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("PIB Promedio", f"${filtered_gdp['value'].mean()/1e6:.1f}B MXN")
            st.metric("PIB Máximo", f"${filtered_gdp['value'].max()/1e6:.1f}B MXN")
        with col2:
            st.metric("Crecimiento Promedio", f"{filtered_gdp['growth_rate'].mean():.2f}%")
            st.metric("Crecimiento Máximo", f"{filtered_gdp['growth_rate'].max():.2f}%")

if indicator in ["Inflación", "Todos"]:
    st.header("💰 Inflación")

    # Filter by date
    filtered_inflation = inflation_data[
        (inflation_data['date'] >= pd.to_datetime(date_range[0])) &
        (inflation_data['date'] <= pd.to_datetime(date_range[1]))
    ]

    # Create inflation chart
    fig_inflation = px.line(
        filtered_inflation,
        x='date',
        y='inflation_rate',
        title='Tasa de Inflación Anual',
        labels={'date': 'Fecha', 'inflation_rate': 'Inflación (%)'}
    )

    fig_inflation.update_traces(line_color='red', line_width=2)
    fig_inflation.add_hline(y=3.0, line_dash="dash", line_color="green",
                            annotation_text="Meta Banco de México (3%)")
    fig_inflation.update_layout(height=400)

    st.plotly_chart(fig_inflation, use_container_width=True)

    # Show CPI chart
    fig_cpi = px.area(
        filtered_inflation,
        x='date',
        y='cpi',
        title='Índice de Precios al Consumidor (IPC)',
        labels={'date': 'Fecha', 'cpi': 'IPC (2018=100)'}
    )
    fig_cpi.update_traces(fillcolor='rgba(255,100,100,0.3)', line_color='darkred')
    fig_cpi.update_layout(height=350)

    st.plotly_chart(fig_cpi, use_container_width=True)

    # Show summary statistics
    with st.expander("Ver estadísticas de inflación"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Inflación Promedio", f"{filtered_inflation['inflation_rate'].mean():.2f}%")
            st.metric("Inflación Máxima", f"{filtered_inflation['inflation_rate'].max():.2f}%")
        with col2:
            st.metric("Inflación Mínima", f"{filtered_inflation['inflation_rate'].min():.2f}%")
            st.metric("Desv. Estándar", f"{filtered_inflation['inflation_rate'].std():.2f}%")

if indicator in ["Desempleo", "Todos"]:
    st.header("👥 Mercado Laboral")

    # Filter by date
    filtered_unemployment = unemployment_data[
        (unemployment_data['date'] >= pd.to_datetime(date_range[0])) &
        (unemployment_data['date'] <= pd.to_datetime(date_range[1]))
    ]

    # Create unemployment chart
    fig_unemployment = go.Figure()

    fig_unemployment.add_trace(go.Scatter(
        x=filtered_unemployment['date'],
        y=filtered_unemployment['unemployment_rate'],
        fill='tozeroy',
        name='Tasa de Desempleo',
        line_color='orange'
    ))

    fig_unemployment.update_layout(
        title='Tasa de Desempleo',
        xaxis_title='Fecha',
        yaxis_title='Desempleo (%)',
        height=400
    )

    st.plotly_chart(fig_unemployment, use_container_width=True)

    # Labor force chart
    fig_labor = px.line(
        filtered_unemployment,
        x='date',
        y=['labor_force', 'employed'],
        title='Fuerza Laboral y Empleo',
        labels={'date': 'Fecha', 'value': 'Personas (millones)'}
    )
    fig_labor.update_layout(height=350)

    st.plotly_chart(fig_labor, use_container_width=True)

    # Show summary statistics
    with st.expander("Ver estadísticas del mercado laboral"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Desempleo Promedio", f"{filtered_unemployment['unemployment_rate'].mean():.2f}%")
            st.metric("Desempleo Mínimo", f"{filtered_unemployment['unemployment_rate'].min():.2f}%")
        with col2:
            st.metric("Fuerza Laboral Actual", f"{filtered_unemployment['labor_force'].iloc[-1]/1e6:.1f}M")
            st.metric("Empleados Actuales", f"{filtered_unemployment['employed'].iloc[-1]/1e6:.1f}M")

# Footer
st.markdown("---")
st.markdown("""
**Fuentes de Datos:**
- PIB: INEGI (Instituto Nacional de Estadística y Geografía)
- Inflación: INEGI / Banco de México
- Desempleo: INEGI (ENOE - Encuesta Nacional de Ocupación y Empleo)

**Actualizado:** Octubre 2024
""")
