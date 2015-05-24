
# original article: http://www.ats.ucla.edu/stat/r/dae/logit.htm

# install.packages("aod")

library(aod)
library(ggplot2)

mydata <- read.csv("http://www.ats.ucla.edu/stat/data/binary.csv")
head(mydata)
summary(mydata)

sapply(mydata, sd)

xtabs(~admit + rank, data = mydata)

# use the logistic regression model
mydata$rank <- factor(mydata$rank)
mylogit <- glm(admit ~ gre + gpa + rank, data = mydata, family = "binomial")

summary(mylogit)

# CIs using profiled log-likelihood
confint(mylogit)

# CIs using standard errors
confint.default(mylogit)

# test overall effect of rank
wald.test(b = coef(mylogit), Sigma = vcov(mylogit), Terms = 4:6)

# test rank2 vs. rank3
l <- cbind(0, 0, 0, 1, -1, 0)
wald.test(b = coef(mylogit), Sigma = vcov(mylogit), L = l)


# exponentiated coefficients

# odds ratios only
exp(coef(mylogit))

## odds ratios and 95% CI
exp(cbind(OR = coef(mylogit), confint(mylogit)))

## predict
newdata1 <- with(mydata, data.frame(gre = mean(gre), gpa = mean(gpa), rank = factor(1:4)))
newdata1

newdata1$rankP <- predict(mylogit, newdata = newdata1, type = "response")
newdata1

# more new data
newdata2 <- with(mydata, 
                 data.frame(gre = rep(seq(from = 200, to = 800, length.out = 100), 4), 
                                    gpa = mean(gpa), 
                                    rank = factor(rep(1:4, each = 100))))
newdata2

newdata3 <- cbind(newdata2, predict(mylogit, newdata = newdata2, type = "link",
                                    se = TRUE))
newdata3 <- within(newdata3, {
  PredictedProb <- plogis(fit)
  LL <- plogis(fit - (1.96 * se.fit))
  UL <- plogis(fit + (1.96 * se.fit))
})

head(newdata3)

ggplot(newdata3, aes(x = gre, y = PredictedProb)) + 
  geom_ribbon(aes(ymin = LL, ymax = UL, fill = rank), alpha = 0.2) + 
  geom_line(aes(colour = rank), size = 1)
