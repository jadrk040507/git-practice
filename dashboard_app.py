import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Economic Observatory Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #970639;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #970639;
    }
    </style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<h1 class="main-header">📊 Economic Observatory Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Interactive Mexican Economic Indicators Platform</p>', unsafe_allow_html=True)

# Sidebar with enhanced controls
st.sidebar.image("https://via.placeholder.com/300x100/970639/FFFFFF?text=Economic+Observatory", use_container_width=True)
st.sidebar.header("📌 Dashboard Controls")
st.sidebar.markdown("---")

# Date range filter
st.sidebar.subheader("📅 Date Range")
date_filter = st.sidebar.radio(
    "Select time period:",
    ["All Time", "Last 5 Years", "Last 10 Years", "Custom Range"]
)

# Indicator selection
st.sidebar.subheader("📈 Indicators")
show_gdp = st.sidebar.checkbox("GDP Analysis", value=True)
show_growth = st.sidebar.checkbox("Growth by Administration", value=True)
show_trends = st.sidebar.checkbox("Trend Analysis", value=True)
show_summary = st.sidebar.checkbox("Summary Statistics", value=True)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Use the filters above to customize your view")

# Main content area
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 GDP Analysis", "🏛️ By Administration", "📉 Trends & Forecasts"])

# Tab 1: Overview
with tab1:
    st.header("Economic Overview")

    # Key metrics in columns
    col1, col2, col3, col4 = st.columns(4)

    try:
        gdp_data = pd.read_csv('data/growth/gdppc.csv')
        gdp_data['date'] = pd.to_datetime(gdp_data['date'])

        latest_gdp = gdp_data.iloc[-1]['gdppc']
        prev_gdp = gdp_data.iloc[-2]['gdppc']
        gdp_change = ((latest_gdp - prev_gdp) / prev_gdp) * 100

        with col1:
            st.metric(
                label="Latest GDP per Capita",
                value=f"${latest_gdp:,.0f} MXN",
                delta=f"{gdp_change:.2f}%"
            )

        with col2:
            st.metric(
                label="Data Points",
                value=len(gdp_data)
            )

        with col3:
            avg_gdp = gdp_data['gdppc'].mean()
            st.metric(
                label="Average GDP per Capita",
                value=f"${avg_gdp:,.0f} MXN"
            )

        with col4:
            years_covered = gdp_data['date'].dt.year.max() - gdp_data['date'].dt.year.min()
            st.metric(
                label="Years of Data",
                value=f"{years_covered} years"
            )
    except:
        st.warning("GDP data not available")

    st.markdown("---")

    # Quick visualization
    col1, col2 = st.columns(2)

    with col1:
        if show_gdp:
            try:
                fig = px.area(gdp_data, x='date', y='gdppc',
                             title='GDP Per Capita Evolution',
                             labels={'gdppc': 'GDP Per Capita (MXN)', 'date': 'Date'})
                fig.update_traces(fillcolor='rgba(151, 6, 57, 0.3)', line_color='#970639')
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.info("GDP data not available")

    with col2:
        if show_growth:
            try:
                sexenios_data = pd.read_csv('data/growth/sexenios_gdp.csv')
                fig = px.bar(sexenios_data, x='mean_growth', y='sexenio',
                            orientation='h',
                            title='Average Growth by Presidential Term',
                            labels={'mean_growth': 'Growth (%)', 'sexenio': 'Term'})
                fig.update_traces(marker_color='#970639')
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.info("Presidential term data not available")

