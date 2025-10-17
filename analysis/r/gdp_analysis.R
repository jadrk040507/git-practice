# GDP Growth Analysis
# Author: Economic Observatory Team
# Date: 2024-10-16
# Description: Analyzes GDP growth trends and creates visualizations
# Data Source: Local CSV files or FRED API

library(tidyverse)
library(lubridate)
library(scales)
library(forecast)
library(dotenv)

# Load environment variables from .env file
load_dot_env()

#' Load GDP data from CSV
#'
#' @param filepath Path to CSV file
#' @return Tibble with GDP data
load_gdp_data <- function(filepath) {

  if (!file.exists(filepath)) {
    stop(paste("File not found:", filepath))
  }

  data <- read_csv(filepath, show_col_types = FALSE) %>%
    mutate(date = ymd(date))

  return(data)
}

#' Calculate growth rates
#'
#' @param data GDP data frame
#' @return Data frame with growth rates added
calculate_growth_rates <- function(data) {

  data <- data %>%
    arrange(date) %>%
    mutate(
      # Quarter-over-quarter growth (annualized)
      qoq_growth = (value / lag(value, 1) - 1) * 100,
      # Year-over-year growth
      yoy_growth = (value / lag(value, 4) - 1) * 100
    )

  return(data)
}

#' Create GDP visualization
#'
#' @param data GDP data with growth rates
#' @param output_path Path to save plot
create_gdp_plot <- function(data, output_path = "../../visualizations/gdp_analysis.png") {

  # Create dual-axis plot
  p <- ggplot(data, aes(x = date)) +
    # GDP level (bars)
    geom_col(aes(y = value / 1000), fill = "steelblue", alpha = 0.6) +
    # Growth rate (line)
    geom_line(aes(y = yoy_growth * 1000), color = "darkred", size = 1) +
    geom_hline(yintercept = 0, linetype = "dashed", color = "gray40") +

    # Labels and theme
    labs(
      title = "GDP Level and Year-over-Year Growth Rate",
      subtitle = "United States, 2020-2024",
      x = "Date",
      y = "GDP (Billions USD)",
      caption = "Source: Federal Reserve Economic Data (FRED)"
    ) +
    theme_minimal() +
    theme(
      plot.title = element_text(size = 14, face = "bold"),
      plot.subtitle = element_text(size = 11, color = "gray30"),
      axis.text = element_text(size = 10),
      panel.grid.minor = element_blank()
    )

  # Save plot
  ggsave(output_path, p, width = 10, height = 6, dpi = 300)
  cat(paste("Plot saved to:", output_path, "\n"))

  return(p)
}

#' Generate summary statistics
#'
#' @param data GDP data with growth rates
generate_summary <- function(data) {

  cat("\n=== GDP ANALYSIS SUMMARY ===\n\n")

  # Latest values
  latest <- data %>% filter(!is.na(yoy_growth)) %>% tail(1)
  cat(paste("Latest GDP (", format(latest$date, "%Y-%m-%d"), "):",
            dollar(latest$value), "\n"))
  cat(paste("Year-over-Year Growth:",
            round(latest$yoy_growth, 2), "%\n\n"))

  # Period statistics
  cat("Growth Rate Statistics:\n")
  stats <- data %>%
    filter(!is.na(yoy_growth)) %>%
    summarise(
      mean_growth = mean(yoy_growth, na.rm = TRUE),
      median_growth = median(yoy_growth, na.rm = TRUE),
      min_growth = min(yoy_growth, na.rm = TRUE),
      max_growth = max(yoy_growth, na.rm = TRUE),
      sd_growth = sd(yoy_growth, na.rm = TRUE)
    )

  print(stats)
  cat("\n")

  return(stats)
}

#' Main execution function
main <- function() {

  cat("Starting GDP Analysis...\n\n")

  # Load data
  cat("Loading GDP data...\n")
  data_path <- "../../data/gdp/usa_gdp_fred.csv"

  if (!file.exists(data_path)) {
    cat("Data file not found. Please run fetch_fred_data.R first.\n")
    return(NULL)
  }

  gdp_data <- load_gdp_data(data_path)

  # Calculate growth rates
  cat("Calculating growth rates...\n")
  gdp_data <- calculate_growth_rates(gdp_data)

  # Generate summary
  summary_stats <- generate_summary(gdp_data)

  # Create visualization
  cat("\nCreating visualization...\n")
  plot <- create_gdp_plot(gdp_data)

  cat("\nAnalysis complete!\n")

  return(list(
    data = gdp_data,
    stats = summary_stats,
    plot = plot
  ))
}

# Run main function if script is executed directly
if (!interactive()) {
  results <- main()
}
