import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import iplot


'''x=np.linspace(0,5,11)
y=x**2
print(x)
print(y)
plt.plot(x,y)
plt.title("basic  graph understanding")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


#subplots in matplotlib
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(y,x)
plt.subplot(2,2,3)
plt.plot(x**2,x**2)
plt.subplot(2,2,4)
plt.plot(x**2,y)
plt.show()'''

#seaborn 
df=sns.load_dataset('tips')
print(df)
'''sns.displot(df['total_bill'])#gives histogram of bill sections
#plt.show()
sns.histplot(df["total_bill"],bins=20,kde=True)
plt.show()
sns.jointplot(x='total_bill',y='tip',data=df,kind="scatter")
plt.show()
sns.jointplot(x='total_bill',y='tip',data=df,kind="hex")
plt.show()
sns.pairplot(df)
plt.show()
sns.pairplot(df,hue='sex',palette="rainbow") #categorial data
plt.show()'''

#catelogical data plots
'''sns.countplot(data=df, x='sex', hue='smoker')
plt.show()'''

'''sns.barplot(x=df['sex'],y=df['total_bill'])
plt.show()
sns.barplot(x=df['sex'],y=df['total_bill'],estimator=np.sum)
plt.show()'''
'''sns.boxplot(x=df['tip'],hue=df['day'],data=df,palette='rainbow')
plt.show()
sns.stripplot(x=df['tip'],hue=df['day'],data=df,palette='rainbow')
plt.show()
sns.swarmplot(x=df['tip'],hue=df['day'],data=df,palette='rainbow')
plt.show()
sns.violinplot(x=df['tip'],hue=df['day'],data=df,palette='rainbow')
plt.show()'''

#Matrix plot
flight=sns.load_dataset('flights')
print(flight)
#data corelation

'''tipscorr=df[['total_bill','tip','size']]
print(tipscorr.corr())'''

#using heatmap
'''sns.heatmap(tipscorr.corr(),annot=True) # in the graph they show the white colour means they have highest ccorrelation and darkest means lowest correlation
plt.show()
sns.clustermap(tipscorr.corr())
plt.show()'''

#using heatmaps with pivot tables
'''pvtflight=flight.pivot_table(values='passengers',index='month',columns='year')
print(pvtflight)
sns.heatmap(pvtflight)
plt.show()'''

#Regression plots
'''sns.lmplot(x='total_bill',y='tip',data=df,hue='sex')
plt.show() #it will give us the prediction of tips '''

#usinf cufflinks and plotly
df['total_bill'].iplot()
plt.show()