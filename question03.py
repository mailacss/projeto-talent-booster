import pandas as pd
from flask import jsonify

def item3():
    df = pd.read_csv('dadosvoos_2007-x2.csv')
    grupo = df.groupby(['Origin'])
    grupo.groups.keys()

    df['Origin'].unique()

    '''grp = grupo.get_group('SM', grupo)
    
    grp = grupo.get_group('BET')
    '''
    grupo = df.groupby(['Origin', 'Dest']).count()

    print(grupo)
    return (grupo)