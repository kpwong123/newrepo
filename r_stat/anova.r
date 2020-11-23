setwd("c:\\Users\\Oscar Wong\\Desktop\\stat_3004_eg")

# one-way ANOVA (p.15)
# Example 2
d=read.csv("ch6_swiss.csv")
d$group=factor(d$group)
model=aov(creat_68 ~ group, data=d)
anova(model)

# plotting one-way ANOVA data by group (p.17)
mean(d$creat_68, na.rm = TRUE)
# Overall mean
print(tapply(d$creat_68, d$group, mean, na.rm = TRUE))
# Group mean
print(tapply(d$creat_68, d$group, sd, na.rm = TRUE))
# Group SD
plot(d$group, d$creat_68, xlab="Group", ylab="Creat_68")
# Plot by group

# Multiple comparisons (for both uncorrectd value and bonferroni method) (p.36)
library(lsmeans)
lsm = lsmeans(model, ~group) 

# Test for some specific contrast (uncorrected)
print(summary(
	contrast(
		lsm, 
		list(
			c1=c(1, -1,0),
			c2=c(0,1,-1)
		)
	),
	infer=c(T,T), 
	level=0.95, 
	side="two-sided"
))

# Individual 90% CI	 of group mean
confint(lsm, level=0.90) 

# Bonferroni's method (p.37)
print(summary(
	contrast(
		lsm, 
		method="pairwise", 
		adjust="bonferroni"
	),
	infer=c(T,T), 
	level=0.99, 
	side="two-sided"
))

# Scheffe's method	(p.42)
print(summary(
	contrast(
		lsm, 
		method="pairwise", 
		adjust="scheffe"
	),
	infer=c(T,T), 
	level=0.99, 
	side="two-sided"
))

# two-way ANOVA all fixed
#  effects/interaction effect F-tests (p.52)
d$age_grp=cut(
	d$age,
	breaks=c(29.5,35,40,45,50),
	# cutting points for age groups
	labels=c("1","2","3","4")
)
table(d$group, d$age_grp)
model2=aov(creat_68 ~ group+age_grp+group:age_grp, data=d)
print(anova(model2))

# Kruskal-Wallis Test (P.60)
# Example 3
d=read.csv("ch6_opt.csv")
print(kruskal.test(score~group, data=d))

# nonparametric comparison of specific groups
library(dunn.test)
dunn.test(d$score, d$group, method = "bonferroni")

