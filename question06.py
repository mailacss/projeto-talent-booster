from flask import jsonify
import pandas as pd

def item6():
    data = pd.read_csv('dadosvoos_2007-x2.csv')
    avioes = data['TailNum'].unique()
    voosPorAeronave = {"VoosPorAeronave":{}}

    for i in avioes:
        result = len(data[data['TailNum']==i])
        voosPorAeronave["VoosPorAeronave"][i] = result

    return jsonify(voosPorAeronave)