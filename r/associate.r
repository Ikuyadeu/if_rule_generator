library(arules)
project <- "eclipse-collections"
project <- "openj9"
project <- "jetty.project"
project <- "development"

original <- read.csv(paste(project, "git_ori.csv", sep = "/"),
                     sep = ",",
                     header = TRUE, row.names = NULL)
df <- read.csv(paste(project, "git_merged.csv", sep = "/"))
metricses <- names(original)
m_t_or_f <- c("filename", "num", "ori", "rev")
metricses <- metricses[5:length(metricses)]

metrics_plus <- c()
metrics_minus <- c()
for (i in 1:length(metricses)){
    metrics <- metricses[i]
    metrics_plus <- append(metrics_plus, paste(metrics, "plus", sep = "_"))
    metrics_minus <- append(metrics_minus, paste(metrics, "minus", sep = "_"))
}
m_t_or_f <- append(metricses,
                   c(metrics_plus, metrics_minus))
df <- subset(df, TRUE, m_t_or_f)

# closed itemset
df <- subset(df, TRUE, m_t_or_f)
data_tran <- as(as.matrix(df[1:ncol(df)]), "transactions")

rules <- apriori(data_tran,
                 parameter = list(supp = 0.01,
                                  maxlen = 2,
                                  minlen = 1,
                                  confidence = 0.01
                                  ))

# Get ini to fin rules
rules <- subset(rules,
                lift > 1 &
                rhs %in% metrics_plus &
                lhs %in% metricses)

rules <- rules[!is.redundant(rules)]

ruledf <- data.frame(lhs = labels(lhs(rules)),
                     rhs = labels(rhs(rules)),
                     rules@quality)
ruledf <- ruledf[order(ruledf$confidence, decreasing = T), ]

write.csv(ruledf, paste(paste(project, "rules.csv", sep = "/"), sep = ""),
          row.names = FALSE)
