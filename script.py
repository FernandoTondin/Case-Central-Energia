import pandas as pd
import numpy as np
from datetime import datetime
import requests


def valorDolar(dia=1, mes=1, ano=2001):
    strmes = str(mes).zfill(2)
    strdia = str(dia).zfill(2)
    strano = str(ano).zfill(4)

    requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='"+strmes+"-"+strdia+"-"+strano+"'&$top=1&$format=json")

    cotacao = requisicao.json()

    while cotacao["value"]==[]:
        dia = dia - 1

        if dia < 1:
            mes = mes - 1
            if mes < 1:
                ano = ano - 1
                mes = 12
            
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dia = 31
            elif mes == 4 or mes == 6 or mes == 9 or mes == 10:
                dia = 30
            elif ano%400 == 0 or (ano%4 == 0 and ano%100!=0):
                dia = 29
            else:
                dia = 28

        strmes = str(mes).zfill(2)
        strdia = str(dia).zfill(2)
        strano = str(ano).zfill(4)

        print("refazendo requisição para a data: "+strdia+"/"+strmes+"/"+strano)
        requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='"+strmes+"-"+strdia+"-"+strano+"'&$top=1&$format=json")

        cotacao = requisicao.json()

    print(cotacao)
    print (cotacao["value"][0])
    cot = (cotacao["value"][0]["cotacaoCompra"]+cotacao["value"][0]["cotacaoVenda"])/2
    
    return cot

def strTodate(str):
    return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

def cotacaoDolar(str):
    data = strTodate(str)
    return valorDolar(dia=data.day,mes=data.month,ano=data.year)





df = pd.read_csv('termicas-nome_num_tipo_preco_pot.csv',sep=',')

num = df.drop_duplicates(subset="num",keep="last").groupby(["tipo_comb_"]).size().sort_values()       #dataset group com o numero de usinas para cada tipo de combustivel

potencias = df.drop_duplicates(subset="num",keep="last").groupby(["tipo_comb_"]).sum().sort_values(by="pot",ascending=False) #dataframe com a soma das potencias instaladas por tipo de combustivel em ordem decrescente.


combustiveis = []

for i in range(0,3):
    combustiveis.append(potencias.iloc[i].name)

print(combustiveis)
usinas = {}

for i in combustiveis:
    lista = []
    for j in range(0,3):
        lista.append(df.loc[df["tipo_comb_"]==i].drop_duplicates(subset="num",keep="last").sort_values(by="pot",ascending=False).iloc[j]["num"])
    usinas[i] = lista

print(usinas)


#df.to_csv(path_or_buf="teste.csv")