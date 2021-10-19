import pandas as pd
import json

# Qual a concentração de voos por aeroporto?
# voos cancelados ( Origin = aeroporto de origem )
# voos realizados ( Origin = aeroporto de origem)
# voos cancelados ( Dest = aeroporto de destino)
# voos realizados ( Dest = aeroporto de destino)

# Cancelled = status de cancelamento

df = pd.read_csv("dadosvoos_2007-x2.csv")

voos_Cancelled = df.groupby(['Cancelled'])
voos_Cancelled_true = voos_Cancelled.get_group(1)
voos_Cancelled_false = voos_Cancelled.get_group(0)

voos_Cancelled_True_Origin = voos_Cancelled_true.groupby(['Origin'])[
    ['Cancelled']].count()

voos_Cancelled_True_Dest = voos_Cancelled_true.groupby(['Dest'])[
    ['Cancelled']].count()

voos_Cancelled_False_Origin = voos_Cancelled_false.groupby(['Origin'])[
    ['Cancelled']].count()

voos_Cancelled_False_Dest = voos_Cancelled_false.groupby(['Dest'])[
    ['Cancelled']].count()

voos_Cancelled_True_Origin_json = voos_Cancelled_True_Origin.to_json(
    orient='table')
voos_Cancelled_True_Origin_parsed = json.loads(voos_Cancelled_True_Origin_json)

voos_Cancelled_True_Dest_json = voos_Cancelled_True_Dest.to_json(
    orient='table')
voos_Cancelled_True_Dest_parsed = json.loads(voos_Cancelled_True_Dest_json)

voos_Cancelled_False_Origin_json = voos_Cancelled_False_Origin.to_json(
    orient='table')
voos_Cancelled_False_Origin_parsed = json.loads(
    voos_Cancelled_False_Origin_json)

voos_Cancelled_False_Dest_json = voos_Cancelled_False_Dest.to_json(
    orient='table')
voos_Cancelled_False_Dest_parsed = json.loads(voos_Cancelled_False_Dest_json)

resultado04 = {
    "voos_Cancelled_True_Origin": voos_Cancelled_True_Origin_parsed,
    "voos_Cancelled_True_Dest": voos_Cancelled_True_Dest_parsed,
    "voos_Cancelled_False_Origin": voos_Cancelled_False_Origin_parsed,
    "voos_Cancelled_False_Dest": voos_Cancelled_False_Dest_parsed
}
