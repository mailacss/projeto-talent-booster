from flask import jsonify
import pandas as pd

def item7():
    data = pd.read_csv('dadosvoos_2007.csv')
    meses = data['Month'].unique()
    dias = data['DayofMonth'].unique()
    print('importado')
    mediasMeses = {}
    mediasDias = {}

    for i in meses: #medias por mes
        result0 = data[data['Month']==i]
        result1 = result0[result0['WeatherDelay']>0]
        media = (result1['WeatherDelay'].sum())/len(result0)
        mediasMeses.update({str(i):(float ("{0:.3f}".format(media)))})

    for i in dias: #medias por dia do mes
        result0 = data[data['DayofMonth']==i]
        result1 = result0[result0['WeatherDelay']>0]
        media = (result1['WeatherDelay'].sum())/len(result0)
        mediasDias.update({str(i):(float ("{0:.3f}".format(media)))})

    dictgeral = {"mediaDeAtrasosPorMes":mediasMeses,"mediaDeAtrasosPorDiaDoMes":mediasDias}

    return jsonify(dictgeral)