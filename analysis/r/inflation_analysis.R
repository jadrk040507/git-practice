# Inflation Analysis Script
# Author: Economic Observatory Team
# Date: 2024-10-16
# Description: Analyzes inflation trends and creates forecasts
# Data Source: Local CSV files or APIs

library(tidyverse)
library(lubridate)
library(forecast)
library(scales)
library(dotenv)

# Load environment variables from .env file
load_dot_env()

#' Load inflation data from CSV
#'
#' @param filepath Path to CSV file
#' @return Tibble with inflation data
load_inflation_data <- function(filepath) {

  if (!file.exists(filepath)) {
    stop(paste("File not found:", filepath))
  }

  data <- read_csv(filepath, show_col_types = FALSE, comment = "#") %>%
    mutate(date = ymd(date))

  return(data)
}

#' Calculate inflation statistics
#'
#' @param data Inflation data frame
#' @return Data frame with additional metrics
calculate_inflation_metrics <- function(data) {

  data <- data %>%
    arrange(date) %>%
    mutate(
      # Month-over-month change
      mom_change = inflation_rate - lag(inflation_rate, 1),
      # 12-month moving average
      ma_12 = zoo::rollmean(inflation_rate, 12, fill = NA, align = "right"),
      # Core vs headline spread (if core_inflation exists)
      spread = if("core_inflation" %in% names(data))
                 inflation_rate - core_inflation
               else NA
    )

  return(data)
}

#' Create inflation visualization
#'
#' @param data Inflation data
#' @param output_path Path to save plot
create_inflation_plot <- function(data, output_path = "../../visualizations/inflation_analysis.png") {

  # Create plot
  p <- ggplot(data, aes(x = date, y = inflation_rate)) +
    geom_line(color = "darkred", size = 1.2) +
    geom_hline(yintercept = 3.0, linetype = "dashed", color = "green", size = 0.8) +
    annotate("text", x = min(data$date), y = 3.2,
             label = "Meta Banco de México (3%)",
             hjust = 0, color = "darkgreen", size = 3.5) +

    # Add shaded area for high inflation
    geom_ribbon(aes(ymin = 3, ymax = pmax(inflation_rate, 3)),
                fill = "red", alpha = 0.2) +

    # Labels and theme
    labs(
      title = "Tasa de Inflación Anual - México",
      subtitle = "Variación porcentual anual del IPC",
      x = "Fecha",
      y = "Inflación (%)",
      caption = "Fuente: INEGI / Banco de México"
    ) +
    theme_minimal() +
    theme(
      plot.title = element_text(size = 14, face = "bold"),
      plot.subtitle = element_text(size = 11, color = "gray30"),
      axis.text = element_text(size = 10),
      panel.grid.minor = element_blank()
    ) +
    scale_y_continuous(labels = scales::percent_format(scale = 1))

  # Save plot
  ggsave(output_path, p, width = 10, height = 6, dpi = 300)
  cat(paste("Plot saved to:", output_path, "\n"))

  return(p)
}

#' Generate inflation summary
#'
#' @param data Inflation data
generate_inflation_summary <- function(data) {

  cat("\n=== INFLATION ANALYSIS SUMMARY ===\n\n")

  # Latest values
  latest <- data %>% tail(1)
  cat(paste("Latest Inflation (", format(latest$date, "%Y-%m-%d"), "):",
            round(latest$inflation_rate, 2), "%\n\n"))

  # Period statistics
  cat("Inflation Statistics:\n")
  stats <- data %>%
    summarise(
      mean_inflation = mean(inflation_rate, na.rm = TRUE),
      median_inflation = median(inflation_rate, na.rm = TRUE),
      min_inflation = min(inflation_rate, na.rm = TRUE),
      max_inflation = max(inflation_rate, na.rm = TRUE),
      sd_inflation = sd(inflation_rate, na.rm = TRUE),
      current_inflation = tail(inflation_rate, 1)
    )

  print(stats)

  # Trend analysis
  cat("\n\nTrend Analysis (last 12 months):\n")
  recent <- data %>% tail(12)

  if (nrow(recent) >= 2) {
    trend <- if(recent$inflation_rate[nrow(recent)] > recent$inflation_rate[1]) {
      "INCREASING ↑"
    } else {
      "DECREASING ↓"
    }

    change <- recent$inflation_rate[nrow(recent)] - recent$inflation_rate[1]
    cat(paste("Trend:", trend, "\n"))
    cat(paste("Change:", round(change, 2), "percentage points\n"))
  }

  return(stats)
}

#' Main execution function
main <- function() {

  cat("Starting Inflation Analysis...\n\n")

  # Load data
  cat("Loading inflation data...\n")
  data_path <- "../../data/inflation/mexico_inflation_sample.csv"

  if (!file.exists(data_path)) {
    cat("Data file not found at:", data_path, "\n")
    cat("Please ensure the data file exists or run data collection script first.\n")
    return(NULL)
  }

  inflation_data <- load_inflation_data(data_path)

  # Calculate metrics
  cat("Calculating inflation metrics...\n")
  inflation_data <- calculate_inflation_metrics(inflation_data)

  # Generate summary
  summary_stats <- generate_inflation_summary(inflation_data)

  # Create visualization
  cat("\nCreating visualization...\n")
  plot <- create_inflation_plot(inflation_data)

  cat("\nAnalysis complete!\n")

  return(list(
    data = inflation_data,
    stats = summary_stats,
    plot = plot
  ))
}

# Run main function if script is executed directly
if (!interactive()) {
  results <- main()
}
