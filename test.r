setwd("c:\\Users\\Oscar Wong\\Desktop\\")
df = read.csv("LEAD.csv")
print(kruskal.test(maxfwt~lead_grp, data = df))

library(dunn.test)
print(dunn.test(df$maxfwt, df$lead_grp, method = "bonferroni"))