# Tab 2: GDP Analysis
with tab2:
    st.header("Detailed GDP Analysis")

    try:
        gdp_data = pd.read_csv('data/growth/gdppc.csv')
        gdp_data['date'] = pd.to_datetime(gdp_data['date'])

        # Apply date filter
        if date_filter == "Last 5 Years":
            cutoff_date = gdp_data['date'].max() - pd.DateOffset(years=5)
            gdp_filtered = gdp_data[gdp_data['date'] >= cutoff_date]
        elif date_filter == "Last 10 Years":
            cutoff_date = gdp_data['date'].max() - pd.DateOffset(years=10)
            gdp_filtered = gdp_data[gdp_data['date'] >= cutoff_date]
        else:
            gdp_filtered = gdp_data

        # Create dual-axis chart
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(x=gdp_filtered['date'], y=gdp_filtered['gdppc'],
                      name="GDP per Capita", line=dict(color='#970639', width=3)),
            secondary_y=False,
        )

        # Calculate year-over-year growth
        gdp_filtered['growth'] = gdp_filtered['gdppc'].pct_change() * 100

        fig.add_trace(
            go.Bar(x=gdp_filtered['date'], y=gdp_filtered['growth'],
                  name="YoY Growth %", marker_color='rgba(151, 6, 57, 0.3)'),
            secondary_y=True,
        )

        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text="GDP per Capita (MXN)", secondary_y=False)
        fig.update_yaxes(title_text="Growth Rate (%)", secondary_y=True)

        fig.update_layout(
            title_text="GDP per Capita with Growth Rate",
            hovermode='x unified',
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

        if show_summary:
            st.subheader("📊 Summary Statistics")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Maximum GDP per Capita", f"${gdp_filtered['gdppc'].max():,.0f}")
            with col2:
                st.metric("Minimum GDP per Capita", f"${gdp_filtered['gdppc'].min():,.0f}")
            with col3:
                st.metric("Standard Deviation", f"${gdp_filtered['gdppc'].std():,.0f}")

    except Exception as e:
        st.error(f"Error loading GDP data: {e}")

# Tab 3: By Administration
with tab3:
    st.header("Economic Performance by Presidential Administration")

    try:
        sexenios_data = pd.read_csv('data/growth/sexenios_gdp.csv')

        # Enhanced bar chart
        fig = go.Figure()

        colors = ['#970639' if x == sexenios_data['mean_growth'].max() else '#d4a5b5'
                 for x in sexenios_data['mean_growth']]

        fig.add_trace(go.Bar(
            x=sexenios_data['mean_growth'],
            y=sexenios_data['sexenio'],
            orientation='h',
            marker_color=colors,
            text=sexenios_data['mean_growth'].round(2),
            texttemplate='%{text}%',
            textposition='outside',
        ))

        fig.update_layout(
            title="Average GDP Growth Rate by Presidential Term",
            xaxis_title="Average Growth Rate (%)",
            yaxis_title="Presidential Administration",
            height=500,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

        # Data table
        st.subheader("📋 Detailed Data")
        st.dataframe(
            sexenios_data.style.background_gradient(subset=['mean_growth'], cmap='RdYlGn'),
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Error loading administration data: {e}")

# Tab 4: Trends
with tab4:
    st.header("Trend Analysis & Insights")

    if show_trends:
        try:
            gdp_data = pd.read_csv('data/growth/gdppc.csv')
            gdp_data['date'] = pd.to_datetime(gdp_data['date'])

            # Moving average
            window = st.slider("Moving Average Window (quarters)", 4, 20, 8)
            gdp_data['ma'] = gdp_data['gdppc'].rolling(window=window).mean()

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=gdp_data['date'], y=gdp_data['gdppc'],
                name='Actual GDP per Capita',
                line=dict(color='lightgray', width=1)
            ))

            fig.add_trace(go.Scatter(
                x=gdp_data['date'], y=gdp_data['ma'],
                name=f'{window}-Quarter Moving Average',
                line=dict(color='#970639', width=3)
            ))

            fig.update_layout(
                title=f"GDP per Capita with {window}-Quarter Moving Average",
                xaxis_title="Date",
                yaxis_title="GDP per Capita (MXN)",
                hovermode='x unified',
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

            # Key insights
            st.subheader("🔍 Key Insights")

            latest_growth = ((gdp_data.iloc[-1]['gdppc'] - gdp_data.iloc[-5]['gdppc']) /
                           gdp_data.iloc[-5]['gdppc'] * 100)

            col1, col2 = st.columns(2)

            with col1:
                st.info(f"""
                **Recent Trend**
                - Last year growth: {latest_growth:.2f}%
                - Current GDP: ${gdp_data.iloc[-1]['gdppc']:,.0f} MXN
                """)

            with col2:
                volatility = gdp_data['gdppc'].pct_change().std() * 100
                st.info(f"""
                **Volatility Metrics**
                - Standard deviation of growth: {volatility:.2f}%
                - Data points: {len(gdp_data)}
                """)

        except Exception as e:
            st.error(f"Error in trend analysis: {e}")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📊 Data Source**")
    st.markdown("INEGI (Instituto Nacional de Estadística y Geografía)")

with col2:
    st.markdown("**🎓 Educational Project**")
    st.markdown("Economic Observatory - Git & GitHub Practice")

with col3:
    st.markdown("**📅 Last Updated**")
    st.markdown(datetime.now().strftime("%Y-%m-%d"))

st.markdown("---")
st.caption("Dashboard created with Streamlit • Data analysis with Python & R • Version 2.0 (Feature Branch)")
