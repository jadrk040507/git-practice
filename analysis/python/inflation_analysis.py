"""
Inflation Analysis Script
Author: Economic Observatory Team
Date: 2024-10-16
Description: Analyzes inflation trends and creates visualizations
Data Source: Local CSV files
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set plot style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def load_inflation_data(filepath):
    """
    Load inflation data from CSV file.

    Args:
        filepath: Path to CSV file

    Returns:
        DataFrame with inflation data
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")

    df = pd.read_csv(filepath, comment='#')
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    return df


def calculate_inflation_metrics(df):
    """
    Calculate additional inflation metrics.

    Args:
        df: DataFrame with inflation data

    Returns:
        DataFrame with additional metrics
    """
    df = df.copy()

    # Month-over-month change in inflation rate
    df['mom_change'] = df['inflation_rate'].diff()

    # 12-month moving average
    df['ma_12'] = df['inflation_rate'].rolling(window=12, min_periods=1).mean()

    # Year-over-year change (12 months ago)
    df['yoy_change'] = df['inflation_rate'] - df['inflation_rate'].shift(12)

    return df


def create_inflation_plot(df, output_path='visualizations/inflation_analysis.png'):
    """
    Create comprehensive inflation visualization.

    Args:
        df: DataFrame with inflation data
        output_path: Path to save the plot
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot 1: Inflation rate over time
    ax1.plot(df['date'], df['inflation_rate'],
             label='Inflation Rate', color='darkred', linewidth=2)
    ax1.plot(df['date'], df['ma_12'],
             label='12-Month Moving Average',
             color='blue', linewidth=1.5, linestyle='--', alpha=0.7)

    # Add target line
    ax1.axhline(y=3.0, color='green', linestyle='--',
                linewidth=1.5, label='Banco de México Target (3%)')

    # Shade high inflation periods
    ax1.fill_between(df['date'], 3, df['inflation_rate'],
                      where=(df['inflation_rate'] > 3),
                      alpha=0.2, color='red', label='Above Target')

    ax1.set_title('Mexico Inflation Rate - Annual Percentage',
                  fontsize=14, fontweight='bold')
    ax1.set_xlabel('Date', fontsize=11)
    ax1.set_ylabel('Inflation Rate (%)', fontsize=11)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)

    # Plot 2: Month-over-month changes
    colors = ['red' if x > 0 else 'green' for x in df['mom_change'].fillna(0)]
    ax2.bar(df['date'], df['mom_change'], color=colors, alpha=0.6)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    ax2.set_title('Month-over-Month Change in Inflation Rate',
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=11)
    ax2.set_ylabel('Change (percentage points)', fontsize=11)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save plot
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {output_path}")

    plt.close()


def generate_inflation_summary(df):
    """
    Generate summary statistics for inflation.

    Args:
        df: DataFrame with inflation data

    Returns:
        Dictionary with summary statistics
    """
    print("\n" + "="*60)
    print("INFLATION ANALYSIS SUMMARY")
    print("="*60)

    # Latest values
    latest = df.iloc[-1]
    print(f"\nLatest Inflation ({latest['date'].strftime('%Y-%m-%d')}): {latest['inflation_rate']:.2f}%")

    if 'cpi' in df.columns:
        print(f"Latest CPI: {latest['cpi']:.2f}")

    # Period statistics
    print("\nInflation Statistics:")
    print(f"  Mean:     {df['inflation_rate'].mean():.2f}%")
    print(f"  Median:   {df['inflation_rate'].median():.2f}%")
    print(f"  Min:      {df['inflation_rate'].min():.2f}%")
    print(f"  Max:      {df['inflation_rate'].max():.2f}%")
    print(f"  Std Dev:  {df['inflation_rate'].std():.2f}%")

    # Trend analysis (last 12 months)
    print("\nTrend Analysis (last 12 months):")
    recent = df.tail(12)

    if len(recent) >= 2:
        change = recent['inflation_rate'].iloc[-1] - recent['inflation_rate'].iloc[0]
        trend = "INCREASING ↑" if change > 0 else "DECREASING ↓"

        print(f"  Trend: {trend}")
        print(f"  Change: {change:.2f} percentage points")

    # Above target analysis
    above_target = df[df['inflation_rate'] > 3.0]
    pct_above = (len(above_target) / len(df)) * 100

    print(f"\nAbove Target Analysis:")
    print(f"  Months above 3% target: {len(above_target)} ({pct_above:.1f}%)")

    stats = {
        'mean': df['inflation_rate'].mean(),
        'median': df['inflation_rate'].median(),
        'min': df['inflation_rate'].min(),
        'max': df['inflation_rate'].max(),
        'std': df['inflation_rate'].std(),
        'current': latest['inflation_rate'],
        'months_above_target': len(above_target)
    }

    return stats


def main():
    """Main execution function."""
    print("Starting Inflation Analysis...\n")

    # Load data
    print("Loading inflation data...")
    data_path = 'data/inflation/mexico_inflation_sample.csv'

    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        print("Please ensure the data file exists.")
        return None

    inflation_data = load_inflation_data(data_path)
    print(f"Loaded {len(inflation_data)} observations")

    # Calculate metrics
    print("\nCalculating inflation metrics...")
    inflation_data = calculate_inflation_metrics(inflation_data)

    # Generate summary
    summary_stats = generate_inflation_summary(inflation_data)

    # Create visualization
    print("\nCreating visualization...")
    create_inflation_plot(inflation_data)

    print("\nAnalysis complete!")

    return {
        'data': inflation_data,
        'stats': summary_stats
    }


if __name__ == '__main__':
    results = main()
