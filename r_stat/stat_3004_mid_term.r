#Question 4(c)
time1 <- c(62, 35, 38, 80, 48, 48, 68, 26, 48, 27, 43, 67, 52, 88)
time2 <- c(46, 42, 40, 42, 36, 46, 45, 40, 42, 40, 46, 31, 44, 48)

print(wilcox.test(time1, time2, mu = 0, paired = TRUE, exact = FALSE))