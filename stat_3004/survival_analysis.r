# Chapter 8

# Kaplan-Meier Estimator
# Example 6
# input data
k=6
t=1:k
d=c(3,6,15,21,15,5)
l=c(4,0,1,26,35,41)
s0=172
alpha=0.05

x=data.frame(
	"t"=c(0,t),
	"d"=c(NA,d),
	"l"=c(NA,l),
	"s"=c(s0,numeric(k)),
	"lambda"=numeric(k+1),
	"S"=c(1,numeric(k)),
	"var_lnlnS"=numeric(k+1),
	"c1"=numeric(k+1),
	"c2"=numeric(k+1),
	"CI_L"=c(1,numeric(k)),
	"CI_U"=c(1,numeric(k))
)

for (i in 2:(k+1)) {
	x$s[i]=x$s[i-1]-x$d[i]-x$l[i]
	x$lambda[i]=x$d[i]/x$s[i-1]
	x$S[i]=x$S[i-1]*(1-x$lambda[i])
	var_lnS=0
	for (j in 2:i) {
		var_lnS=var_lnS+x$d[j]/x$s[j-1]/(x$s[j-1]-x$d[j])
	}
	x$var_lnlnS[i]=1/(log(x$S[i]))^2*var_lnS
	x$c1[i]=log(-log(x$S[i]))-qnorm(1-alpha/2)*sqrt(x$var_lnlnS[i])
	x$c2[i]=log(-log(x$S[i]))+qnorm(1-alpha/2)*sqrt(x$var_lnlnS[i])
	x$CI_L[i]=exp(-exp(x$c2[i]))
	x$CI_U[i]=exp(-exp(x$c1[i]))
}
	
plot(S~t, data=x, type="l", ylim=c(0,1))
lines(CI_U~t, data=x, type="l", lty=2)
lines(CI_L~t, data=x, type="l", lty=2)
	
	
# Log-Rank Test
# input data for the second group
d=c(8,13,21,21,13,13)
l=c(0,3,2,28,31,29)
s0=182

y=data.frame(
	"t"=c(0,t),
	"d"=c(NA,d),
	"l"=c(NA,l),
	"s"=c(s0,numeric(k))
)

for (i in 2:(k+1)) {
	y$s[i]=y$s[i-1]-y$d[i]-y$l[i]
}

table = array(
	0,
	dim = c(2,2,6), 
	dimnames = list(
		Vitamin_A = c("15,000", "75"),
		Fail = c("yes", "no"),
		Year = as.character(1:6)
	)
)

for (i in 1:6) {
	table[1,1,i]=x$d[i+1]
	table[1,2,i]=x$s[i]-x$d[i+1]
	table[2,1,i]=y$d[i+1]
	table[2,2,i]=y$s[i]-y$d[i+1]
}
	
mantelhaen.test(table)
	
	
# Weibull Survival Model
# Example 7
d=read.csv("ch8_cancer.csv")
ln_S=function(t, lambda, gamma) {
	-(lambda*t)^gamma
}
ln_f=function(t, lambda, gamma) {
	log(lambda*gamma*(lambda*t)^(gamma-1))-(lambda*t)^gamma
}
l=function(p, d) {
	l=0
	lambda=p[1]
	gamma=p[2]
	for (i in 1:nrow(d)) {
		if (d$censored[i]==1) {
			l=l+ln_S(d$t[i], lambda, gamma)
		} else {
			l=l+ln_f(d$t[i], lambda, gamma)
		}
	}
	return(-l)
}
p=c(1,1)
out=optim(p,l,d=d)
	
t=0:180
S=exp(-(out$par[1]*t)^out$par[2])
plot(t, S, type="l")

# Goodness of fit
d0=d[d$censored==0,]
n=nrow(d)
m=nrow(d0)
x=data.frame(
	t=c(0,d0$t),
	s=c(n,rep(0,m)),
	d=c(NA,rep(0,m)),
	l=c(NA,rep(0,m)),
	S=c(1,rep(0,m))
)
i=1
j=2
while (j<=(m+1)) {
	if (d$censored[i]==1)
		x$l[j]=x$l[j]+1
	else {
		x$d[j]=x$d[j]+1
		x$s[j]=x$s[j-1]-x$d[j]-x$l[j]
		x$S[j]=x$S[j-1]*(1-x$d[j]/x$s[j-1])
		j=j+1
	}
	i=i+1
}
plot(log(x$t[-1]),log(-log(x$S[-1])),
	xlab="ln(t)",ylab="ln(-ln(S(t)))")
abline(lsfit(log(x$t[-1]),log(-log(x$S[-1]))))
		