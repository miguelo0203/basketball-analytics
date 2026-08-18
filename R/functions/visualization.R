# ==============================================================================
# International Basketball Analytics (2005-2024)
# R Functional Layer: Visual Themes & Plot Styling
# ==============================================================================

# Palette for the 6 Functional Archetypes
ARCHETYPE_COLORS <- c(
  "Primary Initiator"   = "#1f77b4",
  "Secondary Playmaker" = "#2ca02c",
  "Floor Spacer"        = "#ff7f0e",
  "Versatile Wing"      = "#9467bd",
  "Interior Hub"        = "#d62728",
  "Defensive Anchor"    = "#8c564b"
)

# Palette for Tournament Competitions
COMPETITION_COLORS <- c(
  "EuroBasket"  = "#1B365D",
  "World Cup"   = "#008080",
  "Olympics"    = "#D97706"
)

#' Custom Minimal Theme for Basketball Analytics Publications
#'
#' @param base_size Base font size (default: 11)
#' @param base_family Font family
#' @return A ggplot2 theme object
#' @export
theme_basketball_analytics <- function(base_size = 11, base_family = "sans") {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("Package 'ggplot2' is required for theme_basketball_analytics.")
  }
  
  ggplot2::theme_minimal(base_size = base_size, base_family = base_family) +
    ggplot2::theme(
      plot.title = ggplot2::element_text(face = "bold", size = ggplot2::rel(1.2), color = "#111827", margin = ggplot2::margin(b = 6)),
      plot.subtitle = ggplot2::element_text(size = ggplot2::rel(0.95), color = "#4B5563", margin = ggplot2::margin(b = 10)),
      plot.caption = ggplot2::element_text(size = ggplot2::rel(0.75), color = "#9CA3AF", hjust = 1, margin = ggplot2::margin(t = 8)),
      axis.title = ggplot2::element_text(face = "bold", size = ggplot2::rel(0.9), color = "#374151"),
      axis.text = ggplot2::element_text(size = ggplot2::rel(0.85), color = "#4B5563"),
      panel.grid.minor = ggplot2::element_blank(),
      panel.grid.major = ggplot2::element_line(color = "#E5E7EB", linewidth = 0.5),
      legend.position = "bottom",
      legend.title = ggplot2::element_text(face = "bold", size = ggplot2::rel(0.85)),
      legend.text = ggplot2::element_text(size = ggplot2::rel(0.8)),
      strip.text = ggplot2::element_text(face = "bold", size = ggplot2::rel(0.9), color = "#1F2937"),
      strip.background = ggplot2::element_rect(fill = "#F3F4F6", color = NA)
    )
}

#' Format Percentages for Labels
#'
#' @param x Numeric value between 0 and 1
#' @param digits Number of decimal places
#' @return Formatted string with '%'
#' @export
format_pct <- function(x, digits = 1) {
  sprintf(paste0("%.", digits, "f%%"), x * 100)
}

#' Format Net Rating for Labels
#'
#' @param x Numeric Net Rating value
#' @param digits Number of decimal places
#' @return Formatted string with explicit +/- sign
#' @export
format_rating <- function(x, digits = 1) {
  sprintf(paste0("%+.", digits, "f"), x)
}
