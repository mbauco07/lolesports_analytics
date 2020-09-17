import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import global_functions as gfs
import sys

#-----------------------------------------------FUNCTIONS-----------------------------------------------#
#if the system detects nickname instead of a chamions proper name we will auto change it to the proper name



#instead of having the first lines of code be the cleaning of the datasets, just move all the cleaning into one function to clean 
#up main
def clean_data(df, _champ):  
    #once we have the correct champion name we will get the stats from each of the main regions (LCS,LEC,LCK,LPL)
    df = df[df['Champion'] == _champ]
    
    df = df.rename(columns={"W%": "WP"})
    df['WP'] = df['WP'].map(lambda x: x.strip('%'))
    convert_dict= {
        'WP': float
    }
    df = df.astype(convert_dict)
    df = df.sort_values(by=['Pos'])
    return df



#-----------------------------------------------FUNCTIONS-----------------------------------------------#

#-----------------------------------------------MAIN-----------------------------------------------#
champ = gfs.check_for_nickName(sys.argv[1].lower().capitalize())

#read in Data
lcs_df = clean_data(pd.read_csv('Oracles Elixir Data\LCS\LCS 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv'), champ)
lec_df = clean_data(pd.read_csv('Oracles Elixir Data\LEC\LEC 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv'), champ)
lck_df = clean_data(pd.read_csv('Oracles Elixir Data\LCK\LCK 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv'), champ)
lpl_df = clean_data(pd.read_csv('Oracles Elixir Data\LPL\LPL 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv'), champ)



#clean the datasets and only get the data for the champion asked for




#print(lcs_df.head())
#print(lec_df.head())
#print(lck_df.head())
#print(lpl_df.head())

colors = ['green', 'red', 'blue', 'orange', 'gold']      

# Make figure and axes
fig, axs = plt.subplots(4, 2)
fig.suptitle(champ + " Plays per Role per Region during Playoffs")
# A standard pie plot
axs[0,0].set_title("LCS")
axs[0, 0].pie(lcs_df.GP, labels=lcs_df.Pos,autopct=gfs.make_autopct(lcs_df  .GP), shadow=True, colors=colors)
axs[0,1].bar(lcs_df.Pos, lcs_df.WP, align='center', color=colors)
axs[0,1].set_title("Win Percentage Per Role")
axs[0,1].set_yticks([0,25,50,75,100]) 


axs[1,0].set_title("LEC")
axs[1, 0].pie(lec_df.GP, labels=lec_df.Pos, autopct=gfs.make_autopct(lec_df.GP), shadow=True, colors=colors)
axs[1,1].bar(lec_df.Pos, lec_df.WP, align='center', color=colors)
axs[1,1].set_yticks([0,25,50,75,100]) 

axs[2,0].set_title("LCK")
axs[2, 0].pie(lck_df.GP, labels=lck_df.Pos, autopct=gfs.make_autopct(lck_df.GP), shadow=True, colors=colors)
axs[2,1].bar(lck_df.Pos, lck_df.WP, align='center', color=colors )
axs[2,1].set_yticks([0,25,50,75,100]) 

axs[3,0].set_title("LPL")
axs[3, 0].pie(lpl_df.GP, labels=lpl_df.Pos, autopct=gfs.make_autopct(lpl_df.GP), shadow=True, colors=colors)
axs[3,1].bar(lpl_df.Pos, lpl_df.WP, align='center', color=colors)
axs[3,1].set_yticks([0,25,50,75,100])

fig.set_size_inches(8, 6)
plt.savefig(champ+"_DifferencesPerRegion.png", dpi=100)  



plt.show()
#-----------------------------------------------MAIN-----------------------------------------------#
