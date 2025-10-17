# R Analysis Scripts

R scripts for economic data analysis using tidyverse, forecast, and econometric packages.

## Setup

### 1. Install Required Packages

```r
# Core packages
install.packages(c("tidyverse", "forecast", "tseries", "zoo",
                   "lubridate", "ggplot2", "dplyr", "readr"))

# For API access
install.packages(c("httr", "jsonlite"))

# For environment variables
install.packages("dotenv")
```

### 2. Configure Environment Variables

Before running scripts that access APIs, you need to set up your `.env` file:

```bash
# Copy the template
cp ../../.env.example ../../.env

# Edit .env and add your API keys
# See SETUP_ENV.md for detailed instructions
```

## Available Scripts

### `fetch_fred_data.R`
Fetches economic data from FRED API.

**Requirements**:
- FRED API key in `.env` file
- Internet connection

**Usage**:
```r
source("fetch_fred_data.R")
# Data will be saved to ../../data/ directories
```

### `gdp_analysis.R`
Analyzes GDP growth rates and trends.

**Requirements**:
- GDP data in `../../data/gdp/` directory
- Run `fetch_fred_data.R` first or use sample data

**Usage**:
```r
source("gdp_analysis.R")
# Creates visualization in ../../visualizations/
```

### `inflation_analysis.R`
Analyzes inflation trends and forecasts.

**Requirements**:
- Inflation data in `../../data/inflation/` directory

**Usage**:
```r
source("inflation_analysis.R")
# Creates visualization in ../../visualizations/
```

## Script Template

Use this template for new R analysis scripts:

```r
# [Analysis Name]
# Author: [Your Name]
# Date: [YYYY-MM-DD]
# Description: [Brief description]
# Data Source: [Source name and URL]

# Load required libraries
library(tidyverse)
library(forecast)
library(dotenv)

# Load environment variables from .env file
load_dot_env()

# Get API keys if needed
api_key <- Sys.getenv("FRED_API_KEY")

# Function to load data
load_data <- function(filepath) {
  read_csv(filepath, comment = "#")
}

# Function to perform analysis
analyze <- function(data) {
  results <- data %>%
    # Your transformations
    mutate(new_column = value * 2)

  return(results)
}

# Function to create visualizations
visualize <- function(results) {
  plot <- ggplot(results, aes(x = date, y = value)) +
    geom_line() +
    labs(title = "Title",
         x = "X Label",
         y = "Y Label") +
    theme_minimal()

  ggsave("../../visualizations/output.png", plot)
  return(plot)
}

# Main execution
main <- function() {
  data <- load_data("../../data/...")
  results <- analyze(data)
  visualize(results)
  print("Analysis complete!")
}

# Run if script is executed directly
if (!interactive()) {
  main()
}
```

## Common Patterns

### Loading Environment Variables

**Always include at the top of scripts that use APIs:**

```r
library(dotenv)

# Load .env file
load_dot_env()

# Access variables
api_key <- Sys.getenv("API_KEY_NAME")

# Check if key exists
if (api_key == "") {
  stop("API key not found! Please configure .env file.")
}
```

### Error Handling

```r
# Safe file loading
load_data_safe <- function(filepath) {
  if (!file.exists(filepath)) {
    stop(paste("File not found:", filepath))
  }

  tryCatch({
    read_csv(filepath, comment = "#")
  }, error = function(e) {
    stop(paste("Error loading file:", e$message))
  })
}
```

### API Requests

```r
fetch_api_data <- function(url, api_key) {
  response <- GET(url, add_headers(Authorization = paste("Bearer", api_key)))

  if (status_code(response) != 200) {
    stop(paste("API request failed:", status_code(response)))
  }

  content(response, "parsed")
}
```

## Troubleshooting

### "Error: API key not found"

1. Check `.env` file exists in project root
2. Verify variable name: `FRED_API_KEY=your_key_here`
3. Make sure you called `load_dot_env()`

### "Package 'dotenv' not found"

```r
install.packages("dotenv")
```

### "File not found" errors

Make sure you're running scripts from the correct directory:

```r
# Check current directory
getwd()

# Set working directory if needed
setwd("path/to/git-practice/analysis/r")
```

### Visualization not saving

```r
# Create directory if it doesn't exist
dir.create("../../visualizations", showWarnings = FALSE, recursive = TRUE)

# Then save plot
ggsave("../../visualizations/plot.png", plot)
```

## Best Practices

1. **Always use `dotenv`** for API keys and sensitive data
2. **Comment your code** - explain what and why
3. **Use functions** - keep code modular and reusable
4. **Handle errors** - check file existence, API responses
5. **Document dependencies** - list required packages
6. **Use relative paths** - makes code portable
7. **Follow style guide** - use tidyverse style

## Resources

- [tidyverse style guide](https://style.tidyverse.org/)
- [R for Data Science](https://r4ds.had.co.nz/)
- [dotenv package docs](https://github.com/gaborcsardi/dotenv)
- [FRED API docs](https://fred.stlouisfed.org/docs/api/)

---

**Need help?** See [SETUP_ENV.md](../../SETUP_ENV.md) or ask your instructor!
