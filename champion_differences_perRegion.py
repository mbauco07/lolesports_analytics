import pandas as pd
import thinkstats2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import sys


#if the system detects nickname instead of a chamions proper name we will auto change it to the proper name
def check_for_nickName(_nickName):
    if _nickName in champ_Nicknames:
        return champ_Nicknames[_nickName]

    return _nickName

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct

champ_Nicknames = {
    'mf': 'Miss Fortune', 
    'bambi' : 'Lillia',
    'electric bear' : 'Volibear',
    'alligator' : 'Renekton'
}
#read in Data
lcs_df = pd.read_csv('Oracles Elixir Data\LCS\LCS 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv')
lec_df = pd.read_csv('Oracles Elixir Data\LEC\LEC 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv')
lck_df = pd.read_csv('Oracles Elixir Data\LCK\LCK 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv')
lpl_df = pd.read_csv('Oracles Elixir Data\LPL\LPL 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv')

#for index, row in df.iterrows(): 
#   print (row["Champion"] + " Games Played: "+ str(row["GP"]) +" in " + row["Pos"]) 

champ = check_for_nickName(sys.argv[1].lower().capitalize())


lcs_df = lcs_df.rename(columns={"W%": "WP"})
lec_df = lec_df.rename(columns={"W%": "WP"})
lck_df = lck_df.rename(columns={"W%": "WP"})
lpl_df = lpl_df.rename(columns={"W%": "WP"})

#once we have the correct champion name we will get the stats from each of the main regions (LCS,LEC,LCK,LPL)
lcs_df = lcs_df[lcs_df['Champion'] == champ]
lec_df = lec_df[lec_df['Champion'] == champ]
lck_df = lck_df[lck_df['Champion'] == champ]
lpl_df = lpl_df[lpl_df['Champion'] == champ]

lcs_df['WP'] = lcs_df['WP'].map(lambda x: x.strip('%'))
lec_df['WP'] = lec_df['WP'].map(lambda x: x.strip('%'))
lck_df['WP'] = lck_df['WP'].map(lambda x: x.strip('%'))
lpl_df['WP'] = lpl_df['WP'].map(lambda x: x.strip('%'))

convert_dict= {
    'WP': float
}
lcs_df = lcs_df.astype(convert_dict)
lec_df = lec_df.astype(convert_dict)
lck_df = lck_df.astype(convert_dict)
lpl_df = lpl_df.astype(convert_dict)

lcs_df = lcs_df.sort_values(by=['Pos'])
lec_df = lec_df.sort_values(by=['Pos'])
lck_df = lck_df.sort_values(by=['Pos'])
lpl_df = lpl_df.sort_values(by=['Pos'])
#print(lcs_df.head())
#print(lec_df.head())
#print(lck_df.head())
#print(lpl_df.head())

colors = ['green', 'red', 'blue', 'orange', 'gold']      

# Make figure and axes
fig, axs = plt.subplots(4, 2)
fig.suptitle(champ + " Plays per Role per Region")
# A standard pie plot
axs[0,0].set_title("LCS")
axs[0, 0].pie(lcs_df.GP, labels=lcs_df.Pos,autopct=make_autopct(lcs_df  .GP), shadow=True, colors=colors)
axs[0,1].bar(lcs_df.Pos, lcs_df.WP, align='center', color=colors)
axs[0,1].set_title("Win Percentage Per Role")
axs[0,1].set_yticks([0,25,50,75,100]) 


axs[1,0].set_title("LEC")
axs[1, 0].pie(lec_df.GP, labels=lec_df.Pos, autopct=make_autopct(lec_df.GP), shadow=True, colors=colors)
axs[1,1].bar(lec_df.Pos, lec_df.WP, align='center', color=colors)
axs[1,1].set_yticks([0,25,50,75,100]) 

axs[2,0].set_title("LCK")
axs[2, 0].pie(lck_df.GP, labels=lck_df.Pos, autopct=make_autopct(lck_df.GP), shadow=True, colors=colors)
axs[2,1].bar(lck_df.Pos, lck_df.WP, align='center', color=colors )
axs[2,1].set_yticks([0,25,50,75,100]) 

axs[3,0].set_title("LPL")
axs[3, 0].pie(lpl_df.GP, labels=lpl_df.Pos, autopct=make_autopct(lpl_df.GP), shadow=True, colors=colors)
axs[3,1].bar(lpl_df.Pos, lpl_df.WP, align='center', color=colors)
axs[3,1].set_yticks([0,25,50,75,100]) 




plt.show()
