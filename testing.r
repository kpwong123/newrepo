setwd("c:\\Users\\Oscar Wong\\Desktop\\")

data <- read.csv(file = "imt.csv")

bmi <- data$weight/((data$height/100)^2)

measure1 <- data$measure[data$GENDER == 1]

print(head(data))

print(t.test(measure1, mu = 0.58, alternative = "greater"))

print(t.test(data$measure, conf.level = 0.9))

print(t.test(data$measure[data$GENDER == 2 & data$SPORT == 1], data$measure[data$GENDER == 2 & data$SPORT == 0], alternative = "two.sided", var.equal = TRUE))

