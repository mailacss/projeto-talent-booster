from flask import jsonify
import pandas as pd

def item2():
    data = pd.read_csv('dadosvoos_2007-x2.csv')
    origem = data['Origin'].unique()
    destino = data['Dest'].unique()
    print('importado')
    mediasAtrasoPartida = {}
    mediasAtrasoChegada = {}

    for i in origem: #atraso na partida
        result = data[data['Origin']==i]
        media = (result['DepDelay'].sum())/len(result)
        mediasAtrasoPartida.update({i: (float("{0:.2f}".format(media)))})

    for i in destino: #atraso na chegada
        result = data[data['Dest']==i]
        media = (result['ArrDelay'].sum())/len(result)
        mediasAtrasoChegada.update({i: (float("{0:.2f}".format(media)))})

    dictgeral = {"mediasAtrasoPartida":mediasAtrasoPartida,"mediasAtrasoChegada":mediasAtrasoChegada}

    return (jsonify(dictgeral))