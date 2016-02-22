
install.packages("caret")
install.packages("rpart")
install.packages("tree")
install.packages("randomForest")
install.packages("e1071")
install.packages("ggplot2")

local({r <- getOption("repos");         r["CRAN"] <- "http://cran.r-project.org"; options(repos=r)})

getwd()
setwd('/Users/wangfang/Documents/Work/datasci_course_materials/assignment5')

d=read.csv('seaflow_21min.csv',header=T)
names(d)

summary(d)
n=dim(d)[1]
n

idtrain=sample(1:n,n/2)
idtest=(1:n)[!(1:n %in% idtrain)]
#is.element

setdiff(idtrain,idtest)
union(idtrain,idtest)
intersect(idtrain,idtest)

Train=d[idtrain,]
dim(Train)

Test=d[idtest,]
dim(Test)

#plot the data
library(ggplot2)
ggplot(Train, aes(pe, chl_small, color=pop)) + geom_point()

library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
dtmodel <- rpart(fol, method="class", data=Train)
print(dtmodel)

plot(dtmodel)
text(dtmodel, use.n=TRUE, all=T, cex=0.8)

dtpred <- predict(dtmodel, newdata=Test, type="class")
corr_pred_dt <- dtpred == Test$pop
accuracy_dt <- sum(corr_pred) / length(corr_pred)
accuracy_dt


library(randomForest) 
rfmodel <- randomForest(fol, data=Train)
print(rfmodel)
rfpred <- predict(rfmodel, newdata=Test, type="class")
corr_pred_rf <- rfpred == Test$pop
accuracy_rf <- sum(corr_pred_rf) / length(corr_pred_rf)
accuracy_rf
importance(rfmodel)

library(e1071) 
svmmodel <- svm(fol, data=Train)
svmpred <- predict(svmmodel, newdata=Test, type="class")
corr_pred_svm <- svmpred == Test$pop
accuracy_svm <- sum(corr_pred_svm) / length(corr_pred_svm)
accuracy_svm
accuracy_svm0=accuracy_svm

predictions=cbind(dtpred,rfpred,svmpred)
dim(predictions)
table(pred=predictions[,1], true = Test$pop)
table(pred=predictions[,2], true = Test$pop)
table(pred=predictions[,3], true = Test$pop)

#fsc_small, fsc_perp, fsc_big, pe, chl_small, chl_big
p13 <- ggplot(d, aes(x = time , y = fsc_big ) )
p13 + geom_jitter(aes(color=pop))

p131 <- ggplot(d, aes(x = time , y = fsc_small ) )
p131 + geom_jitter(aes(color=pop))

p132 <- ggplot(d, aes(x = time , y = fsc_perp ) )
p132 + geom_jitter(aes(color=pop))

p133 <- ggplot(d, aes(x = time , y = pe ) )
p133 + geom_jitter(aes(color=pop))

p134 <- ggplot(d, aes(x = time , y = chl_small ) )
p134 + geom_jitter(aes(color=pop))

p135 <- ggplot(d, aes(x = time , y = chl_big ) )
p135 + geom_jitter(aes(color=pop))



names(d)
dnew=d[d$file_id!=208,]
n=dim(dnew)[1]
n
idtrain=sample(1:n,n/2)
idtest=(1:n)[!(1:n %in% idtrain)]
#is.element

Train=dnew[idtrain,]
dim(Train)

Test=dnew[idtest,]
dim(Test)

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
svmmodel <- svm(fol, data=Train)
svmpred <- predict(svmmodel, newdata=Test, type="class")
corr_pred_svm <- svmpred == Test$pop
accuracy_svm <- sum(corr_pred_svm) / length(corr_pred_svm)
accuracy_svm

accuracy_svm-accuracy_svm0





