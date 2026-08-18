# ==============================================================================
# International Basketball Analytics (2005-2024)
# R Functional Layer: Independent Statistical Validation Functions
# ==============================================================================

#' Compute Non-Parametric Bootstrap Confidence Intervals for the Mean
#'
#' @param x Numeric vector of observations
#' @param n_boot Number of bootstrap resamples (default: 5000)
#' @param conf_level Confidence level (default: 0.95)
#' @param seed Random seed for reproducibility
#' @return A list with point estimate, lower bound, and upper bound
#' @export
bootstrap_ci_mean <- function(x, n_boot = 5000, conf_level = 0.95, seed = 42) {
  set.seed(seed)
  clean_x <- x[!is.na(x)]
  n <- length(clean_x)
  if (n < 2) {
    return(list(mean = mean(clean_x), ci_lower = NA, ci_upper = NA, n = n))
  }
  
  boot_means <- replicate(n_boot, {
    sample_idx <- sample.int(n, size = n, replace = TRUE)
    mean(clean_x[sample_idx])
  })
  
  alpha <- 1 - conf_level
  ci <- quantile(boot_means, probs = c(alpha / 2, 1 - alpha / 2))
  
  list(
    mean = mean(clean_x),
    ci_lower = as.numeric(ci[1]),
    ci_upper = as.numeric(ci[2]),
    conf_level = conf_level,
    n_boot = n_boot,
    n = n
  )
}

#' Two-Sample Permutation Test for Difference in Means
#'
#' Evaluates whether the observed difference in means between two groups is statistically significant.
#'
#' @param group_a Numeric vector of Group A observations
#' @param group_b Numeric vector of Group B observations
#' @param n_permutations Number of random permutations (default: 10000)
#' @param seed Random seed
#' @return A list with observed diff, p-value, and permutation distribution summary
#' @export
permutation_test_diff <- function(group_a, group_b, n_permutations = 10000, seed = 42) {
  set.seed(seed)
  a <- group_a[!is.na(group_a)]
  b <- group_b[!is.na(group_b)]
  
  n_a <- length(a)
  n_b <- length(b)
  
  obs_diff <- mean(a) - mean(b)
  combined <- c(a, b)
  total_n <- length(combined)
  
  perm_diffs <- replicate(n_permutations, {
    shuffled <- sample(combined, size = total_n, replace = FALSE)
    mean(shuffled[1:n_a]) - mean(shuffled[(n_a + 1):total_n])
  })
  
  p_val <- mean(abs(perm_diffs) >= abs(obs_diff))
  
  list(
    observed_diff = obs_diff,
    p_value = p_val,
    n_permutations = n_permutations,
    mean_a = mean(a),
    mean_b = mean(b)
  )
}

#' Evaluate Ranking Stability across Eras or Replicas (Spearman Rank Correlation)
#'
#' @param rank_1 Numeric vector of first ranking / score
#' @param rank_2 Numeric vector of second ranking / score
#' @return A list with Spearman rho and asymptotic p-value
#' @export
evaluate_rank_stability <- function(rank_1, rank_2) {
  valid <- !is.na(rank_1) & !is.na(rank_2)
  r1 <- rank_1[valid]
  r2 <- rank_2[valid]
  
  test_res <- cor.test(r1, r2, method = "spearman", exact = FALSE)
  
  list(
    spearman_rho = as.numeric(test_res$estimate),
    p_value = as.numeric(test_res$p.value),
    n = sum(valid)
  )
}

#' Compare Two Empirical Distributions via Kolmogorov-Smirnov Test
#'
#' @param sample_1 Numeric vector of sample 1
#' @param sample_2 Numeric vector of sample 2
#' @return A list with KS D-statistic and p-value
#' @export
compare_distributions_ks <- function(sample_1, sample_2) {
  s1 <- sample_1[!is.na(sample_1)]
  s2 <- sample_2[!is.na(sample_2)]
  
  ks_res <- ks.test(s1, s2)
  
  list(
    statistic_D = as.numeric(ks_res$statistic),
    p_value = as.numeric(ks_res$p.value)
  )
}
