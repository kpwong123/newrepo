#conduct Yates-Corrected Chi-Square Test:
table=matrix(c(683,1498,2537,8747),nrow = 2)
print(chisq.test(table))

# sometimes the factorial is too large to calculate e.g.
factorial(300)
#thus, we calculate probability of the occurrence of a particular table by:
exp(
	lgamma(2182)+lgamma(11285)+lgamma(3221)+
	lgamma(10246)-lgamma(13466)-lgamma(684)-
	lgamma(2538)-lgamma(1499)-lgamma(8748)
)
#or, for small samples sizes:
dhyper(2, m=5, n=6, k=7)
# where m = m_1,
# n = m_2, and
# k = n_1

# calculate p-value for two-sided Fisher's Exact Test
# Example 3
table=matrix(c(2,5,23,30),nrow = 2)
p_lower=fisher.test(table,alternative = "less")$p.value
p_upper=fisher.test(table,alternative = "greater")$p.value
p=2*min(p_lower,p_upper,0.5)
print(p)
#conduct two-sided Fisher's Exact Test
print(fisher.test(table))
#the p value is different because the latter uses a different and more precise definition of p value.

#conduct Mc Nemar's Test
Performance <- 
matrix(c(794, 86, 150, 570),
nrow = 2,
dimnames = list("1st Survey" = c("Approve", "Disapprove"), "2nd Survey" = c("Approve", "Disapprove")))
Performance
print(mcnemar.test(Performance))

#conduct chi-square test:
table=matrix(c(
				320,1422,
				1206,4432,
				1011,2893,
				463,1092,
				220,406
				),
			nrow = 2
			)
test=chisq.test(table)
print(test)
#print expected RxC contingency table
print(test$expected)

# conduct Chi-Square Goodness-of-Fit Test
# Example 8
O=c(57, 330, 2132, 4584, 4604, 2119, 659, 251) #number of observation in an interval
mu=80.68 #population mean of the hypothetical normal distribution
s=12 #population standard deviation of the hypothetical normal distribution
k=2 # two parameters are estimated
n=sum(O)
a=c(-Inf,seq(50,110,by=10),Inf) #seq(higher class boundary of the lowest class, lower class boundary of the highest class, class interval)
g=length(a)-1
E=numeric(g)
for (i in 1:g) {
	E[i]=n*(pnorm((a[i+1]-mu)/s)-pnorm((a[i]-mu)/s)) #expected frequency of a class of this normal distribution
}
X2=sum((O-E)^2/E)
p=1-pchisq(X2,g-k-1)
print(p)
