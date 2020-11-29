
# Install packages
install.packages("ggplot2")  
install.packages("devtools")
install.packages("ggpubr")
install.packages('viridis')
install.packages('hrbrthemes')

library(dplyr)
library(tidyr)
library(scales)
library(devtools)
library(ggpubr)
library(ggplot2)                      
library(cowplot)
library(viridis)
library(hrbrthemes)

# Load database
dataset <- read.csv('raw-responses.csv', header = TRUE)

head(dataset)
class(dataset)

data1 = dataset[,c(80,95,84)]
data1
# age3 = age range
# q0024 = civil status
# q0026 = sexual orientation
class(data1)
colnames(data1) <- c('CivilSts','AgeRage','SexOrient')


# Pie Chart Total Respondents
nrLines <- length(data1$AgeRage)
mycol <- "#0073C2FF"

count.data <- data.frame(
  class = 'Respondents',
  n = nrLines
)


pie2 <- ggplot(count.data, aes(x='', y=n, fill=class)) + 
  geom_bar(stat='identity', width = 1) +
  coord_polar('y',start=0) +
  geom_text(aes(label=n), color='white', size=12, position = position_stack(vjust = 0.5)) +
  scale_fill_manual(values=c("#55DDE0", "#33658A", "#2F4858", "#F6AE2D",  "#999999")) +
  labs(x = NULL, y = NULL, fill = NULL,title='Total Respondents') + 
  #ggtitle('Total Number of \n Respondents') +
  theme_classic() + theme(axis.line = element_blank(),
                          axis.text = element_blank(),
                          axis.ticks = element_blank(),
                          legend.position = 'none',
                          plot.title = element_text(hjust = 0.5, color = "#666666"))
card1 <- pie2
card1


# Bar chart 
require(dplyr)
agect <- dataset %>% count(age3)
agect <- agect[order(agect$n),]
colnames(agect) <- c("group", "nro")

card2 <- ggplot(agect, aes(x=group, y=nro)) + 
  geom_bar(stat = "identity") + coord_flip() +
  labs(x = NULL, y = NULL, fill = NULL,title='Total Respondents by \n Age Group') +
  theme(legend.position="none") +
  theme_classic() + theme(axis.title.y = element_blank(),
                          axis.title.x = element_blank())
card2

# Bar chart Sex Orientation

# require(dplyr)
# sex_or <- dataset %>% count(q0026)
# sex_or <- sex_or[order(sex_or$n),]
# colnames(sex_or) <- c("group", "nro")
# 
# 
# pie <- ggplot(sex_or, aes(x='', y=nro, fill=group)) + geom_bar(stat='identity', width = 1) + 
#   coord_polar('y',start=0) + geom_text(aes(label=group), position = position_stack(vjust = 0.5)) + 
#   scale_fill_manual(values=c("#55DDE0", "#33658A", "#2F4858", "#F6AE2D",  "#999999")) + 
#   labs(x = NULL, y = NULL, fill = NULL, title='Total Respondents by \n Sexual Orientation')  + 
#   theme_classic() + theme(axis.line = element_blank(),
#                                     axis.text = element_blank(),
#                                     axis.ticks = element_blank(),
#                                     legend.position = 'none',
#                                     plot.title = element_text(hjust = 0.5, color = "#666666"))
# card3 <- pie
# card3

require(dplyr)
sex_or <- dataset %>% count(q0026)
sex_or <- sex_or[order(sex_or$n),]
colnames(sex_or) <- c("group", "nro")

sex_or <- sex_or %>% 
  mutate(tot = round(100 * (nro / nrLines)),2)
colnames(sex_or) <- c("group", 'nro', 'perc',  'pos')

card3 <- ggplot(sex_or, aes(fill=group, y=perc, x=2, label=perc)) + 
  #geom_col() + coord_flip() +
  geom_bar(stat = "identity", width = 1) + 
  labs(x = NULL, y = NULL, fill = NULL, title='Total Respondents by \n Sexual Orientation?') +
  theme(legend.position="none") +
  theme_classic() + 
  #geom_text(aes(x=pos, y=perc_adj,label = prettyNum(perc_adj,big.mark = ",")), vjust = 0,  size = 12) +
  geom_text(size = 4, position = position_stack(vjust = 0.5)) +
  theme(axis.title.y = element_blank(), axis.title.x = element_blank(), axis.text.x=element_blank())
card3


# Line chart Civil Status
require(dplyr)
civ_st <- dataset %>% count(q0024)
civ_st <- civ_st[order(civ_st$n),]
colnames(civ_st) <- c("group", "nro")



