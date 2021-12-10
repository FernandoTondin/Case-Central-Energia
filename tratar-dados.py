import pandas as pd
import json
from datetime import datetime
import requests
import investpy as inv


def strTodate(str):
    return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

def cotacaoDolar(string):
    data = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    dia=data.day
    mes=data.month
    ano=data.year

    strmes = str(mes).zfill(2)
    strdia = str(dia).zfill(2)
    strano = str(ano).zfill(4)
    strdata = strmes + "-" + strdia + "-" + strano

    requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='"+strdata+"'&$top=1&$format=json")

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
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                dia = 30
            elif ano%400 == 0 or (ano%4 == 0 and ano%100!=0):
                dia = 29
            else:
                dia = 28

        strmes = str(mes).zfill(2)
        strdia = str(dia).zfill(2)
        strano = str(ano).zfill(4)

        requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='"+strmes+"-"+strdia+"-"+strano+"'&$top=1&$format=json")

        cotacao = requisicao.json()
    cot = (cotacao["value"][0]["cotacaoCompra"]+cotacao["value"][0]["cotacaoVenda"])/2
    
    return cot

def precoPetroleo(string):
    data = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    dia = str(data.day).zfill(2)
    mes = str(data.month).zfill(2)
    ano = str(data.year).zfill(4)
    strdata = dia+"/"+mes+"/"+ano
    cotacao = json.loads(oleo)

    for i in cotacao["historical"]:
        if i["date"] == strdata:
            cot = i["open"] + i["high"] + i["low"] + i["close"]
            cot = cot / 4
            return cot

def precoGas(string):
    data = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    dia = str(data.day).zfill(2)
    mes = str(data.month).zfill(2)
    ano = str(data.year).zfill(4)
    strdata = dia+"/"+mes+"/"+ano
    cotacao = json.loads(gas)

    for i in cotacao["historical"]:
        if i["date"] == strdata:
            cot = i["open"] + i["high"] + i["low"] + i["close"]
            cot = cot / 4
            return cot

def precoCarvao(string):
    data = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    dia=1
    mes=data.month
    ano=data.year

    strdia = str(dia).zfill(2)
    strmes = str(mes).zfill(2)
    strano = str(ano).zfill(4)
    strdata = strano+"/"+strmes+"/"+strdia

    
    df = pd.read_excel("preco-carvao-mineral.xls")
    
    cotacao = df.loc[df["Month"] == strdata]

    while cotacao.empty:
        mes = mes - 1
        if mes < 1:
            ano = ano - 1
            mes = 12
        strmes = str(mes).zfill(2)
        strano = str(ano).zfill(4)
        strdata = strano+"/"+strmes+"/"+strdia
        cotacao = df.loc[df["Month"] == strdata]

    cot = cotacao["Price"]


df = pd.read_csv('termicas-nome_num_tipo_preco_pot.csv',sep=',')

potencias = df.drop_duplicates(subset="num",keep="last").groupby(["tipo_comb_"]).sum().sort_values(by="pot",ascending=False) #dataframe com a soma das potencias instaladas por tipo de combustivel em ordem decrescente.


combustiveis = []

for i in range(0,3):
    combustiveis.append(potencias.iloc[i].name)

usinas = {}

for i in combustiveis:
    lista = []
    for j in range(0,3):
        lista.append(df.loc[df["tipo_comb_"]==i].drop_duplicates(subset="num",keep="last").sort_values(by="pot",ascending=False).iloc[j]["num"])
    usinas[i] = lista

for i in usinas:
    for j in usinas[i]:
        custo = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["custo1"].to_frame()

        dias = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["date"]
        ini = strTodate(dias.min())
        strdia = str(ini.day).zfill(2)
        strmes = str(ini.month).zfill(2)
        strano = str(ini.year).zfill(4)
        strdataini = strdia+"/"+strmes+"/"+strano

        fim = strTodate(dias.max())
        strdia = str(fim.day).zfill(2)
        strmes = str(fim.month).zfill(2)
        strano = str(fim.year).zfill(4)
        strdatafim = strdia+"/"+strmes+"/"+strano

        oleo = inv.get_commodity_historical_data(commodity="Brent Oil",from_date=strdataini,to_date=strdatafim,order='descending',as_json=True)
        gas = inv.get_commodity_historical_data(commodity="Natural Gas",from_date=strdataini,to_date=strdatafim,order='descending',as_json=True)

        result = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["date"].apply(func=cotacaoDolar)
        custo.insert(loc=1,column="dolar",value=result)
        csv = "custo-usina-"+str(j)+"-"+i+"Xdolar.csv"
        custo.to_csv(path_or_buf=csv, index = False)
        custo = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["custo1"].to_frame()
        if i == "Oleo":
            result = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["date"].apply(func=precoPetroleo)
            custo.insert(loc=1,column="Petroleo",value=result)
            csv = "custo-usina-"+str(j)+"-"+i+"Xpetroleo.csv"
            custo.to_csv(path_or_buf=csv, index = False)
        elif i == "Gas":
            result = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["date"].apply(func=precoGas)
            custo.insert(loc=1,column="Gas natural",value=result)
            csv = "custo-usina-"+str(j)+"-"+i+"Xgas-natural.csv"
            custo.to_csv(path_or_buf=csv, index = False)
        elif i == "Carvao":
            result = df.loc[df["tipo_comb_"]==i].loc[df["num"]==j]["date"].apply(func=precoCarvao)
            custo.insert(loc=1,column="Carvao",value=result)
            csv = "custo-usina-"+str(j)+"-"+i+"Xcarvao-mineral.csv"
            custo.to_csv(path_or_buf=csv, index = False)



