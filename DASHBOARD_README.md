# Economic Dashboard - Setup Instructions

This dashboard provides interactive visualizations of Mexican economic indicators.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/YOUR-USERNAME/git-practice.git
   cd git-practice
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install streamlit pandas plotly python-dotenv
   ```

## Running the Dashboard

### Option 1: Command Line
```bash
streamlit run dashboard_app.py
```

### Option 2: With custom port
```bash
streamlit run dashboard_app.py --server.port 8502
```

The dashboard will open automatically in your web browser at `http://localhost:8501`

## Features

- **PIB (GDP)**: Quarterly GDP values and growth rates
- **Inflación**: Monthly inflation rates and CPI index
- **Desempleo**: Unemployment rates and labor force statistics
- **Interactive filters**: Date range selection
- **Real-time updates**: Automatically refreshes when data changes

## Dashboard Structure

```
dashboard_app.py          # Main Streamlit application
data/
  ├── gdp/               # GDP data files
  ├── inflation/         # Inflation data files
  └── unemployment/      # Unemployment data files
requirements.txt         # Python dependencies
```

## Troubleshooting

### Dashboard won't start
- Make sure all packages are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

### Data not loading
- Verify CSV files exist in `data/` directories
- Check file paths in `dashboard_app.py`
- Ensure CSV files have proper headers

### Port already in use
- Use a different port: `streamlit run dashboard_app.py --server.port 8502`
- Stop other Streamlit instances

## Customization

### Adding New Indicators

1. Add data CSV to appropriate folder in `data/`
2. Create loading function in `dashboard_app.py`:
   ```python
   @st.cache_data
   def load_your_data():
       df = pd.read_csv('data/folder/your_file.csv', comment='#')
       df['date'] = pd.to_datetime(df['date'])
       return df
   ```

3. Add visualization section:
   ```python
   if indicator in ["Your Indicator", "Todos"]:
       st.header("Your Indicator")
       # Your charts here
   ```

### Modifying Charts

The dashboard uses Plotly for interactive charts. Modify the `fig_*` variables to customize:
- Colors: `marker_color`, `line_color`
- Chart type: `go.Bar`, `go.Scatter`, `px.line`, etc.
- Layout: `fig.update_layout()`

## Data Sources

- **PIB**: INEGI
- **Inflación**: INEGI / Banco de México
- **Desempleo**: INEGI (ENOE)

## Contributing

Want to improve the dashboard? Follow the Git workflow:

1. Create a branch: `git checkout -b feature/dashboard-improvement`
2. Make your changes
3. Test locally: `streamlit run dashboard_app.py`
4. Commit: `git commit -m "feat: improve dashboard visuals"`
5. Push and create PR

---

**Questions?** Open an issue or contact the instructor.
