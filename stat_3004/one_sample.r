# setwd("c:\\Users\\Oscar Wong\\Desktop\\")

data <- read.csv(file = "BONEDEN.csv")

#conduct one sample t test: t.test(vector, hypothesized population mean, alternative(two.sided, greater, less), confidence level = (1- alpha))
print(t.test(data$fn1, mu = 45, alternative = "greater", conf.level = 0.97))

#calculate p value of students t test: pt(t score, df)
#two sided p value: 2*(t score, df)
print(pt(-2.12, 95))
print(2*(1-pt(2.12, 20)))

#calculate p value of z test: pnorm(z score)
print(2*(1-pnorm(3)))

#calculate critical values of chisquare test: qchisq(quantile, df)
print(qchisq(0.025, 9))

#calculate p value of chisquare test: pchisq(chisq score, df)
print(2*pchisq(2.103, 9))

#conduct one sample binomial proportion test: 
# prop.test(no. of successful trials, total trials, null proportion,
#     alternative = "two.sided", "less", "greater",
#     correct = TRUE, FALSE
# )
result <- prop.test(10, 40, 0.2,
    alternative = "two.sided",
    correct = TRUE
)
print(result)

#calculate p value of one sample binomial proportion exact test: pbinom(successful, total trials, null proportion)
#pbinom calculates the probability of events = Pr(x <= successful)
print(2*(1-pbinom(4, 13, 0.2)))

#calculatr p value of one sample poisson approximation test: ppois(obs. no. of occurrence, null occurrence)
#ppois calculates the probability of events = Pr(x <= occurrence)
print(2*(1-ppois(3, 3.3)))