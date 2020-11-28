# -*- coding: utf-8 -*-
"""
Dublin Business School
@author: Juliana Salvadori  @Student_number: 10521647
@author: Peterson Donada    @Student_number: 10521646
@Assigment: CA2

"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from itertools import cycle, islice 
import seaborn as sns
import matplotlib.patches as mpatches

'''
Load data
######################################
'''
file_name='raw-responses.csv'
data = pd.read_csv(file_name)

'''
Quick Glance
######################################
'''
view = data.head(10)
print(view)

col_names = list(data)
print(col_names)

'''
######################################
Plot cards
######################################
'''
columns = ['q0024','age3','q0026']
# age3 = age range
# q0024 = civil status
# q0026 = sexual orientation
data1 = data[columns]
   
#########################################
# 1 pie chart
s = len(data1)
# get x (sizes) and y (labels) data 
pie_labels = ['Respondents = ' + str(s)]
pie_sizes = np.array(s)
pie_colors = ['lightskyblue']
# create a figure and axis 
#fig1, ax1 = plt.subplots()
#ax1.pie(x=pie_sizes, labels = pie_labels, colors=pie_colors, labeldistance=0.0)
#ax1.set_title('Total respondents')
#plt.show()

#########################################
# 2 bar chart - horizontal
# count the occurrence of each class 
tot = data1['age3'].value_counts().sort_index()
# get x and y data 
barhx = tot.index
barhy = tot.values
width = 0.75 # the width of the bars 
ind = np.arange(len(barhy))  # the x locations for the groups
barh_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(barhy)))
# create a figure and axis 
#fig, ax1 = plt.subplots() 
#ax1.barh(ind, barhy, width, color= barh_colors)
#ax1.set_yticks(ind+width/2)
#ax1.set_yticklabels(barhx, minor=False)
#plt.show()

#########################################
# 3 stacked bar chart - 
# count the occurrence of each class 
columns = ['q0026']
stack2 = data[columns]
stack2.groupby('q0026').size()
staked2_label = ["All respondents"]

straight  = stack2[ stack2['q0026'] == 'Straight'].count()
gay       = stack2[ stack2['q0026'] == 'Gay'].count()
bisexual  = stack2[ stack2['q0026'] == 'Bisexual'].count()
other     = stack2[ stack2['q0026'] == 'Other'].count()
no_answer = stack2[ stack2['q0026'] == 'No answer'].count()

columns = ["q0026","bisexual", "gay", "no answer","other","straight"]
df = pd.DataFrame( list(zip(staked2_label,bisexual,gay,no_answer,other,straight)) , columns = columns)
df_total = df["bisexual"] + df["gay"] + df["no answer"]+df["other"]+df["straight"]
df_rel = np.round(df[df.columns[1:]].div(df_total, 0)*100,1)
start = 0
'''
fig, ax = plt.subplots(figsize=(15, 10))

ax.broken_barh([(start, df_rel["straight"])
        , (df_rel["straight"], df_rel["straight"]+ df_rel["gay"])
        , (df_rel["straight"]+df_rel["gay"], df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"])
        , (df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"], df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"])
        , (df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"], df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"]+df_rel["no answer"])
        ], [10, 9]
        , facecolors=('tab:brown', 'tab:pink', 'tab:grey','tab:olive','tab:cyan')
                      )
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_yticks([15, 25])
ax.set_xticks([0, 25, 50, 75, 100])

ax.set_axisbelow(True) 

print(df_rel["straight"].values[0])

ax.set_yticklabels([""])
ax.grid(axis='x')
ax.text(df_rel["straight"]-6, 14.5, str(df_rel["straight"].values[0])+"%", fontsize=8)
ax.text((df_rel["straight"]+ df_rel["gay"])-4, 14.5, str(df_rel["gay"].values[0])+"%", fontsize=8)
ax.text((df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"])-3, 14.5, str(df_rel["bisexual"].values[0])+"%", fontsize=8)
ax.text((df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"])-1.5, 14.5, str(df_rel["other"].values[0])+ "%", fontsize=8)
ax.text((df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"]+df_rel["no answer"])+1, 14.5, str(df_rel["no answer"].values[0])+ "%", fontsize=8)

fig.suptitle('This is title of the chart', fontsize=16)

leg1 = mpatches.Patch(color='tab:brown', label='straight')
leg2 = mpatches.Patch(color='tab:pink', label='gay')
leg3 = mpatches.Patch(color='tab:grey', label='bisexual')
leg4 = mpatches.Patch(color='tab:olive', label='other')
leg5 = mpatches.Patch(color='tab:cyan', label='no answer')
ax.legend(handles=[leg1, leg2, leg3, leg4, leg5], ncol=5)

plt.show()
'''

#########################################
# 4 line chart
# count the occurrence of each class 
tot = data1['q0024'].value_counts().sort_index()
# get x and y data 
linex = tot.index
liney = tot.values
# create a figure and axis 
#fig, ax1 = plt.subplots() 
#ax1.plot(linex, liney)
#plt.show()


#########################################
# cards
fig, ((ax1, ax2), (ax3,ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(20, 15))
# total respondentss
ax1.pie(x=pie_sizes, labels = pie_labels, colors=pie_colors, labeldistance=0.0)
ax1.set_title('Total respondents')
# total respondents by age range
ax2.barh(ind, barhy, width, color= barh_colors)
ax2.set_yticks(ind+width/2)
ax2.set_yticklabels(barhx, minor=False)
ax2.set_title('Total respondents by age group')
# total respondents by sexual orientation
ax3.broken_barh([(start, df_rel["straight"])
        , (df_rel["straight"], df_rel["straight"]+ df_rel["gay"])
        , (df_rel["straight"]+df_rel["gay"], df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"])
        , (df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"], df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"])
        , (df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"], df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"]+df_rel["no answer"])
        ], [10, 9]
        , facecolors=('tab:brown', 'tab:pink', 'tab:grey','tab:olive','tab:cyan')
                      )
ax3.set_ylim(5, 15)
ax3.set_xlim(0, 100)
ax3.spines['left'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.set_yticks([15, 25])
ax3.set_xticks([0, 25, 50, 75, 100])
ax3.set_axisbelow(True) 
ax3.set_yticklabels([""])
ax3.grid(axis='x')
ax3.text(df_rel["straight"]-6, 14.5, str(df_rel["straight"].values[0])+"%", fontsize=8)
ax3.text((df_rel["straight"]+ df_rel["gay"])-6, 14.5, str(df_rel["gay"].values[0])+"%", fontsize=8)
ax3.text((df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"])-4, 14.5, str(df_rel["bisexual"].values[0])+"%", fontsize=8)
ax3.text((df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"])-1.5, 14.5, str(df_rel["other"].values[0])+ "%", fontsize=8)
ax3.text((df_rel["straight"]+df_rel["gay"]+df_rel["bisexual"]+df_rel["other"]+df_rel["no answer"])+2, 14.5, str(df_rel["no answer"].values[0])+ "%", fontsize=8)
leg1 = mpatches.Patch(color='tab:brown', label='straight')
leg2 = mpatches.Patch(color='tab:pink', label='gay')
leg3 = mpatches.Patch(color='tab:grey', label='bisexual')
leg4 = mpatches.Patch(color='tab:olive', label='other')
leg5 = mpatches.Patch(color='tab:cyan', label='no answer')
ax3.legend(handles=[leg1, leg2, leg3, leg4, leg5], ncol=5)
ax3.set_title('Total respondents by sexual orientation')
#total respondents by civil status
ax4.plot(linex, liney, marker='o')
ax4.set_title('Total respondents by civil status')
plt.show()

'''
######################################
Plot 1
In general, how masculine or “manly” do you feel?
######################################
'''
columns = ['q0001', 'age3']
data2 = data[columns]
# add a column tot just to use it on the count
data2["Respondents"] = 1

data.groupby('q0001').size()
'''
In general, how masculine or “manly” do you feel?
No answer                14
Not at all masculine     32
Not very masculine      131
Somewhat masculine      826
Very masculine          612
'''

q0001_count = data2.groupby(['q0001']).agg({'Respondents':['count']})
q0001_count.columns = q0001_count.columns.droplevel(0)
x = []
y = []
for row in q0001_count.iterrows():
    x.append(row[0][0:20]) # get the row index
    y.append(row[1][0])    # get the count value    

fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the x locations for the groups
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(y)))
ax.barh(ind, y, width, color= my_colors)
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plt.title('In general, how masculine or “manly” do you feel?', fontsize = 15)
plt.xlabel('Number of respondents')

for i, v in enumerate(y):
    ax.text(v + 100, i, str(v), color='black', fontweight='bold', fontsize=14, ha='left', va='center')
plt.show()

#Plot the data:
# use format='svg' or 'pdf' for vectorial pictures
plt.savefig(os.path.join('test.png'), dpi=300, format='png', bbox_inches='tight') 


'''
######################################
Plot 2
How masculine do you feel? by Age group
######################################
'''
data.groupby('age3').size()
'''
What is your age?
18 - 34      133
35 - 64      855
65 and up    627
'''
data2 = data2[ data2['q0001'] != 'No answer']
q0001_age_count = data2.groupby(['q0001','age3']).agg({'Respondents':['count']})
q0001_age_count.columns = q0001_age_count.columns.droplevel(0)

x = []
y = []
z = []
for row in q0001_age_count.iterrows():
    q0001 , age = row[0][0:20]
    x.append(q0001)  # get the first row index
    y.append(age)    # get the second row index
    z.append(row[1][0])  # get the count value   
    
columns = ['q0001', 'Age group','count']    
df = pd.DataFrame( list(zip(x, y,z)), columns = columns)
fig, ax = plt.subplots(figsize=(15,10))
axe = sns.barplot(ax=ax, x="q0001", y="count", hue="Age group", data=df, palette="Blues_d")
axe.set_title("How masculine do you feel? by Age group", fontsize = 15)
axe.set(xlabel=" ", ylabel="Number of respondents")

'''
######################################
Plot 3
How masculine do you feel? by Civil status
######################################
'''
columns = ['q0001','q0024']
data3 = data[columns]
data3 = data3[ data3['q0001'] != 'No answer']
# add a column tot just to use it on the count
data3["Respondents"] = 1

data.groupby('q0024').size()
'''
Are you now married, widowed, divorced, separated, or have you never
been married?
Divorced         218
Married          996
Never married    286
No answer          8
Separated         25
Widowed           82
'''
result = data3[ data3['q0024'] != 'No answer']
q0001_status_count = result.groupby(['q0001','q0024']).agg({'Respondents':['count']})

x = []
y = []
z = []
for row in q0001_status_count.iterrows():
    q0001 , q0024 = row[0][0:20]
    x.append(q0001)    # get the first row index
    y.append(q0024)    # get the second row index
    z.append(row[1][0])  # get the count value   
    
columns = ['q0001', 'Civil Status','count']    
df = pd.DataFrame( list(zip(x, y,z)), columns = columns)
fig, ax = plt.subplots(figsize=(15,10))
axe = sns.barplot(ax=ax, x="q0001", y="count", hue="Civil Status", data=df)
axe.set_title("How masculine do you feel? by Civil status", fontsize = 15)
axe.set(xlabel=" ", ylabel="Number of respondents")

'''
######################################
Plot 4 - Q0005
Do you think that society puts pressure on men in a way that is unhealthy or bad
for them?
######################################
'''
columns = ['q0005']
data.groupby('q0005').size()
'''
How often do you try to be the one who pays when on a date?
No           647
No answer     13
Yes          955
'''
data4 = data[columns]
#Get values from the group and categories
label = ["All respondents"]
yes = data4[ data4['q0005'] == 'Yes'].count()
no  = data4[ data4['q0005'] == 'No'].count()
no_answer =  data4[ data4['q0005'] == 'No answer'].count()

columns = ["q0005","Yes", "No", "No answer"]
df = pd.DataFrame( list(zip(label,yes,no,no_answer)) , columns = columns)
# plot a Stacked Bar Chart using matplotlib 
df.plot( x = 'q0005', kind = 'barh', figsize=(10,5),
         stacked = True, 
         title = 'Do you think that society puts pressure on men in a way that is unhealthy or bad for them?', 
         mark_right = True ) 
plt.ylabel(" ")

df_total = df["Yes"] + df["No"] + df["No answer"] 
df_rel = df[df.columns[1:]].div(df_total, 0)*100
  
for n in df_rel: 
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n],  
                                         df[n], df_rel[n])): 
        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%',  
                 va = 'center', ha = 'center')


'''
######################################
Plot 4.1 - q0005 vs age3
Do you think that society puts pressure on men in a way that is unhealthy or bad
for them? by Age group
######################################
'''
yes_values = []
no_values  = []
no_answer  = []
         
result = data[['q0005','age3']]
# add a column tot just to use it on the count
result["Respondents"] = 1
result_count = result.groupby(['q0005','age3']).agg({'Respondents':['count']})

for row in result_count.iterrows():
    q0005 , age3 = row[0][0:20]
    if q0005 == 'No':
       no_values.append(row[1][0]) 
    elif q0005 == 'Yes':
       yes_values.append(row[1][0]) 
    else:
        no_answer.append(row[1][0]) 
        
df = pd.DataFrame({'Yes':yes_values,'No':no_values})
# Names of group 
names = ['18 - 34','35 - 64','65 and up']
width = 0.85 # the width of the bars 
ind = np.arange(len(yes_values))  # the x locations for the groups
ax = df.plot.barh(stacked = True
                 , width = width
                 , figsize=(10,5)
                 , title = 'Do you think that society puts pressure on men in a way that is unhealthy or bad for them? by Age group' )
for rowNum,row in df.iterrows():
    xpos = 0
    for val in row:
        xpos += val
        ax.text(xpos -30, rowNum-0.05, str(val), color='black')
    xpos = 0

ax.set_yticks(ind+width/2)
ax.set_yticklabels(names, minor=False)


'''
######################################
Plot 5 - q0017
Do you typically feel as though you’re expected to make the first move in romantic
relationships?
######################################
'''
columns = ['q0017']
data.groupby('q0017').size()
'''
No            570
No answer      31
Yes          1014
'''
data4 = data[columns]
#Get values from the group and categories
label = ["All respondents"]
yes = data4[ data4['q0017'] == 'Yes'].count()
no  = data4[ data4['q0017'] == 'No'].count()
no_answer =  data4[ data4['q0017'] == 'No answer'].count()

columns = ["q0017","Yes", "No", "No answer"]
df = pd.DataFrame( list(zip(label,yes,no,no_answer)) , columns = columns)
# plot a Stacked Bar Chart using matplotlib 
df.plot( x = 'q0017', kind = 'barh', figsize=(10,5),
         stacked = True, 
         title = 'Do you typically feel as though you’re expected to make the first move in romantic relationships?', 
         mark_right = True ) 
plt.ylabel(" ")

df_total = df["Yes"] + df["No"] + df["No answer"] 
df_rel = df[df.columns[1:]].div(df_total, 0)*100
  
for n in df_rel: 
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n],  
                                         df[n], df_rel[n])): 
        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%',  
                 va = 'center', ha = 'center')


'''
######################################
Plot 5.1 - q0017 vs age3
Do you typically feel as though you’re expected to make the first move in romantic
relationships? by Age group
######################################
'''
yes_values = []
no_values  = []
no_answer  = []
         
result = data[['q0017','age3']]
# add a column tot just to use it on the count
result["Respondents"] = 1
result_count = result.groupby(['q0017','age3']).agg({'Respondents':['count']})

for row in result_count.iterrows():
    q0017 , age3 = row[0][0:20]
    if q0017 == 'No':
       no_values.append(row[1][0]) 
    elif q0017 == 'Yes':
       yes_values.append(row[1][0]) 
    else:
        no_answer.append(row[1][0]) 
        
df = pd.DataFrame({'Yes':yes_values,'No':no_values})
# Names of group 
names = ['18 - 34','35 - 64','65 and up']
width = 0.85 # the width of the bars 
ind = np.arange(len(yes_values))  # the x locations for the groups
ax = df.plot.barh(stacked = True
                , width = width
                , figsize=(10,5)
                , title = 'Do you typically feel as though you’re expected to make the first move in romantic relationships? by Age group' )
for rowNum,row in df.iterrows():
    xpos = 0
    for val in row:
        xpos += val
        ax.text(xpos -30, rowNum-0.05, str(val), color='black')
    xpos = 0

ax.set_yticks(ind+width/2)
ax.set_yticklabels(names, minor=False)


'''
######################################
Plot 6
How often do you try to be the one who pays when on a date?
######################################
'''
columns = ['q0018','age3', 'q0024']
data.groupby('q0018').size()
'''
How often do you try to be the one who pays when on a date?
Always       794
Never         75
No answer     41
Often        457
Rarely        24
Sometimes    224
'''
data6 = data[columns]
data6 = data6[ data6['q0018'] != 'No answer']
data6 = data6[ data6['q0024'] != 'No answer']
# add a column tot just to use it on the count
data6["Respondents"] = 1

q0018_age_count = data6.groupby(['q0018','q0024','age3']).agg({'Respondents':['count']})

x = []
y = []
w = []
z = []
for row in q0018_age_count.iterrows():
    q0018, q0024, age3 = row[0][0:30]
    x.append(q0018)    # get the first row index
    w.append(q0024)    # get the second row index
    y.append(age3)     # get the third row index 
    z.append(row[1][0])  # get the count value   
    
columns = ['How often do you try to be the one who pays when on a date?','Civil Status','Age group','Number of respondents']    
df = pd.DataFrame( list(zip(x,w,y,z)), columns = columns)
axe = sns.catplot(x="How often do you try to be the one who pays when on a date?", y="Number of respondents", hue="Civil Status", col="Age group",
                  data=df, kind="bar", height= 5, aspect= 1)     

'''
######################################
Plot 7
How important is it to you that others see you as masculine?
######
'''
columns = ['q0002','age3']
data.groupby('q0002').size()
'''
No answer                 9
Not at all important    240
Not too important       541
Somewhat important      628
Very important          197
'''  
data7 = data[columns]
data7 = data7[ data7['q0002'] != 'No answer']
# add a column tot just to use it on the count
data7["Respondents"] = 1
##########################################
# pie1
q0002_count = data7.groupby(['q0002']).agg({'Respondents':['count']})
x = []
y = []
for row in q0002_count.iterrows():
    x.append(row[0][0:20])  # get the row index
    y.append(row[1][0])     # get the count value      
total = sum(y)
y_pct = [ np.round( (x / total)*100,1) for x in y]    
# get x (sizes) and y (labels) data 
labels1 = x
sizes1 = np.array(y_pct)              

##########################################
# pie2 - Age group 18-34
q0002 = data7[ data7['age3'] == '18 - 34']
q0002_count = q0002.groupby(['q0002']).agg({'Respondents':['count']})
x = []
y = []
for row in q0002_count.iterrows():
    x.append(row[0][0:20])  # get the row index
    y.append(row[1][0])     # get the count value      
total = sum(y)
y_pct = [ np.round( (x / total)*100,1) for x in y]    
# get x (sizes) and y (labels) data 
labels2 = x
sizes2 = np.array(y_pct)    
##########################################
# pie3 - Age group 35-64
q0002 = data7[ data7['age3'] == '35 - 64']
q0002_count = q0002.groupby(['q0002']).agg({'Respondents':['count']})
x = []
y = []
for row in q0002_count.iterrows():
    x.append(row[0][0:20])  # get the row index
    y.append(row[1][0])     # get the count value      
total = sum(y)
y_pct = [ np.round( (x / total)*100,1) for x in y]    
# get x (sizes) and y (labels) data 
labels3 = x
sizes3 = np.array(y_pct)        
##########################################
# pie4 - Age group 65 and up
q0002 = data7[ data7['age3'] == '65 and up']
q0002_count = q0002.groupby(['q0002']).agg({'Respondents':['count']})
x = []
y = []
for row in q0002_count.iterrows():
    x.append(row[0][0:20])  # get the row index
    y.append(row[1][0])     # get the count value      
total = sum(y)
y_pct = [ np.round( (x / total)*100,1) for x in y]    
# get x (sizes) and y (labels) data 
labels4 = x
sizes4 = np.array(y_pct)          
         
#########################################
# cards
fig, ((ax1, ax2), (ax3,ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
fig.suptitle('How important is it to you that others see you as masculine?', fontsize = 15)
# pie1 - overal
ax1.pie(x=sizes1, labels=labels1, autopct='%1.1f%%')
ax1.set_title('Overall - all respondets')
# pie2 - 
ax2.pie(x=sizes2, labels=labels2, autopct='%1.1f%%')
ax2.set_title('Age group 18 - 34')
# pie3
ax3.pie(x=sizes3, labels=labels3, autopct='%1.1f%%')
ax3.set_title('Age group 35 - 64')
# pie4
ax4.pie(x=sizes4, labels=labels4, autopct='%1.1f%%')
ax4.set_title('Age group 65 and up')
plt.show()