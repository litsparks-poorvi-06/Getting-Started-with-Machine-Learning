import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv('IPL.csv')
print(df.head())
print(df.info()) #gives information about the dataset
print(f"your rows are {df.shape[0]} and your columns are {df.shape[1]}") #gives no of rows and columns
print(df.isnull().sum())

#Which team won the most matches?
'''matchwin=df['match_winner'].value_counts()
print(matchwin)
sns.barplot(y=matchwin.index,x=matchwin.values,palette='rainbow') # matchwin.index- table index, matchwin .value-table values
plt.title("Most Match Winner") 
plt.show()

#toss decision
sns.countplot(x=df['toss_decision'],palette='rainbow') #shows no of team opted for fields or bat
plt.title("Toss Decision Trends")
plt.show()

#toss winner vs match winner
count=df[df['toss_winner']==df['match_winner']] ['match_id'].count()
percentage=(count*100)/df.shape[0]
print(percentage) # means number of chances if you are wining toss then you will win the match '''

#how do teams win? run or wickets
'''sns.countplot(x=df['won_by'])
plt.show()
count1=df['player_of_the_match'].head(10)
print(count1)
sns.barplot(y=count1.values,x=count1.index)
plt.show()'''

#Top Scorer using groupby
'''high=df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2) #means we are gruoupby top scorers by highscore and we will sum the highscore means per player got how many scores and sorting by ascending order
print(high)'''

#bestbowler
df['highest_wicket'] = df['best_bowling_figure'].apply(lambda x: x.split('--')[0])
df['highest_wicket']=df['highest_wicket'].astype(int)
top_bowler=df.groupby('best_bowling')['highest_wicket'].sum().sort_values(ascending=False).head(10)
print(top_bowler)
top_bowler.plot(kind='bar')
plt.show()