card4<- ggplot(data=civ_st, aes(x=group, y=nro,group=1)) +
  geom_line(color="#aa0022", size=1.75) +
  geom_point(color="#aa0022", size=3.5) +
  labs(x = NULL, y = NULL, fill = NULL, title='Total Respondents by \n Civil Status')  + 
  theme(axis.title.y = element_blank(),
        axis.title.x = element_blank())
card4


# Ploting multpile charts
plot_grid(card1,card2, card3, card4)

# Plot 1 - In general, how masculine or “manly” do you feel?
require(dplyr)
q0001_bar <- dataset %>% count(q0001)
q0001_bar <- q0001_bar[order(q0001_bar$n),]
colnames(q0001_bar) <- c("group", "nro")

dfTab <- q0001_bar
dfTab$lab <- as.character(round(100 * dfTab$nro / sum(dfTab$nro)),2)

plot1 <- ggplot(dfTab, aes(x=group, y=lab)) + 
  geom_bar(stat = "identity") + 
  coord_flip() +
  geom_text(aes( label = lab,   y= ..prop.. ), stat= "count", vjust = 1) +
  labs(x = NULL, y = NULL, fill = NULL, title='In general, how masculine or “manly” do you feel?') +
  theme(legend.position="none") +
  theme_classic() + 
  theme(axis.title.y = element_blank(), axis.title.x = element_blank(), axis.text.x=element_blank()) 
plot1



# Plot 2 - How masculine do you feel? by Age group
require(dplyr)
q0001_by_age <- dataset %>% count(q0001,age3)
q0001_by_age <- q0001_by_age[order(q0001_by_age$age),]
colnames(q0001_by_age) <- c("group", "age", 'nro')

plot2 <- ggplot(q0001_by_age, aes(x=group, y=nro, label=nro)) + 
  geom_bar(aes(fill = age), position = "dodge", stat="identity") +
  labs(x = NULL, y = NULL, fill = NULL, title='How masculine do you feel? by Age group') +
  theme(legend.position="none") +
  geom_text(position = position_dodge2(width = 0.9, preserve = "single"), angle = 90, vjust=0.25, hjust=0.5) +
  theme_classic() + 
  theme(axis.title.y = element_blank(), axis.title.x = element_blank()) 
plot2



# Plot 3 How masculine do you feel? by Civil status
require(dplyr)
q0001_by_cst <- dataset %>% count(q0001,q0024)
q0001_by_cst <- q0001_by_cst[order(q0001_by_cst$q0024),]
colnames(q0001_by_cst) <- c("group", "civilsts", 'nro')

plot3 <- ggplot(q0001_by_cst, aes(x=group, y=nro, label=nro)) + 
  geom_bar(aes(fill = civilsts), position = "dodge", stat="identity") +
  #geom_text(aes(label = nro,   y= ..prop.. ), stat= "count", vjust = 1) +
  labs(x = NULL, y = NULL, fill = NULL, title='How masculine do you feel? by Civil Status') +
  theme(legend.position="none") +
  geom_text(position = position_dodge2(width = 0.9, preserve = "single"), angle = 90, vjust=0.25, hjust=0.5) +
  theme_classic() + 
  theme(axis.title.y = element_blank(), axis.title.x = element_blank()) 
plot3


# Plot 4 - Q0005 Do you think that society puts pressure on men in a way that is unhealthy or bad for them?
require(dplyr)
q0005_bar <- dataset %>% count(q0005)
q0005_bar <- q0005_bar[order(q0005_bar$n),]
colnames(q0005_bar) <- c("group", 'nro')

q0005_bar <- q0005_bar %>% 
  mutate(tot = round(100 * (nro / nrLines)),2)
colnames(q0005_bar) <- c("group", 'nro', 'perc',  'pos')

plot4 <- ggplot(q0005_bar, aes(fill=group, y=perc, x=2, label='')) + 
         #geom_col() + coord_flip() +
         geom_bar(stat = "identity", width = 1) + coord_flip() +
         labs(x = NULL, y = NULL, fill = NULL, title='Do you think that society puts pressure on men \n in a way that is unhealthy or bad for them?') +
         theme(legend.position="none") +
         theme_classic() + 
         #geom_text(aes(x=pos, y=perc_adj,label = prettyNum(perc_adj,big.mark = ",")), vjust = 0,  size = 12) +
          geom_text(size = 5, position = position_stack(vjust = 0.5)) +
         theme(axis.title.y = element_blank(), axis.title.x = element_blank(), axis.text.y=element_blank())
plot4



