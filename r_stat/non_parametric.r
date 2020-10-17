setwd("c:\\Users\\Oscar Wong\\Desktop\\")
data <- read.csv("ch3_oph.csv")

#conduct sign test(which is a special case of one sample biniomial test with p = .5):
#prop.test(positive (or negative) trials, total trials, alternative = "two-sided", correct = TRUE)
print(prop.test(18, 40, 0.5, alternative = "two.sided", correct = TRUE))

#conduct simultaneous sign test and wilcoxon signed rank test:
dose.lab1 <- c(22, 18, 28, 26, 13, 8, 21, 26, 27, 29, 25, 24, 22,
28, 15)
dose.lab2 <- c(25, 21, 31, 27, 11, 10, 25, 26, 29, 28, 26, 23, 22,
25, 17)
# sign test
dif <- (dose.lab1-dose.lab2)
nminus <- sum(dif<0)
nplus <- sum(dif>0)
binom.test(min(nplus,nminus),nplus+nminus)
# Wilcoxon
wilcox.test(dose.lab1, dose.lab2, paired = TRUE, exact = FALSE)

#conduct wilcoxon signed rank test:
#note that if exact = TRUE, no ties are allowed
#FOR ALL WILCOX.TEXT, PUT THE GROUP WITH SMALLER SAMPLE SIZE IN THE FRONT
# wilcox.test(
#     vector 1,
#     vector 2 (if paired)/ y = NULL (if not paired),
#     mu = 0,
#     paired = TRUE (if paired)/FALSE (if not paired),
#     exact = NULL,
#     correct = TRUE,
#     conf.int = FALSE
# )

d = rep(-10:10, c(0,0,1,3,2,2,1,5,4,4,5,10,6,2,0,0,0,0,0,0,0))
result <- wilcox.test(
    d,
    y = NULL,
    mu = 0,
    paired = FALSE,
    exact = NULL,
    correct = TRUE,
    conf.int = FALSE
)
print(result)

#conduct wilcoxon rank sum test:
# wilcox.test(
#     vector 1 ~ group 1,
#     vector 2 ~ selected rows (if 2 vectors)
#     alternative = "two.sided",
#     mu = 0,
#     paired = FALSE,
#     exact = NULL,
#     correct = TRUE,
#     conf.int = FALSE
# )

result <- wilcox.test(
    data$VA ~ data$g,
    alternative = "two.sided",
    mu = 0,
    paired = FALSE,
    exact = NULL,
    correct = TRUE,
    conf.int = FALSE
)

print(result)

#conduct permutation test:
#1. construct data frame
x=c(7.5,12.6,3.8,20.2,6.8,403.3,2.9,7.2,10.5,205.4)
y=c(8.2,13.3,102.0,12.7,6.3,4.8,19.5,8.3,407.1,10.2)
n1=length(x)
n2=length(y)
gp=rep(1:2,c(n1,n2)) # group label
z=c(x,y)
d=as.data.frame(cbind(gp,z))

#2. conduct test
r=rank(d$z)
R1=sum(r[d$gp==1])
perm=combn(1:(n1+n2),n1) # index of permutation sample
# E.g., the first permutation sample is d$z[perm[,1]]
M=ncol(perm)	# number of permutation sample
R1_perm=numeric(M)
for (i in 1:M) {	
	# compute R1 for each permutation sample
	R1_perm[i]=sum(r[perm[,i]])
}
R1_le=R1_perm[R1_perm<=R1]	# R1_perm<=R1_obs
R1_ge=R1_perm[R1_perm>=R1]	# R1_perm>=R1_obs
p=2*min(length(R1_le)/M,length(R1_ge)/M,0.5)

# compare with the built in function
wilcox.test(x,y)


#3. Simulation based approach
set.seed(3004)
r=rank(d$z)
R1=sum(r[d$gp==1])
M=1000	# number of simulation trial
R1_perm=numeric(M)
for (i in 1:M) {	
	# compute R1 for each random sample
	R1_perm[i]=sum(r[sample(1:(n1+n2),n1)])
}
R1_le=R1_perm[R1_perm<=R1]	# R1_perm<=R1_obs
R1_ge=R1_perm[R1_perm>=R1]	# R1_perm>=R1_obs
p=2*min(length(R1_le)/M,length(R1_ge)/M,0.5)