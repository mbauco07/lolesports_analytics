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
import matplotlib
import sys


#-----------------------------------------------FUNCTIONS-----------------------------------------------#
def clean_data(df , _champ, _role):
    #get Data for the correct champion in the specified position
    df = df[(df['Pos'] == _role) and (df['Champion'] != _champ)]

    #rename columns to easier read names and change their type (because it is a csv it is all strings)
    df = df.rename(columns={"W%": "WP", "P%" : "PP", "B%" : "BP", "P+B%" : "PBP", "CTR%": "CTRP"})
    #remove any trailing characthers that will not make typechanging work
    df['WP'] = df['WP'].map(lambda x: x.strip('%'))
    df['PP'] = df['PP'].map(lambda x: x.strip('%'))
    df['BP'] = df['BP'].map(lambda x: x.strip('%'))
    df['PBP'] = df['PBP'].map(lambda x: x.strip('%'))
    df['CTRP'] = df['CTRP'].map(lambda x: x.strip('%'))

    convert_dict= {
        'WP': float,
        'PP': float,
        'BP': float,
        'PBP': float,
        'CTRP': float
    }
    df = df.astype(convert_dict)
    return df


#The whole idea behing this script is to have create COMPARATIVE visualisations between the given champ versus other champion in her same role
#We want to also create an automated script that will come with the visualisations to help explain what the visualisations are showing.
def create_insigths(_champ, df):
    index = len(df.index) #we remove one because we do not want to account for our champion
    print(index)
#-----------------------------------------------FUNCTIONS-----------------------------------------------#




#-----------------------------------------------MAIN-----------------------------------------------#
champ = gfs.check_for_nickName(sys.argv[1].lower().capitalize())
role = sys.argv[2].lower().capitalize()
_league = sys.argv[3].upper()

df = clean_data(pd.read_csv('Oracles Elixir Data\\'+_league+'\\'+_league+' 2020 Summer Playoffs - Champion Stats - OraclesElixir.csv'), champ, role)


create_insigths(champ, df)
#-----------------------------------------------MAIN-----------------------------------------------#