# Plot 4.1 - q0005 vs age3 Do you think that society puts pressure on men in a way that is unhealthy or bad for them? by Age group
require(dplyr)
q0005_by_age <- dataset [ dataset$q0005 != 'No answer', ]
q0005_by_age <- q0005_by_age %>% count(q0005,age3)
q0005_by_age <- q0005_by_age[order(q0005_by_age$age3),]
colnames(q0005_by_age) <- c("group", "age", 'nro')
total = sum(q0005_by_age[, 'nro'])
q0005_by_age <- q0005_by_age %>% 
  mutate(tot = 100 * round((nro / total),2))


plot4_1 <- ggplot((q0005_by_age), aes(fill=group, y=tot, x=age,label='')) + 
  geom_bar(stat = "identity", width = 0.9) + coord_flip() +
  labs(x = NULL, y = NULL, fill = NULL, title='Do you think that society puts pressure on men \n in a way that is unhealthy or bad for them? \n by Age group') +
  theme(legend.position="none") +
  geom_text(size = 5, position = position_stack(vjust = 0.5),data=subset(q0005_by_age, tot>0)) +
  theme_classic() + 
  theme(axis.title.y = element_blank(), axis.title.x = element_blank()) 
plot4_1



# Plot 5 - q0017 Do you typically feel as though you’re expected \n to make the first move in romantic relationships?
require(dplyr)
q0017_bar <- dataset %>% count(q0017)
q0017_bar <- q0017_bar[order(q0017_bar$n),]
colnames(q0017_bar) <- c("group", 'nro')
q0017_bar <- q0017_bar %>% 
  mutate(tot = 100 * round((nro / nrLines),2))


plot5 <- ggplot((q0017_bar), aes(fill=group, y=tot, x=2,label='')) + 
  geom_bar(stat = "identity", width = 0.9) + coord_flip() +
  labs(x = NULL, y = NULL, fill = NULL, title='Do you typically feel as though you’re expected \n to make the first move in romantic relationships?') +
  theme(legend.position="none") +
  geom_text(size = 5, position = position_stack(vjust = 0.5),data=subset(q0017_bar, tot>0)) +
  theme_classic() + 
  theme(axis.title.y = element_blank(), axis.title.x = element_blank(), axis.text.y=element_blank()) 
plot5


# Plot 5.1 - q0017 vs age3 Do you typically feel as though you’re expected \n to make the first move in romantic relationships? \n by Age group
require(dplyr)
q0017_by_age <- dataset %>% count(q0017,age3)
q0017_by_age <- q0017_by_age[order(q0017_by_age$age3),]
colnames(q0017_by_age) <- c("group", "age", 'nro')
q0017_by_age <- q0017_by_age %>% 
  mutate(tot = 100 * round((nro / nrLines),2))


plot5_1 <- ggplot((q0017_by_age), aes(fill=group, y=tot, x=age,label='')) + 
  geom_bar(stat = "identity", width = 0.9) + coord_flip() +
  labs(x = NULL, y = NULL, fill = NULL, title='Do you typically feel as though you’re expected to make the first move in romantic relationships? \n by Age group') +
  theme(legend.position="none") +
  geom_text(size = 5, position = position_stack(vjust = 0.5),data=subset(q0005_by_age, tot>0)) +
  theme_classic() + 
  theme(axis.title.y = element_blank(), axis.title.x = element_blank()) 
plot5_1


# Plot 6 How often do you try to be the one who pays when on a date?
require(dplyr)
q0018_by_age <- dataset %>% count(q0018,age3,q0024)
colnames(q0018_by_age) <- c("group", "age", 'civilst', 'nro')

caz <- subset(q0018_by_age, age == '18 - 34')

plot6<-ggplot(caz) +
  geom_bar(aes(x = group, y = nro, fill = civilst ), stat = "identity", position = "dodge") +
  labs(x = NULL, y = NULL, fill = NULL, title='Age group = 18 - 34') +
  theme_minimal() +
  theme(axis.title.y = element_blank(), axis.title.x = element_blank(),axis.text.y=element_blank())

plot6

caz1 <- subset(q0018_by_age, age == '35 - 64')

plot61<-ggplot(caz1) +
  geom_bar(aes(x = group, y = nro, fill = civilst ), stat = "identity", position = "dodge") +
  labs(x = NULL, y = NULL, fill = NULL, title='Age group = 35 - 64') +
  theme_minimal() +
  theme(axis.title.y = element_blank(), axis.title.x = element_blank(),axis.text.y=element_blank()) 

plot61


caz2 <- subset(q0018_by_age, age == '65 and up')

