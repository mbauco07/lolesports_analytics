#champion insigths will focus on a specific Champion in a specific position in a specific league IE Lillia in LPL.
#the point of this script is to get some details into why a specific champion is doing better/worse in a specific league versus others
# For example Lillia has under a 50% win in all major regions in JG with its highest being at 40ish in LCS. 

#TODO:
#Will try to create a automatic "write-up" as well as the visualtions, the idea being this is to have a short idea of what COULD be a reason why
#upon first inspection (is she being blind-picked or being used as a counter pick, etc)


#data cleaning function
#we want to get only rows for a specific champion
#_champ: name of the champ that we want
#_role: role that the champ must be playing

import pandas as pd
import global_functions as gfs
import matplotlib.pyplot as plt
import sys


#-----------------------------------------------FUNCTIONS-----------------------------------------------#
def clean_data(df , _champ, _role):
    #get Data for the correct champion in the specified position
    df = df[(df['Pos'] == _role)] 

    #rename columns to easier read names and change their type (because it is a csv it is all strings)
    df = df.rename(columns={"W%": "WP", "P%" : "PP", "B%" : "BP", "GOLD%" : "GOLDP", "CTR%": "CTRP", "DMG%":"DMG"})

    #remove any trailing characthers that will not make typechanging work
    df['WP'] = df['WP'].map(lambda x: x.strip('%'))
    df['PP'] = df['PP'].map(lambda x: x.strip('%'))
    df['BP'] = df['BP'].map(lambda x: x.strip('%'))
    df['GOLDP'] = df['GOLDP'].map(lambda x: x.strip('%'))
    df['CTRP'] = df['CTRP'].map(lambda x: x.strip('%'))
    df['KP'] = df['KP'].map(lambda x: x.strip('%'))
    df['DMG'] = df['DMG'].map(lambda x: x.strip('%'))
    
    convert_dict= {
        'WP': float,
        'PP': float,
        'BP': float,
        'GOLDP': float,
        'CTRP': float,
        'KP': float,
        'DMG': float,
        'DPM': int
    }
    df = df.astype(convert_dict) 
    df = df.replace(['-'], 0)    
    champ_df = df[(df['Champion'] == _champ)]
    if champ_df.empty:
         raise Exception('EXECEPTION THE CHAMPION CHOSEN WAS NEVER PICKED THEREFORE WE CANNOT CREATE INISGHTS BASED ON THEM CHAMPION: ' + _champ)
    return (df, champ_df)


#The whole idea behing this script is to have create COMPARATIVE visualisations between the given champ versus other champion in her same role
#We want to also create an automated script that will come with the visualisations to help explain what the visualisations are showing.
def create_insigths(_champ_df, all_champ_df):

    #get  average WP for all other champs round(non_champ_df['WP'].mean(),2))
    #standard deviation for GP: round(non_champ_df['GP'].std())
    #average games played: round(non_champ_df['GP'].mean())
    #we want to comapare our champion to the most seens champions (to do this we can look at all champions that have GP >= mean + std)

    #we will compare our champion the champions near the same amount of games played and the top played champion if they arent that champion
    kp_bins = 10
    gp_bins= 5
    tdmg_bin = 7

    fig, axs = plt.subplots(3, 2)
    fig.suptitle("Comparing: "+ champ + " to Other Champions playing " +role+ " in the " + league)
    #KP
    axs[0,0].set_title("Kill Participation in %")
    axs[0,0].hist(all_champ_df['KP'], kp_bins, color = 'green', alpha=0.8, edgecolor='black', linewidth=1.2)

    #GP
    axs[0,1].set_title("Games Played")
    axs[0,1].hist(all_champ_df['GP'], gp_bins, color = 'blue', alpha=0.8, edgecolor='black', linewidth=1.2)

    #WP
    axs[1,0].set_title("Wins Percentage")
    axs[1,0].hist(all_champ_df['WP'], kp_bins, color = 'yellow', alpha=0.8, edgecolor='black', linewidth=1.2)

    #WP
    axs[1,1].set_title("Damage Per Minute")
    axs[1,1].hist(all_champ_df['DPM'], kp_bins, color = 'orange', alpha=0.8, edgecolor='black', linewidth=1.2)

    #GOLDP
    axs[2,0].set_title("Champion Gold Share")
    axs[2,0].hist(all_champ_df['GOLDP'], gp_bins, color = 'blue', alpha=0.8, edgecolor='black', linewidth=1.2)
    
    #DMG
    axs[2,1].set_title("Percent of Team's Damage")
    axs[2,1].hist(all_champ_df['DMG'], tdmg_bin, color = 'red', alpha=0.8, edgecolor='black', linewidth=1.2)


    fig.text(0.06, 0.5, 'Total Champions per Bin', ha='center', va='center', rotation='vertical')
    plt.subplots_adjust(left=None, bottom=0.075, right=None, top=None, wspace=None, hspace=0.5) 
    fig.set_size_inches(8, 6)
    plt.savefig(champ+"_"+role+"_"+league+".png", dpi=100)  

    #print(round(all_champ_df['GP'].mean()))
    #print(all_champ_df[all_champ_df['GP'] <= round(all_champ_df['GP'].mean())])
    file = open(champ+"_"+role+"_"+league+"-insight.txt", "w+") 
    line1 = "This text file will help to understand the figures that compare " + champ + " to the rest of the champions played in " + role + " in the " + league + ".\n"
    line2 = champ + " has a " + str(_champ_df['KP'].item()) + " Kill Participation while the league average is " + str(round(all_champ_df['KP'].mean(),2)) + ".\n"
    line3 = champ + " has a " + str(_champ_df['GP'].item()) + " Games Played while the league average is " + str(round(all_champ_df['GP'].mean(),2))+ ".\n"
    line4 = champ + " has a " + str(_champ_df['WP'].item()) + " Win Percentage while the league average is " + str(round(all_champ_df['WP'].mean(),2))+ ".\n"
    line5 = champ + " has a " + str(_champ_df['DPM'].item()) + " Damage Per Minute while the league average is " + str(round(all_champ_df['DPM'].mean(),2))+ ".\n"
    line6 = champ + " has a " + str(_champ_df['GOLDP'].item()) + " Percent of the team gold share while the league average is " + str(round(all_champ_df['GOLDP'].mean(),2))+ ".\n"
    line7 = champ + " has a " + str(_champ_df['DMG'].item()) + " Percent of team's damage while the league average is " + str(round(all_champ_df['DMG'].mean(),2))+ ".\n"
    text = [line1, line2, line3, line4, line5, line6, line7]
    for line  in text:
        file.write(line)
    file.close() 

   #we now generate a textfile that we can use will looking at the figure to compare our champion to all champions





#-----------------------------------------------FUNCTIONS-----------------------------------------------#




#-----------------------------------------------MAIN-----------------------------------------------#
champ = gfs.check_for_nickName(sys.argv[1].lower().capitalize())
role = sys.argv[2].lower().capitalize()
league = sys.argv[3].upper()

#this returns our dataset without our champion included because of this we must also create a df that ONLY includes our champion
all_champ_df, champ_df = clean_data(pd.read_csv('Oracles Elixir Data\\'+league+'\\'+league+' 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv'), champ, role)

create_insigths(champ_df, all_champ_df)
#-----------------------------------------------MAIN-----------------------------------------------#
