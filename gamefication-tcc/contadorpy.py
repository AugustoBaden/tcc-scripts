#para definir o interpertador como python 3 "#! python"
#para definir o interpertador como python2.7 nesse sistema "#! python2"

import csv
import pandas as pd
import time

from datetime import date, timedelta
today = date.today()
diaUsado = today.strftime('%Y%m%d')
print(diaUsado)
print("logs_"+diaUsado)
diaInt = int(diaUsado)
diaLa = str(diaInt)
print(diaLa)

with open("logs_"+diaLa+ ".csv", 'r',  encoding='utf-8') as logs:
    ler = pd.read_csv(logs)
    ler["junto"] = ler["NomeCompleto"] + "," + ler["ContextoEvento"]
    ler["junto"].to_csv(r"concat.csv", header=["NomeCompleto"])

data = pd.read_csv("concat.csv")
duplicador = data.pivot_table(index=["NomeCompleto"], aggfunc = "size")
duplicador.to_csv(r"logsCalculado"+diaLa+".csv", header=["ContextoEvento,Quantidade"], sep = ",", quotechar = " ")

time.sleep(3)

import shutil



