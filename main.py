import pandas as pd
import thinkstats2
import matplotlib.pyplot as plt



#read in Data
df = pd.read_csv('Oracles Elixir Data\LCS 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv')
#print(df.head())

#for index, row in df.iterrows(): 
#   print (row["Champion"] + " Games Played: "+ str(row["GP"]) +" in " + row["Pos"]) 

#we need to first remove all '%' chars so we can convert to strings
gp_df = df[df['GP'] > 0]
gp_df['P%'] = gp_df['P%'].map(lambda x: x.strip('%'))
convert_dict= {
    'P%': float
}
gp_df = gp_df.astype(convert_dict)
gp_df.plot.bar(x='P%', y='GP',  rot=70, title="Pick Percentage LCS Summer Playoffs")
plt.xticks(gp_df['P%'], gp_df['Champion'])

plt.show()