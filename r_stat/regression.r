setwd("c:\\Users\\Oscar Wong\\Desktop\\stat_3004_eg")

# simple linear regression -- F test (p.19)
d=read.csv("ch5_obs.csv")
model=lm(birthweight~estriol, data=d)
summary(model)
anova(model)

# Prediction CI (p.27)
newdata=data.frame(estriol = c(10,15,20))
# single new observation
print(predict(model, newdata, interval = "prediction"))
# mean predicted value
print(predict(model, newdata, interval = "confidence"))

# Assessing the Goodness of Fit (p.29)
# scatter plot
plot(birthweight~estriol, data=d)
abline(model$coeff)

# studentized residuals plots (p.30)
library(MASS)
std_res=studres(model) # Studentized residual
par(mfrow=c(2,1))
plot(d$estriol,std_res, 
	xlab="estriol",ylab="residuals")
plot(model$fitted,std_res, 
	xlab="fitted value",ylab="residuals")

# studentized residuals plot in logged form (p.32)
par(mfrow=c(1,1))
plot(log(model$fitted),std_res, 
	xlab="fitted value",ylab="residuals")

# studentized residuals (p.33)
# against the order of the observations
# to check for the independence assumption
plot(std_res)

#multiple regression (p.37)
d=read.csv("ch5_sbp.csv")
model=lm(SBP~Age+BW, data=d)
summary(model)
anova(model)

# Correlation test (p.44)
# Example 3
d=read.csv("ch5_obs.csv")
cor.test(d$birthweight,d$estriol)

