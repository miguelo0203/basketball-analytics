# ==============================================================================
# International Basketball Analytics (2005-2024)
# R Functional Layer: Basketball Metrics & Formulas
# ==============================================================================

#' Calculate Possessions (Pace) for a Team Game
#'
#' Uses Dean Oliver's standard possession estimation formula:
#' Poss = FGA + 0.44 * FTA - ORB + TOV
#'
#' @param fga Field Goals Attempted
#' @param fta Free Throws Attempted
#' @param orb Offensive Rebounds
#' @param tov Turnovers
#' @return Numeric vector of estimated possessions
#' @export
calculate_possessions <- function(fga, fta, orb, tov) {
  pmax(fga + 0.44 * fta - orb + tov, 1.0)
}

#' Calculate Dean Oliver's Four Factors
#'
#' 1. Effective Field Goal Percentage: (FGM + 0.5 * 3PM) / FGA
#' 2. Turnover Ratio: TOV / (FGA + 0.44 * FTA + TOV)
#' 3. Offensive Rebound Percentage: ORB / (ORB + Opponent_DRB)
#' 4. Free Throw Rate: FTA / FGA
#'
#' @param fgm Field Goals Made
#' @param fga Field Goals Attempted
#' @param fg3m 3-Point Field Goals Made
#' @param tov Turnovers
#' @param fta Free Throws Attempted
#' @param orb Offensive Rebounds
#' @param opp_drb Opponent Defensive Rebounds
#' @return A tibble with the four factor metrics
#' @export
calculate_four_factors <- function(fgm, fga, fg3m, tov, fta, orb, opp_drb) {
  efg_pct <- ifelse(fga > 0, (fgm + 0.5 * fg3m) / fga, 0.0)
  tov_pct <- ifelse((fga + 0.44 * fta + tov) > 0, tov / (fga + 0.44 * fta + tov), 0.0)
  orb_pct <- ifelse((orb + opp_drb) > 0, orb / (orb + opp_drb), 0.0)
  ft_rate <- ifelse(fga > 0, fta / fga, 0.0)
  
  data.frame(
    efg_pct = efg_pct,
    tov_pct = tov_pct,
    orb_pct = orb_pct,
    ft_rate = ft_rate
  )
}

#' Calculate Offensive, Defensive, and Net Rating per 100 Possessions
#'
#' @param pts Points Scored
#' @param opp_pts Points Allowed
#' @param poss Estimated Possessions
#' @return A data.frame with off_rtg, def_rtg, and net_rtg
#' @export
calculate_ratings <- function(pts, opp_pts, poss) {
  safe_poss <- pmax(poss, 1.0)
  off_rtg <- (pts / safe_poss) * 100
  def_rtg <- (opp_pts / safe_poss) * 100
  net_rtg <- off_rtg - def_rtg
  
  data.frame(
    off_rtg = off_rtg,
    def_rtg = def_rtg,
    net_rtg = net_rtg
  )
}

#' Calculate True Shooting Percentage (TS%)
#'
#' Formula: PTS / (2 * (FGA + 0.44 * FTA))
#'
#' @param pts Points Scored
#' @param fga Field Goals Attempted
#' @param fta Free Throws Attempted
#' @return Numeric vector of True Shooting percentages
#' @export
calculate_true_shooting <- function(pts, fga, fta) {
  denom <- 2 * (fga + 0.44 * fta)
  ifelse(denom > 0, pts / denom, 0.0)
}

#' Normalize Counting Statistics to 40 Minutes
#'
#' Standard FIBA regulation game length is 40 minutes.
#'
#' @param stat Vector of counting statistics (points, rebounds, assists, etc.)
#' @param minutes Vector of minutes played
#' @return Normalized per-40 numeric vector
#' @export
normalize_per_40 <- function(stat, minutes) {
  ifelse(minutes > 0, (stat / minutes) * 40, 0.0)
}

#' Calculate Assist-to-Turnover Ratio
#'
#' @param ast Assists
#' @param tov Turnovers
#' @return Numeric vector of AST/TOV ratio
#' @export
calculate_ast_tov_ratio <- function(ast, tov) {
  ifelse(tov > 0, ast / tov, ifelse(ast > 0, ast / 0.5, 0.0))
}
