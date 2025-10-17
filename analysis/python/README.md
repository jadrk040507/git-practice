# Python Analysis Scripts

Python scripts for economic data analysis using pandas, numpy, matplotlib, and more.

## Setup

### 1. Install Required Packages

```bash
# Install all required packages
pip install -r ../../requirements.txt
```

Or install individually:

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn python-dotenv requests
```

### 2. Configure Environment Variables

Before running scripts that access APIs, set up your `.env` file:

```bash
# Copy the template
cp ../../.env.example ../../.env

# Edit .env and add your API keys
# See SETUP_ENV.md for detailed instructions
```

## Available Scripts

### `fetch_worldbank_data.py`
Fetches economic indicators from World Bank API.

**Usage**:
```bash
python fetch_worldbank_data.py
```

### `inflation_analysis.py`
Analyzes inflation trends and creates visualizations.

**Usage**:
```bash
python inflation_analysis.py
```

## Script Template

Use this template to start a new analysis:

```python
"""
[Analysis Name]
Author: [Your Name]
Date: [YYYY-MM-DD]
Description: [Brief description]
Data Source: [Source name and URL]
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_data(filepath):
    """Load and prepare data."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath, comment='#')
    df['date'] = pd.to_datetime(df['date'])
    return df

def main():
    """Main execution function."""
    print("Starting analysis...")
    # Your code here
    print("Analysis complete!")

if __name__ == '__main__':
    main()
```

**Need help?** See [SETUP_ENV.md](../../SETUP_ENV.md) or ask your instructor!
