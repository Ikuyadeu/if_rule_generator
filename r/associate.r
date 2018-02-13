library(arules)

original <- read.csv("git_ori.csv", sep = ",",
                     header = TRUE, row.names = NULL)
df <- read.csv("git_merged.csv")
metricses <- names(original)
m_t_or_f <- c("filename", "num", "ori", "rev")
metricses <- metricses[5:length(metricses)]
metricses <- metricses[(1 + length(m_t_or_f)):length(metricses)]

metrics_plus <- c()
metrics_minus <- c()
for (i in 1:length(metricses)){
    metrics <- metricses[i]
    metrics_plus <- append(metrics_plus, paste(metrics, "plus", sep = "_"))
    metrics_minus <- append(metrics_minus, paste(metrics, "minus", sep = "_"))
}
m_t_or_f <- append(metricses,
                   c(metrics_plus, metrics_minus))
df <- subset(df, T, m_t_or_f)

# closed itemset
df <- subset(df, TRUE, m_t_or_f)
data_tran <- as(as.matrix(df[1:ncol(df)]), "transactions")

rules <- apriori(data_tran,
                 parameter = list(
                                  maxlen = 2,
                                  minlen = 1,
                                  confidence = 0.001
                                  ))
rules <- rules[!is.redundant(rules)]

# Get ini to fin rules
ini_fin <- subset(rules,
                lift > 1 &
                !(rhs %in% metricses |
                lhs %in% append(metrics_plus, metrics_minus)))

for (i in 1:length(metricses)){
    metrics <- metricses[i]
    ini_fin <- subset(ini_fin,
                    !(lhs %in% c(metricses) &
                      rhs %in% paste(metrics, "minus", sep = "_"))
    )
}
ini_fin <- ini_fin[!is.redundant(ini_fin)]

ini_fin_df <- data.frame(lhs = labels(lhs(ini_fin)),
                        rhs = labels(rhs(ini_fin)),
                        ini_fin@quality)
ruledf <- ini_fin_df

write.csv(ruledf, paste("proto_rule.csv", sep = ""),
          row.names = FALSE)
