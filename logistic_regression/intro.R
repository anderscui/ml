# R version 3.1.1 (2014-07-10)

# see original: http://statistics.ats.ucla.edu/stat/r/dae/logit.htm

#install.packages("aod")
library(aod)
library(ggplot2)

# download data
url <- "http://www.ats.ucla.edu/stat/data/binary.csv"
file <- "binary.csv"
download.file(url, file)

# read file
mydata <- read.csv(file)
head(mydata)

# this data set has a binary response admit (0 or 1) and three predictor vars: 
#   gre, gpa and rank.

summary(mydata)

# check sd
sapply(mydata, sd)

# two-way cnotingency table
xtabs(~admit+rank, data = mydata)

## possible methods
# logistic regression
# probit regression
# OLS regression
# two-group discriminant function analysis
# Hotelling's T2
mydata$rank <- factor(mydata$rank)
mylogit <- glm(admit ~ gre + gpa + rank, data = mydata, family = "binomial")

# confidence intervals (log-likelihood)
confint(mylogit)

# confidence intervals (stardard errors)
confint.default(mylogit)

# test the overall effect of *rank* var.
wald.test(b = coef(mylogit), Sigma = vcov(mylogit), Terms = 4:6)

# compare rank2 and rank3
l <- cbind(0, 0, 0, 1, -1, 0)
wald.test(b = coef(mylogit), Sigma = vcov(mylogit), L = l)

# odds ratios only
exp(coef(mylogit))
# odds ratios and 95% CI
exp(cbind(OR = coef(mylogit), confint(mylogit)))

newdata1 <- with(mydata, data.frame(gre = mean(gre), gpa = mean(gpa), rank = factor(1:4)))
## view data frame
newdata1