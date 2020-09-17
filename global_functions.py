def check_for_nickName(_nickName):
    champ_Nicknames = {
    'mf': 'Miss Fortune', 
    'bambi' : 'Lillia',
    'electric bear' : 'Volibear',
    'alligator' : 'Renekton'
    }   
    if _nickName in champ_Nicknames:
        return champ_Nicknames[_nickName]

    return _nickName

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct


def fix_playerName(_playerName):
    playerNames = {
    'Broken_Blade': 'Broken Blade', 
    'BrokenBlade': 'Broken Blade', 
    }   
    if _playerName in playerNames:
        return playerNames[_playerName]

    return _playerName