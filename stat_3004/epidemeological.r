# Chapter 7

# Mantel-Haenszel Test 
# Example 5
table = array(
	c(120,80,111,155,161,130,117,124),
	dim = c(2,2,2), 
	dimnames = list(
		cancer = c("yes", "no"),
		passive.smoker = c("yes", "no"), 
		active.smoker = c("no", "yes")
	)
)

mantelhaen.test(table)


# Logistic regression
# Example 1
# x=1 if Age at first birth >= 30
# x=0 if Age at first birth < 30
x=c(rep(1,683),rep(0,2537),rep(1,1498),rep(0,8747))
# y=1 for cancer group
# y=0 for non-cancer group
y=c(rep(1,683+2537),rep(0,1498+8747))
d=data.frame(cbind(x,y))
model = glm(y~x, data=d ,family=binomial)
summary(model)
est=as.numeric(model$coeff)
OR=exp(est[2])
pE=exp(sum(est))/(1+exp(sum(est)))
pU=exp(est[1])/(1+exp(est[1]))


# Missing data
# Example 8
d=read.csv("ch7_missing.csv")
d1=d[!is.na(d$x3),] # complete case
d2=d[is.na(d$x3),] # incomplete case
d2_copy=d2
n2=nrow(d2) # number of incomplete case
fit1=lm(x3~x1+x2+y, data=d1)
s=sigma(fit1) # residual standard deviation
m=100 # imputation trial
beta=matrix(0,nr=m,nc=4)
var_beta=matrix(0,nr=m,nc=4)
for (q in 1:m) {
	d2_copy$x3=predict(fit1, d2)+rnorm(n2,0,s)
	fit2=glm(
		y~x1+x2+x3, 
		data=rbind(d1,d2_copy),
		family=binomial
	)
	beta[q,]=fit2$coeff
	var_beta[q,]=diag(summary(fit2)$cov.unscaled)
}
# To test H0: beta_j=0
j=4
beta_j=mean(beta[,j])
var_beta_j=mean(var_beta[,j])+(m+1)/m*var(beta[,j])
t=beta_j/sqrt(var_beta_j)
df=(m-1)*(1+1/(1+var(beta[,j])*(m+1)/m/sum(var_beta[,j])))^2
p=2*(1-pt(abs(t),df))

# Consider only complete cases
summary(glm(y~x1+x2+x3, data=d1,family=binomial))
	