# ==============================================================================
# International Basketball Analytics (2005-2024)
# Master R Analysis Runner: Sequential End-to-End Execution
# ==============================================================================

scripts <- c(
  "R/analysis/01_eda_tournaments.R",
  "R/analysis/02_player_longitudinal_analysis.R",
  "R/analysis/03_role_stability.R",
  "R/analysis/04_team_four_factors.R",
  "R/analysis/05_player_distributions.R",
  "R/analysis/06_statistical_validation.R"
)

cat("================================================================================\n")
cat("STARTING END-TO-END R ANALYSIS PIPELINE EXECUTION\n")
cat("================================================================================\n\n")

results <- list()
overall_start <- Sys.time()

for (s in scripts) {
  cat(sprintf(">>> Executing: %s ...\n", s))
  start_time <- Sys.time()
  
  status <- tryCatch({
    source(s, local = new.env())
    "SUCCESS"
  }, error = function(e) {
    cat(sprintf("    [ERROR]: %s\n", e$message))
    "FAILED"
  })
  
  elapsed <- as.numeric(difftime(Sys.time(), start_time, units = "secs"))
  results[[s]] <- list(status = status, elapsed_sec = elapsed)
  cat(sprintf("    [STATUS]: %s (%.2f seconds)\n\n", status, elapsed))
}

overall_elapsed <- as.numeric(difftime(Sys.time(), overall_start, units = "secs"))

cat("================================================================================\n")
cat("R PIPELINE EXECUTION SUMMARY\n")
cat("================================================================================\n")
for (s in names(results)) {
  cat(sprintf("%-45s | %-8s | %6.2f s\n", s, results[[s]]$status, results[[s]]$elapsed_sec))
}
cat(sprintf("\nTotal Execution Time: %.2f seconds\n", overall_elapsed))
cat("================================================================================\n")
