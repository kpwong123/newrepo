setwd("c:\\Users\\Oscar Wong\\Desktop\\")
data <- read.csv(file = "BONEDEN.csv")

#conduct paired t test: t.test(vector 1, vector 2, paired = TRUE)
print(t.test(data$fn1, data$fn2, paired = TRUE))

#calculate critical values of f test: qf(quantile, df1, df2)
print(qf(0.025, 99, 73))

#calculate p value of f test: pf(f score, df1, df2)
#note that when f statistic>1, 1-pf() is needed
print(2*(1-pf(4.23, 99, 73)))

#calculate critical value of two sample t test with unequal variances: qt(quantile, df)
print(qt(0.975, 151.4))

#calculate p value of unequal variances: pt(t score, df)
print(2*(1-pt(3.40, 151.4)))

#conduct independent samples t test: t.test(x, y, alternative = "two.sided", var.equal = TRUE/FALSE)
print(t.test(data$fn1, data$fn2, alternative = "two.sided", var.equal = TRUE))

#conduct f test: var.test(x,y)

