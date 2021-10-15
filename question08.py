from flask import jsonify
import pandas as pd

def item8():
    data = pd.read_csv('dadosvoos_2007-x2.csv')
    origens = data['Origin'].unique()
    destinos = data['Dest'].unique()
    print('importado')
    mediasEmbarque = {}
    mediasDesembarque = {}

    for i in origens: #medias de embarque
        result = data[data['Origin']==i]
        media = (result['TaxiIn'].sum())/len(result)
        mediasEmbarque.update({i: (float("{0:.2f}".format(media)))})

    for i in destinos: #medias de desembarque
        result = data[data['Dest']==i]
        media = (result['TaxiOut'].sum())/len(result)
        mediasDesembarque.update({i: (float("{0:.2f}".format(media)))})

    print('medias ok')

    dictEmbarque = {"maiorMediaEmbarque":{},"menorMediaEmbarque":{}}
    dictDesembarque = {"maiorMediaDesembarque":{},"menorMediaDesembarque":{}}
    dictgeral = {"tempoDeDesembarque":dictDesembarque,"tempoDeEmbarque":dictEmbarque}

    #ESSAS 4 ESTRUTURAS PRECISAM PEGAR 10 PRIMEIROS E 10 ÚLTIMOS VALORES DO MEDIAS
    cont = 0
    for i in sorted(mediasEmbarque, key=mediasEmbarque.get, reverse=True): #maiorMediaEmbarque
        dictEmbarque["maiorMediaEmbarque"][i] = mediasEmbarque[i]
        cont += 1
        if cont == 10:
            break

    cont = 0
    for i in sorted(mediasEmbarque, key = mediasEmbarque.get): #menorMediaEmbarque
        dictEmbarque["menorMediaEmbarque"][i] = mediasEmbarque[i]
        cont += 1
        if cont == 10:
            break

    cont = 0
    for i in sorted(mediasDesembarque, key = mediasDesembarque.get, reverse=True): #maiorMediaDesembarque
        dictDesembarque["maiorMediaDesembarque"][i] = mediasDesembarque[i]
        cont += 1
        if cont == 10:
            break

    cont = 0
    for i in sorted(mediasDesembarque, key = mediasDesembarque.get): #menorMediaDesembarque
        dictDesembarque["menorMediaDesembarque"][i] = mediasDesembarque[i]
        cont += 1
        if cont == 10:
            break
    print('separados')

    listafinal = [dictgeral]
    print(jsonify(listafinal))
    return (jsonify(listafinal))