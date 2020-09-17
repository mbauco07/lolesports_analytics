#the goal of player_insigths.py will be to compare:
#1: Compare a player for a league to his peers in his position 
#2: Compare a player to the TOP players of the same role in the other leagues (TOP 3).
#3 We can only just compare a position without focusing on a specific player 


##THIS WILL BE FOR WORLDS TEAMS ONLY##

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import global_functions as gfs
import sys

#-----------------------------------------------FUNCTIONS-----------------------------------------------#
def clean_df(_df):
    _df = _df.rename(columns={"W%": "WP", "CTR%": "CTRP", "KS%": "KSP", "DTH%": "DTHP", "FB%": "FBP", "CS%P15": "CSP15P", "DMG%": "DMGP", "GOLD%": "GOLDP"})

    _df['WP'] = _df['WP'].map(lambda x: x.strip('%'))
    _df['CTRP'] = _df['CTRP'].map(lambda x: x.strip('%'))
    _df['KP'] = _df['KP'].map(lambda x: x.strip('%'))
    _df['FBP'] = _df['FBP'].map(lambda x: x.strip('%'))
    _df['KSP'] = _df['KSP'].map(lambda x: x.strip('%'))
    _df['DTHP'] = _df['DTHP'].map(lambda x: x.strip('%'))
    _df['CSP15P'] = _df['CSP15P'].map(lambda x: x.strip('%'))
    _df['DMGP'] = _df['DMGP'].map(lambda x: x.strip('%'))
    _df['GOLDP'] = _df['GOLDP'].map(lambda x: x.strip('%'))
    _df['KP'] = _df['KP'].map(lambda x: x.strip('%'))

    convert_dict= {
        'WP': float,
        'CTRP': float,
        'K': int,
        'D': int,   
        'A': int,
        'KSP': float,
        'DTHP': float,
        'FBP': float,
        'GD10': int,
        'XPD10': int,
        'CSD10': float,
        'CSPM': float,
        'CSP15P': float,
        'DMGP': float,
        'WPM': float,
        'WCPM': float
    }
    _df = _df.astype(convert_dict) 
    _df = _df.replace(['-'], 0)    

    return _df

def check_if_player_exists(_df, _player):
    _df = _df[(_df['Player'] == _player)]

    if _df.empty:
        raise Exception('PLAYER IS NOT IN DATAFRAME GUESS HE IS NOT A WORLDs \_(\'_\')_/' + _player)

    return (_player,  _df['Pos'].item())

def create_stats(_df, _player_row):
    groups = df.groupby("League")
    #create a scatter plot to compare a players CSD at 10 vs their CS per Minute
    fig, ax = plt.subplots()
    ax.scatter(_df['CSPM'], _df['CSD10'], alpha=0.5)

    ax.set_xlabel('CS Per Minute', fontsize=7)
    ax.set_ylabel('CS Difference at 10 minutes', fontsize=7)
    ax.set_title('Comparing '+_player_row['Pos'].item()+' CSD at 10 versus their CS per Minute')
    for name, group in groups:
        plt.plot(group["CSPM"], group["CSD10"], marker="o", linestyle="", label=name)

    for index, row in df.iterrows():
        #ax.annotate(txt, (z[i], y[i]))
           ax.annotate(row['Player'], (_df['CSPM'][index], _df['CSD10'][index]))
    ax.grid(True)
    plt.legend(bbox_to_anchor=(0, 0))
    plt.subplots_adjust(left=None, bottom=0.229) 
    plt.show()


#-----------------------------------------------FUNCTIONS-----------------------------------------------#


#-----------------------------------------------MAIN-----------------------------------------------#

##code to concant and create one large df instead of using 4 seperate dataframes
#lcs_df = pd.read_csv('Oracles Elixir Data\worlds\LCS 2020 - Player Stats - OraclesElixir.csv')
#lec_df = pd.read_csv("Oracles Elixir Data\worlds\LEC 2020 - Player Stats - OraclesElixir.csv")
#lpl_df = pd.read_csv("Oracles Elixir Data\worlds\LPL 2020 - Player Stats - OraclesElixir.csv")
#lck_df = pd.read_csv("Oracles Elixir Data\worlds\LCK 2020 - Player Stats - OraclesElixir.csv")

#lcs_df.insert(2,"League", ['LCS', 'LCS', 'LCS' ,'LCS','LCS','LCS','LCS','LCS','LCS','LCS','LCS','LCS','LCS','LCS','LCS','LCS'])
#lec_df.insert(2,"League", ['LEC', 'LEC', 'LEC' ,'LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC','LEC'])
#lpl_df.insert(2,"League", ['LPL', 'LPL', 'LPL' ,'LPL','LPL','LPL','LPL','LPL','LPL','LPL','LPL','LPL','LPL','LPL','LPL',])
#lck_df.insert(2,"League", ['LCK', 'LCK', 'LCK' ,'LCK','LCK','LCK','LCK','LCK','LCK','LCK','LCK','LCK','LCK','LCK','LCK',])
#frames = [lcs_df, lec_df, lck_df, lpl_df]

#df = pd.concat(frames)

#df.to_csv (r'Oracles Elixir Data\worlds\all_players_data - OraclesElixir.csv ', index = False, header=True)
df = clean_df(pd.read_csv('Oracles Elixir Data\\worlds\\all_players_data - OraclesElixir.csv'))

player, position = check_if_player_exists(df, gfs.fix_playerName(sys.argv[1]))
#after we get the player check complete we will remove all rows from our dataset that is not the same role as the player provided
df = df[(df['Pos'] == position)]

create_stats(df, df[(df['Player'] == player)])


#-----------------------------------------------MAIN-----------------------------------------------#


