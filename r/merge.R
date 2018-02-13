original <- read.csv("git_ori.csv", sep = ",",
                     header = TRUE, row.names = NULL)
revised <- read.csv("git_rev.csv", sep = ",",
                    header = TRUE, row.names = NULL)

output <- data.frame()

m_t_or_f <- c("filename", "num", "ori", "rev")

merged <- merge(original, revised,
                by = c("filename", "num", "ori", "rev"))
metricses <- names(original)

metricses <- metricses[(1 + length(m_t_or_f)):length(metricses)]

for (i in 1:length(metricses)){
    metrics <- metricses[i]

    metrics_plus <- paste(metrics, "plus", sep = "_")
    metrics_minus <- paste(metrics, "minus", sep = "_")
    m_t_or_f <- append(m_t_or_f, c(metrics_plus, metrics_minus))

    metrics.x <- paste(metrics, "x", sep = ".")
    metrics.y <- paste(metrics, "y", sep = ".")
    merged[, metrics] <- merged[, metrics.y] - merged[, metrics.x]

    merged[, metrics_plus] <- as.numeric( (merged[, metrics] > 0))
    merged[, metrics_minus] <- as.numeric( (merged[, metrics] < 0))
}
merged <- subset(merged, TRUE, m_t_or_f)


for (i in 1:length(metricses)){
    metrics <- metricses[i]
    original[, metrics] <- as.numeric( (original[, metrics] > 0))
}

new_merged <- merge(x = original, y = merged,
                    by = c("filename", "num", "ori", "rev"),
                    all = FALSE)

write.csv(new_merged,
          "git_merged.csv",
          quote = TRUE, row.names = FALSE)