plot62<-ggplot(caz2) +
  geom_bar(aes(x = group, y = nro, fill = civilst ), stat = "identity", position = "dodge") +
  labs(x = NULL, y = NULL, fill = NULL, title='Age group = 35 - 64') +
  theme_minimal() +
  theme(axis.title.y = element_blank(), axis.title.x = element_blank(),axis.text.y=element_blank()) 

plot62

# plot 6 multi graph
plot_grid(plot6,plot61, plot62)


# Plot 7
############################
data7 = dataset[,c(5,95)]
data7 <- data7 [ data7$q0002 != 'No answer', ]
# q0002 = How important is it to you that others see you as masculine?
# age3 = age range

head(data7)
############################
# Pie chart - Overall

require(dplyr)
q0002_count <- data7 %>% count(q0002)
q0002_count <- q0002_count[order(q0002_count$n),]
colnames(q0002_count) <- c("group", "total")
q0002_count$Label <- paste(round(((q0002_count$total/sum(q0002_count$total))*100),2),"%")

pie <- ggplot(q0002_count, aes(x='', y=total, fill=group)) + 
        geom_col(position = 'stack', width = 1) +
        geom_text(aes(label = Label), position = position_stack(vjust = 0.5)) + 
        labs(x = NULL, y = NULL, fill = NULL, title='Overall - all respondents')  + 
        theme_classic() +
        theme(plot.title = element_text(hjust=0.5, color = "#666666"),
              axis.line = element_blank(),
              axis.text = element_blank(),
              axis.ticks = element_blank() ) +
        coord_polar('y') 

pie_overall <- pie


##########################################
# pie2 - Age group 18-34
df <- data7 [ data7$age3 == '18 - 34', ]

q0002_count <- df %>% count(q0002)
q0002_count <- q0002_count[order(q0002_count$n),]
colnames(q0002_count) <- c("group", "total")
q0002_count$Label <- paste(round(((q0002_count$total/sum(q0002_count$total))*100),2),"%")

pie <- ggplot(q0002_count, aes(x='', y=total, fill=group)) + 
       geom_col(position = 'stack', width = 1) +
       geom_text(aes(label = Label), position = position_stack(vjust = 0.5)) + 
       labs(x = NULL, y = NULL, fill = NULL, title='Age group 18 - 34')  + 
       theme_classic() +
       theme(plot.title = element_text(hjust=0.5, color = "#666666"),
             axis.line = element_blank(),
             axis.text = element_blank(),
             axis.ticks = element_blank() ) +
       coord_polar('y') 

pie2 <- pie

##########################################
# pie3 - Age group 35-64
df <- data7 [ data7$age3 == '35 - 64', ]

q0002_count <- df %>% count(q0002)
q0002_count <- q0002_count[order(q0002_count$n),]
colnames(q0002_count) <- c("group", "total")
q0002_count$Label <- paste(round(((q0002_count$total/sum(q0002_count$total))*100),2),"%")

pie <- ggplot(q0002_count, aes(x='', y=total, fill=group)) + 
      geom_col(position = 'stack', width = 1) +
      geom_text(aes(label = Label), position = position_stack(vjust = 0.5)) + 
      labs(x = NULL, y = NULL, fill = NULL, title='Age group 35 - 64')  + 
      theme_classic() +
      theme(plot.title = element_text(hjust=0.5, color = "#666666"),
            axis.line = element_blank(),
            axis.text = element_blank(),
            axis.ticks = element_blank() ) +
      coord_polar('y') 

pie3 <- pie

##########################################
# pie4 - Age group 65 and up
df <- data7 [ data7$age3 == '65 and up', ]

q0002_count <- df %>% count(q0002)
q0002_count <- q0002_count[order(q0002_count$n),]
colnames(q0002_count) <- c("group", "total")
q0002_count$Label <- paste(round(((q0002_count$total/sum(q0002_count$total))*100),2),"%")

pie <- ggplot(q0002_count, aes(x='', y=total, fill=group)) + 
      geom_col(position = 'stack', width = 1) +
      geom_text(aes(label = Label), position = position_stack(vjust = 0.5)) + 
      labs(x = NULL, y = NULL, fill = NULL, title='Age group 65 and up')  + 
      theme_classic() +
      theme(plot.title = element_text(hjust=0.5, color = "#666666"),
            axis.line = element_blank(),
            axis.text = element_blank(),
            axis.ticks = element_blank() ) +
      coord_polar('y') 

pie4 <- pie

##################################################
#ploting multpile charts

p <- plot_grid(pie_overall, pie2, pie3, pie4)
title <- ggdraw() + draw_label("How important is it to you that others see you as masculine?", fontface='bold')

plot_grid(title, p, ncol=1, rel_heights=c(0.1, 1)) # rel_heights values control title margins
