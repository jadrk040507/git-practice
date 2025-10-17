"""
World Bank Data Fetcher
Author: Economic Observatory Team
Date: 2024-10-16
Description: Fetches economic indicators from World Bank API
Data Source: World Bank Open Data
"""

import os
import pandas as pd
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key (World Bank API is actually free and doesn't require a key,
# but this shows the pattern for APIs that do)
WORLD_BANK_API_KEY = os.getenv('WORLD_BANK_API_KEY', '')

# Base URL for World Bank API
WORLD_BANK_BASE_URL = "https://api.worldbank.org/v2"


def fetch_indicator_data(country_code, indicator_code, start_year=2020, end_year=2024):
    """
    Fetch indicator data from World Bank API.

    Args:
        country_code: ISO country code (e.g., 'MEX' for Mexico, 'USA' for United States)
        indicator_code: World Bank indicator code (e.g., 'NY.GDP.MKTP.CD' for GDP)
        start_year: Start year for data
        end_year: End year for data

    Returns:
        DataFrame with indicator data
    """

    # Build API URL
    url = f"{WORLD_BANK_BASE_URL}/country/{country_code}/indicator/{indicator_code}"

    # Set parameters
    params = {
        'format': 'json',
        'date': f'{start_year}:{end_year}',
        'per_page': 1000
    }

    # Make API request
    print(f"Fetching {indicator_code} for {country_code}...")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")

    # Parse JSON response
    data = response.json()

    if len(data) < 2 or data[1] is None:
        print(f"  No data available for {indicator_code}")
        return pd.DataFrame()

    # Convert to DataFrame
    df = pd.DataFrame(data[1])

    if df.empty:
        print(f"  No data returned for {indicator_code}")
        return df

    # Clean and format data
    df_clean = pd.DataFrame({
        'date': pd.to_datetime(df['date'].astype(str) + '-12-31'),
        'value': pd.to_numeric(df['value'], errors='coerce'),
        'country': df['country'].apply(lambda x: x['value'] if isinstance(x, dict) else x),
        'indicator': indicator_code
    })

    # Remove rows with missing values
    df_clean = df_clean.dropna(subset=['value'])
    df_clean = df_clean.sort_values('date')

    print(f"  Retrieved {len(df_clean)} observations")

    return df_clean


def fetch_multiple_indicators(country_code, indicators, start_year=2020, end_year=2024):
    """
    Fetch multiple indicators for a country.

    Args:
        country_code: ISO country code
        indicators: Dictionary of {name: indicator_code}
        start_year: Start year
        end_year: End year

    Returns:
        Dictionary of DataFrames
    """

    results = {}

    for name, code in indicators.items():
        try:
            data = fetch_indicator_data(country_code, code, start_year, end_year)
            if not data.empty:
                results[name] = data
        except Exception as e:
            print(f"  Error fetching {name}: {e}")
            continue

    return results


def save_data_to_csv(data_dict, country_code):
    """
    Save fetched data to CSV files.

    Args:
        data_dict: Dictionary of DataFrames
        country_code: Country code for filename
    """

    print("\nSaving data to CSV files...")

    for name, df in data_dict.items():
        # Determine subdirectory based on indicator type
        if 'gdp' in name.lower():
            subdir = 'gdp'
        elif 'inflation' in name.lower() or 'cpi' in name.lower():
            subdir = 'inflation'
        elif 'unemployment' in name.lower() or 'labor' in name.lower():
            subdir = 'unemployment'
        else:
            subdir = 'gdp'  # default

        # Create filename
        filename = f"../../data/{subdir}/{country_code.lower()}_{name.lower()}_worldbank.csv"

        # Save to CSV
        df.to_csv(filename, index=False)
        print(f"  Saved {filename}")


def main():
    """Main execution function."""

    print("=" * 60)
    print("World Bank Economic Data Fetcher")
    print("=" * 60)
    print()

    # Define indicators to fetch
    indicators = {
        'gdp': 'NY.GDP.MKTP.CD',  # GDP (current US$)
        'gdp_growth': 'NY.GDP.MKTP.KD.ZG',  # GDP growth (annual %)
        'inflation': 'FP.CPI.TOTL.ZG',  # Inflation, consumer prices (annual %)
        'unemployment': 'SL.UEM.TOTL.ZS',  # Unemployment, total (% of total labor force)
    }

    # Fetch data for Mexico
    country_code = 'MEX'
    print(f"\nFetching data for {country_code}...\n")

    data = fetch_multiple_indicators(country_code, indicators, start_year=2015, end_year=2024)

    # Save data
    if data:
        save_data_to_csv(data, country_code)
        print("\nData fetch complete!")
    else:
        print("\nNo data was fetched.")

    return data


if __name__ == '__main__':
    results = main()
