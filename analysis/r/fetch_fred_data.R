# FRED API Data Fetcher
# Author: Economic Observatory Team
# Date: 2024-10-16
# Description: Fetches economic data from FRED API
# Data Source: Federal Reserve Economic Data (FRED)

# Load required libraries
library(httr)
library(jsonlite)
library(tidyverse)
library(lubridate)
library(dotenv)

# Load environment variables from .env file
load_dot_env()

# Get API key from environment
FRED_API_KEY <- Sys.getenv("FRED_API_KEY")

if (FRED_API_KEY == "") {
  stop("ERROR: FRED_API_KEY not found in environment variables.
       Please create a .env file with your API key.
       See .env.example for template.")
}

# Base URL for FRED API
FRED_BASE_URL <- "https://api.stlouisfed.org/fred/series/observations"

#' Fetch data from FRED API
#'
#' @param series_id FRED series ID (e.g., "GDP", "CPIAUCSL", "UNRATE")
#' @param start_date Start date in YYYY-MM-DD format
#' @param end_date End date in YYYY-MM-DD format
#' @return Data frame with date and value columns
fetch_fred_data <- function(series_id, start_date = "2020-01-01",
                           end_date = Sys.Date()) {

  # Build API request
  url <- paste0(FRED_BASE_URL,
                "?series_id=", series_id,
                "&api_key=", FRED_API_KEY,
                "&file_type=json",
                "&observation_start=", start_date,
                "&observation_end=", end_date)

  # Make API request
  response <- GET(url)

  # Check if request was successful
  if (status_code(response) != 200) {
    stop(paste("API request failed with status:", status_code(response)))
  }

  # Parse JSON response
  data <- fromJSON(content(response, "text", encoding = "UTF-8"))

  # Extract observations
  observations <- data$observations %>%
    as_tibble() %>%
    mutate(
      date = ymd(date),
      value = as.numeric(value)
    ) %>%
    select(date, value) %>%
    filter(!is.na(value))

  # Add series name
  observations$series_id <- series_id

  return(observations)
}

#' Main execution function
main <- function() {

  cat("Fetching economic data from FRED...\n\n")

  # Example: Fetch US GDP data
  cat("Fetching GDP data...\n")
  gdp_data <- fetch_fred_data("GDP", "2020-01-01")
  cat(paste("  Retrieved", nrow(gdp_data), "observations\n"))

  # Example: Fetch CPI (inflation) data
  cat("Fetching CPI data...\n")
  cpi_data <- fetch_fred_data("CPIAUCSL", "2020-01-01")
  cat(paste("  Retrieved", nrow(cpi_data), "observations\n"))

  # Example: Fetch unemployment rate
  cat("Fetching unemployment data...\n")
  unemployment_data <- fetch_fred_data("UNRATE", "2020-01-01")
  cat(paste("  Retrieved", nrow(unemployment_data), "observations\n"))

  # Save to CSV files
  cat("\nSaving data to CSV files...\n")
  write_csv(gdp_data, "../../data/gdp/usa_gdp_fred.csv")
  write_csv(cpi_data, "../../data/inflation/usa_cpi_fred.csv")
  write_csv(unemployment_data, "../../data/unemployment/usa_unemployment_fred.csv")

  cat("\nData fetch complete!\n")
  cat("Files saved to data/ directory\n")

  # Return combined data
  return(list(
    gdp = gdp_data,
    cpi = cpi_data,
    unemployment = unemployment_data
  ))
}

# Run main function if script is executed directly
if (!interactive()) {
  main()
}
