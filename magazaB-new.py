import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import plotly.plotly as py
#from scipy import stats
import statistics
import dateutil
import sklearn.metrics

dataset = pd.read_csv('C:/Users/User/Desktop/magaza_b.csv', sep=';')
df = pd.DataFrame(dataset)

##dataset
df['TARIH'] = df['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df['TARIH'] = pd.to_datetime(df['TARIH'])
df['month'] = df['TARIH'].dt.month
df['day'] = df['TARIH'].dt.day
df['week'] = df['TARIH'].dt.week
df['year'] = df['TARIH'].dt.year
df['day_of_week'] = df['TARIH'].dt.dayofweek
days = {0:'mon',1:'tues',2:'wed',3:'thu',4:'fri',5:'sat',6:'sun'}
df['day_of_week'] = df['day_of_week'].apply(lambda x: days[x])


################################################################

var = df.groupby(['year','month'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind = 'line')
plt.show()
##############################
var = df.groupby(['year','month','day'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind = 'line')
plt.show()
########################
var = df.groupby(['year','week'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind = 'line')
plt.show()
###########################
var = df.groupby(['year','month'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
##################
var = df.groupby(['year','week'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
##############
var = df.groupby(['year','month','day'])['CIRO'].sum().head(365) #2011
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
###################3
var = df.groupby(['year','month','day'])['CIRO'].sum().head(731).tail(366) #2012
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
#####################
var = df.groupby(['year','month','day'])['CIRO'].sum().tail(365)#2013
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
#######################
var = df.groupby(['year','month'])['CIRO'].sum()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue','green','yellow','pink','magenta','cyan'], grid=False)
plt.show()

########################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['dolar']
b = df['CIRO']
ax.set_xlabel('dolar')
ax.set_ylabel('Price')
ax.scatter(a,b)
plt.show()
##################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['month'][df['year'] == 2011]
b = df['CIRO'][df['year'] == 2011]
ax.set_xlabel('month')
ax.set_ylabel('Price')
ax.scatter(a,b)
plt.show()
########################3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['month'][df['year'] == 2012]
b = df['CIRO'][df['year'] == 2012]
ax.set_xlabel('month')
ax.set_ylabel('Price')
ax.scatter(a,b)
plt.show()
###############

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['month'][df['year'] == 2013]
b = df['CIRO'][df['year'] == 2013]
ax.set_xlabel('month')
ax.set_ylabel('Price')
ax.scatter(a,b)
plt.show()
##############
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('euro')
ax.set_ylabel('Price')
a = df['euro']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
####################3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('gold')
ax.set_ylabel('Price')
a = df['altin']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
##########################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('temperature')
ax.set_ylabel('Price')
a = df['temperature']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
###########################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('special days')
ax.set_ylabel('Price')
a = df['special days']
b = df['CIRO']
ax.scatter(a,b)
plt.show()

################################
plt.figure(figsize=(10,8))
plt.scatter(df['month'][df['year'] == 2011], df['year'][df['year'] == 2011], marker='o',color='b',alpha=0.7,s = 124,)
plt.show()
##########################33

##############################3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df.groupby(['year','month','day'])['temperature'].mean()
b = df.groupby(['year','month','day'])['CIRO'].sum()
ax.scatter(a,b)
plt.show()
####################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
var = df.groupby(['TARIH','day_of_week'])['CIRO'].sum().head(30)#ocak2011
ax.set_xlabel('Day_of_week')
ax.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
####################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
var = df.groupby(['TARIH','day_of_week'])['CIRO'].sum().head(59).tail(28) #subat2011
ax.set_xlabel('Day_of_week')
ax.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
#################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
var = df.groupby(['TARIH','day_of_week'])['CIRO'].sum().head(425).tail(29)#subat2012
ax.set_xlabel('Day_of_week')
ax.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
###############
fig = plt.figure()

var = df.groupby(['TARIH','day_of_week'])['CIRO'].sum().head(790).tail(28)#subat2012
ax.set_xlabel('Day_of_week')
ax.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
##############
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df.groupby(['year','month','day'])['special days'].mean()
b = df.groupby(['year','month','day'])['CIRO'].sum()
ax.set_xlabel('Special days')
ax.set_ylabel('Price')
ax.scatter(a,b)
plt.show()

####################3
var = df.groupby(['year','month','day','day_of_week'])['CIRO'].sum().head(396).tail(31) ##2012 ocak
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('Day_of_week')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
##############
var = df.groupby(['year','month','day','day_of_week'])['CIRO'].sum().head(731).tail(31) ##2013 ocak
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('Day_of_week')
ax1.set_ylabel('Price')
var.plot(kind='bar')
plt.show()
########################
var = df.groupby(['year', 'month', 'day'])['special days'].mean()
v = df.groupby(['year', 'month', 'day'])['CIRO'].sum()
plt.hist(v, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Cıro')
plt.hist(var, bins=20, histtype='stepfilled', normed=True, color='b', label='special days')

plt.title("CIRO/SPECIALDAYS")
plt.xlabel("days")
plt.ylabel("CIRO")
plt.legend()
plt.show()
########################
#Mutual Info
review_count_altin = sklearn.metrics.mutual_info_score(df['CIRO'], df['altin'], contingency=None);
review_count_dolar = sklearn.metrics.mutual_info_score(df['CIRO'], df['dolar'], contingency=None);
review_count_euro = sklearn.metrics.mutual_info_score(df['CIRO'], df['euro'], contingency=None);
review_count_temperature = sklearn.metrics.mutual_info_score(df['CIRO'], df['temperature'], contingency=None);
###################3

#chi square
obs = df['CIRO']
do = df['dolar']/len(df['dolar'])
ex = do*len(df['CIRO'])
chi = (((obs - ex)**2)/ex).sum()
print(chi)
