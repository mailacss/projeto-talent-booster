import pandas as pd

# Qual o atraso médio por mês de todos os voos?
df = pd.read_csv("dadosvoos_2007-x2.csv")

# # uma tabela com todos os meses
month = df.groupby(['Month'])

months = []
dados = []

for i in range(1, 13):
    months.append(month.get_group(i))

for i in range(0, 12):
    sumArrDelay = months[i]['ArrDelay'].sum()
    mediaArrDelay = sumArrDelay / months[i].shape[0]

    sumDepDelay = months[i]['DepDelay'].sum()
    mediaDepDelay = sumDepDelay / months[i].shape[0]

    dados.append({"Month": i+1, "ArrDelay": mediaArrDelay,
                 "DepDelay": mediaDepDelay})

# print(months)

resultado = {
    "result": dados
}
