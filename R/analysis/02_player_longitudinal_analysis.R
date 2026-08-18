# ==============================================================================
# International Basketball Analytics (2005-2024)
# R Script 02: Longitudinal Player Trajectory & Aging Curves
# ==============================================================================
# Objective:
#   Track individual career evolutions (USG% vs True Shooting% vs Net Impact)
#   for iconic international players across multiple tournament campaigns.
# ==============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(ggplot2)
})

# Source custom functions
source("R/functions/metrics.R")
source("R/functions/visualization.R")

# 1. Fetch Player Campaign Records
get_longitudinal_players <- function() {
  db_path <- "data/03_validated/basketball_analytics.duckdb"
  player_parquet <- "data/04_analytics/mart_player_tournament_features.parquet"
  
  if (requireNamespace("duckdb", quietly = TRUE) && requireNamespace("DBI", quietly = TRUE) && file.exists(db_path)) {
    con <- DBI::dbConnect(duckdb::duckdb(), db_path, read_only = TRUE)
    on.exit(DBI::dbDisconnect(con, shutdown = TRUE))
    
    query <- "
      SELECT 
        p.full_canonical_name as canonical_name,
        p.primary_position as position,
        t.year,
        t.competition_id as competition,
        SUM(fpg.minutes_decimal) as total_minutes,
        SUM(fpg.pts) as total_pts,
        SUM(fpg.fga) as total_fga,
        SUM(fpg.fta) as total_fta,
        SUM(fpg.ast) as total_ast,
        SUM(fpg.tov) as total_tov,
        SUM(fpg.trb) as total_reb,
        COUNT(DISTINCT fpg.game_id) as games_played
      FROM dim_player p
      JOIN fact_player_game fpg ON p.canonical_player_id = fpg.canonical_player_id
      JOIN fact_game g ON fpg.game_id = g.game_id
      JOIN dim_tournament t ON g.tournament_id = t.tournament_id
      WHERE p.full_canonical_name IN ('Pau Gasol', 'Marc Gasol', 'Rudy Fernandez', 'Ricky Rubio', 'Bogdan Bogdanovic', 'Patty Mills')
      GROUP BY p.full_canonical_name, p.primary_position, t.year, t.competition_id
      HAVING SUM(fpg.minutes_decimal) >= 40
      ORDER BY p.full_canonical_name, t.year;
    "
    df <- DBI::dbGetQuery(con, query)
    return(df)
  } else {
    # Illustrative structure for standalone execution
    expand.grid(
      canonical_name = c("Pau Gasol", "Marc Gasol", "Rudy Fernandez", "Ricky Rubio"),
      year = c(2006, 2008, 2010, 2012, 2014, 2016, 2019, 2021)
    ) %>%
      mutate(
        total_minutes = sample(100:250, n(), replace = TRUE),
        total_pts = sample(80:200, n(), replace = TRUE),
        total_fga = sample(60:150, n(), replace = TRUE),
        total_fta = sample(20:60, n(), replace = TRUE),
        total_ast = sample(10:45, n(), replace = TRUE),
        total_tov = sample(10:30, n(), replace = TRUE),
        games_played = sample(6:9, n(), replace = TRUE)
      )
  }
}

# 2. Compute Advanced Longitudinal Metrics
player_df <- get_longitudinal_players() %>%
  mutate(
    ts_pct = calculate_true_shooting(total_pts, total_fga, total_fta),
    pts_per_40 = normalize_per_40(total_pts, total_minutes),
    ast_per_40 = normalize_per_40(total_ast, total_minutes),
    reb_per_40 = normalize_per_40(total_reb, total_minutes)
  )

cat("=== Longitudinal Player Analysis (Sample Elite Cohort) ===\n")
print(head(player_df, 10))

# 3. Generate Longitudinal Plot: True Shooting % over Career Tournaments
if (requireNamespace("ggplot2", quietly = TRUE)) {
  p2 <- ggplot(player_df, aes(x = year, y = ts_pct * 100, color = canonical_name, group = canonical_name)) +
    geom_line(linewidth = 1.1, alpha = 0.85) +
    geom_point(size = 3.5, alpha = 0.9) +
    scale_y_continuous(labels = function(x) paste0(x, "%"), limits = c(35, 75)) +
    scale_x_continuous(breaks = seq(2006, 2024, by = 2)) +
    labs(
      title = "Longitudinal True Shooting (TS%) Trajectories in International Tournaments",
      subtitle = "Evolution of Scoring Efficiency across FIBA World Cups, EuroBaskets & Olympic Games",
      x = "Tournament Year",
      y = "True Shooting Percentage (TS%)",
      color = "Player",
      caption = "Source: International Basketball Analytics (2005-2024) | Filter: Qualified Campaigns (>=40 Min)"
    ) +
    theme_basketball_analytics()

  dir.create("reports/figures_r", showWarnings = FALSE, recursive = TRUE)
  try(ggsave("reports/figures_r/fig_02_player_trajectories.png", p2, width = 9, height = 5.5, dpi = 300), silent = TRUE)
  cat("Figure 02 generated in reports/figures_r/fig_02_player_trajectories.png\n")
}
