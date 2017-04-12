import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
#from scipy import stats
import statistics
import dateutil

dataset = pd.read_csv('C:/Users/User/Desktop/MAGAZA_B_2011-2013.csv', sep=';')
df = pd.DataFrame(dataset)

dolardata = pd.read_csv('C:/Users/User/Desktop/dolar.csv', sep=';')
df_dolar = pd.DataFrame(dolardata)

eurodata = pd.read_csv('C:/Users/User/Desktop/euro.csv', sep=';')
df_euro = pd.DataFrame(eurodata)

golddata= pd.read_csv('C:/Users/User/Desktop/gold.csv', sep=';')
df_gold = pd.DataFrame(golddata)

temperaturedata = pd.read_csv('C:/Users/User/Desktop/temperature.csv', sep=';')
df_temperature = pd.DataFrame(temperaturedata)

daysdata = pd.read_csv('C:/Users/User/Desktop/special_days.csv', sep=';')
df_days = pd.DataFrame(daysdata)



##dataset
df['TARIH'] = df['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df['TARIH'] = pd.to_datetime(df['TARIH'])
df['month'] = df['TARIH'].dt.month
df['day'] = df['TARIH'].dt.day
df['week'] = df['TARIH'].dt.week
df['year'] = df['TARIH'].dt.year
df['day_of_week'] = df['TARIH'].dt.dayofweek
days = {0:'0',1:'0',2:'0',3:'0',4:'0',5:'1',6:'1'}
df['day_of_week'] = df['day_of_week'].apply(lambda x: days[x])

##for data of dolar
df_dolar['TARIH'] = df_dolar['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df_dolar['TARIH'] = pd.to_datetime(df_dolar['TARIH'])
df_dolar['month'] = df_dolar['TARIH'].dt.month
df_dolar['day'] = df_dolar['TARIH'].dt.day
df_dolar['week'] = df_dolar['TARIH'].dt.week
df_dolar['year'] = df_dolar['TARIH'].dt.year


##for data of euro
df_euro['TARIH'] = df_euro['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df_euro['TARIH'] = pd.to_datetime(df_euro['TARIH'])
df_euro['month'] = df_euro['TARIH'].dt.month
df_euro['day'] = df_euro['TARIH'].dt.day
df_euro['week'] = df_euro['TARIH'].dt.week
df_euro['year'] = df_euro['TARIH'].dt.year


## for data of gold
df_gold['TARIH'] = df_gold['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df_gold['TARIH'] = pd.to_datetime(df_gold['TARIH'])
df_gold['month'] = df_gold['TARIH'].dt.month
df_gold['day'] = df_gold['TARIH'].dt.day
df_gold['week'] = df_gold['TARIH'].dt.week
df_gold['year'] = df_gold['TARIH'].dt.year


##for data of temperature
df_temperature['TARIH'] = df_temperature['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df_temperature['TARIH'] = pd.to_datetime(df_temperature['TARIH'])
df_temperature['month'] = df_temperature['TARIH'].dt.month
df_temperature['day'] = df_temperature['TARIH'].dt.day
df_temperature['week'] = df_temperature['TARIH'].dt.week
df_temperature['year'] = df_temperature['TARIH'].dt.year


#for data of special_days
df_days['TARIH'] = df_days['TARIH'].apply(dateutil.parser.parse, dayfirst=True)
df_days['TARIH'] = pd.to_datetime(df_days['TARIH'])
df_days['month'] = df_days['TARIH'].dt.month
df_days['day'] = df_days['TARIH'].dt.day
df_days['week'] = df_days['TARIH'].dt.week
df_days['year'] = df_days['TARIH'].dt.year


##addition datas in df.
for i in range(0,len(df_dolar['TARIH'])):
    df.loc[df['day'] == df_dolar['day'][i], 'dolar'] = df_dolar['dolar'][i];
    df.loc[df['day'] == df_euro['day'][i], 'euro'] = df_euro['euro'][i];
    df.loc[df['day'] == df_gold['day'][i], 'gold'] = df_gold['gold'][i];
    df.loc[df['day'] == df_temperature['day'][i], 'temperature'] = df_temperature['temperature'][i];
    df.loc[df['day'] == df_days['day'][i], 'special_days'] = df_days['special_days'][i];


################################################################

var = df.groupby(['year','month'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('DATE')
ax1.set_ylabel('Price')
var.plot(kind = 'line')
plt.show()
##############################
var = df.groupby(['year','day'])['CIRO'].sum()
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
var.plot(kind='bar')
plt.show()
##################
var = df.groupby(['year','day'])['CIRO'].sum()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
var.plot(kind='bar')
plt.show()
##############

var = df.groupby(['year','month'])['CIRO'].sum()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue','green','yellow','pink','magenta','cyan'], grid=False)
plt.show()

########################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df_dolar['dolar']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
##################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['month'][df['year'] == 2011]
b = df['CIRO'][df['year'] == 2011]
ax.scatter(a,b)
plt.show()
########################3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['month'][df['year'] == 2012]
b = df['CIRO'][df['year'] == 2012]
ax.scatter(a,b)
plt.show()
###############

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df['month'][df['year'] == 2013]
b = df['CIRO'][df['year'] == 2013]
ax.scatter(a,b)
plt.show()
##############
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df_euro['euro']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
####################3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df_gold['gold']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
##########################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df_temperature['temperature']
b = df['CIRO']
ax.scatter(a,b)
plt.show()
###########################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
a = df_days['special_days']
b = df['CIRO']
ax.scatter(a,b)
plt.show()

################################
plt.figure(figsize=(10,8))
plt.scatter(df['month'][df['year'] == 2011], df['year'][df['year'] == 2011], marker='o',color='b',alpha=0.7,s = 124,)
plt.show()
