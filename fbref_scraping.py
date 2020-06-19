# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:58:45 2020

@author: Ciaran
"""

def fbref_player_stats(url):
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import re
    
    response = requests.get(url)
    print(response)
    
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("", response.text), 'lxml')
    
    player_table = soup.find_all('table')[1]
    
    player_df = pd.read_html(str(player_table))[0]
    
    level_one = player_df.columns.get_level_values(0).astype(str)
    level_two = player_df.columns.get_level_values(1).astype(str)
    new_columns = level_one + "|" + level_two
    new_columns = [x.split("|")[1] if x[0:7] == 'Unnamed' else x for x in new_columns]
    new_columns
    player_df.columns = new_columns
    
    drop_indices = player_df[player_df['Player'] == 'Player'].index
    player_df.drop(drop_indices, inplace = True)
    
    return player_df


#### Example:
#
#   fbref_player_stats("https://fbref.com/en/comps/Big5/passing/players/Big-5-European-Leagues-Stats")


def fbref_squad_stats(url):
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import re
    
    response = requests.get(url)
    print(response)
    
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("", response.text), 'lxml')
    if url.split("/")[5] == 'Big5':
        squad_table = soup.find_all('table')[1]
    else:
        squad_table = soup.find_all('table')[0]
    
    squad_df = pd.read_html(str(squad_table))[0]
    
    level_one = squad_df.columns.get_level_values(0).astype(str)
    level_two = squad_df.columns.get_level_values(1).astype(str)
    new_columns = level_one + "|" + level_two
    new_columns = [x.split("|")[1] if x[0:7] == 'Unnamed' else x for x in new_columns]
    squad_df.columns = new_columns
    
    drop_indices = squad_df[squad_df['Squad'] == 'Squad'].index
    squad_df.drop(drop_indices, inplace = True)
    
    return squad_df

#### Example:
#
#   fbref_squad_stats("https://fbref.com/en/comps/Big5/defense/squads/Big-5-European-Leagues-Stats")


