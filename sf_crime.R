library(readr)
library(ggplot2)
library(dplyr)

setwd('C:\\Users\\usz003g\\Documents\\R training\\Crime')

d=read_csv("sanfrancisco_incidents_summer_2014.csv",col_names=T)
d0=d
head(d)
d=d[order(d$Date),]
head(d)

tb=table(d$Category)
names(tb)
topcat=names(tb[order(tb, decreasing = TRUE)][1:7])
d=d[d$Category %in% topcat,]
d$hour=as.numeric(substr(d$Time,1,2))
d$Month=as.numeric(substr(d$Date,1,2))

d$day[d$DayOfWeek=='Monday']='1.Monday'
d$day[d$DayOfWeek=='Tuesday']='2.Tuesday'
d$day[d$DayOfWeek=='Wednesday']='3.Wednesday'
d$day[d$DayOfWeek=='Thursday']='4.Thursday'
d$day[d$DayOfWeek=='Friday']='5.Friday'
d$day[d$DayOfWeek=='Saturday']='6.Saturday'
d$day[d$DayOfWeek=='Sunday']='7.Sunday'

#by hour
mdf <- d%>%group_by(hour)%>%summarise(count=n())
ggplot(mdf, aes(x = hour, y = count)) +  geom_bar(stat = "identity", color= "blue",fill='blue')+ labs(x = "Hour", y = "Count of Incidents") + 
  scale_x_continuous(breaks=c(0:23)) + 
  ggtitle("Number of incident by hour") + 
  theme(plot.title = element_text(size = 14))

#by day
mdf <- d%>%group_by(day)%>%summarise(count=n())
ggplot(mdf, aes(x = day, y = count)) +  geom_bar(stat = "identity", color= "blue",fill='blue')+ labs(x = "Hour", y = "Count of Incidents") +
  ggtitle("Number of incident by Day") + 
  theme(plot.title = element_text(size = 14))

#by month
mdf <- d%>%group_by(Month)%>%summarise(count=n())
ggplot(mdf, aes(x = Month, y = count)) +  geom_bar(stat = "identity", color= "blue",fill='blue')+ labs(x = "Hour", y = "Count of Incidents") + 
  ggtitle("Number of incident by Month") + 
  theme(plot.title = element_text(size = 14))


#by category
mdf <- d%>%group_by(Category)%>%summarise(count=n())
ggplot(mdf, aes(x = Category, y = count)) +  geom_bar(stat = "identity", color= "blue",fill='blue')+ labs(x = "Category", y = "Count of Incidents") + 
  ggtitle("Number of incident by category") + 
  theme(plot.title = element_text(size = 14))

#by date
d$date=substr(d$Date,1,5)
mdf <- d%>%group_by(date)%>%summarise(count=n())
ggplot(mdf, aes(x = date, y = count)) +  geom_bar(stat = "identity", color= "black",fill='blue')+ labs(x = "Date", y = "Count of Incidents") + 
  ggtitle("Number of incident by date") +theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))


#crime by hour

mdf <- d%>%group_by(hour,Category)%>%summarise(count=n())
#mdf=mdf[mdf$count>1]
table(mdf$hour)
mdf
#ggplot(mdf,aes(x=factor(income),y=case))+ stat_summary(fun.y=mean,geom="bar",fill='blue')
ggplot(mdf,aes(x=factor(hour),y=count,group=factor(Category), colour=factor(Category)))+geom_line(size=1) +geom_point(size=3, fill="white") +geom_jitter(aes(color=factor(Category)))+theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

ggplot(mdf, aes(y=Category, x=factor(hour), fill=count)) + geom_tile(colour="white") + 
  scale_fill_gradientn(colours=topo.colors(10),
                       guide=guide_colourbar(ticks=T, nbin=50,
                                             barheight=10, label=T, 
                                             barwidth=1)) +theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))


#crime by dayofweek
mdf <- d%>%group_by(DayOfWeek,Category)%>%summarise(count=n())
#mdf=mdf[mdf$count>1]
factor(mdf$DayOfWeek)
mdf$day[mdf$DayOfWeek=='Monday']='1.Monday'
mdf$day[mdf$DayOfWeek=='Tuesday']='2.Tuesday'
mdf$day[mdf$DayOfWeek=='Wednesday']='3.Wednesday'
mdf$day[mdf$DayOfWeek=='Thursday']='4.Thursday'
mdf$day[mdf$DayOfWeek=='Friday']='5.Friday'
mdf$day[mdf$DayOfWeek=='Saturday']='6.Saturday'
mdf$day[mdf$DayOfWeek=='Sunday']='7.Sunday'

#ggplot(mdf,aes(x=factor(income),y=case))+ stat_summary(fun.y=mean,geom="bar",fill='blue')
ggplot(mdf,aes(x=factor(day),y=count,group=factor(Category), colour=factor(Category)))+geom_line(size=1) +geom_point(size=3, fill="white") +geom_jitter(aes(color=factor(Category)))+theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

ggplot(mdf, aes(y=Category, x=factor(day), fill=count)) + geom_tile(colour="white") + 
  scale_fill_gradientn(colours=topo.colors(10),
                       guide=guide_colourbar(ticks=T, nbin=50,
                                             barheight=10, label=T, 
                                             barwidth=1)) +theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

#PD district 

mdf <- d%>%group_by(PdDistrict,Category)%>%summarise(count=n())
#mdf=mdf[mdf$count>1]

#ggplot(mdf,aes(x=factor(income),y=case))+ stat_summary(fun.y=mean,geom="bar",fill='blue')
ggplot(mdf,aes(x=factor(PdDistrict),y=count,group=factor(Category), colour=factor(Category)))+geom_line(size=1) +geom_point(size=3, fill="white") +geom_jitter(aes(color=factor(Category)))+theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

ggplot(mdf, aes(y=Category, x=factor(PdDistrict), fill=count)) + geom_tile(colour="white") + 
  scale_fill_gradientn(colours=topo.colors(10),
                       guide=guide_colourbar(ticks=T, nbin=50,
                                             barheight=10, label=T, 
                                             barwidth=1)) +theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

#month by category

mdf <- d%>%group_by(Month,Category)%>%summarise(count=n())
#mdf=mdf[mdf$count>1]
table(mdf$Month)
#ggplot(mdf,aes(x=factor(income),y=case))+ stat_summary(fun.y=mean,geom="bar",fill='blue')
ggplot(mdf,aes(x=factor(Month),y=count,group=factor(Category), colour=factor(Category)))+geom_line(size=1) +geom_point(size=3, fill="white") +geom_jitter(aes(color=factor(Category)))+theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

ggplot(mdf, aes(y=Category, x=factor(Month), fill=count)) + geom_tile(colour="white") + 
  scale_fill_gradientn(colours=topo.colors(10),
                       guide=guide_colourbar(ticks=T, nbin=50,
                                             barheight=10, label=T, 
                                             barwidth=1)) +theme(text = element_text(size=14),axis.text.x = element_text(angle = 90, hjust = 1, size=14))

#map

library(ggmap)
d$Latitude   <- d$Y
d$Longitude  <- d$X

g <- qmplot(Longitude, Latitude, data = d, color = Category, size = I(1))
g

R.home(component = "home")
