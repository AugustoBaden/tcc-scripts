import csv
import pymysql
import pandas as pd
import sys
import os
import time

from datetime import date, timedelta
today = date.today()
diaUsado = today.strftime('%Y%m%d')
print(diaUsado)
print("logs_"+diaUsado)
diaInt = int(diaUsado)
diaLa = str(diaInt)
print(diaLa)
with open("logs_" + diaLa + ".csv","r",  encoding = 'utf-8') as logs:
    ler = pd.read_csv(logs)
    ler["junto"] = ler["NomeCompleto"] + "," + ler["ContextoEvento"]
    ler["junto"].to_csv(r"concat.csv", header=["NomeCompleto"])

#Calcula pontos por atividade realizada
data = pd.read_csv("concat.csv")
duplicador = data.pivot_table(index=["NomeCompleto"], aggfunc = "size")
duplicador.to_csv(r"logsCalculado"+diaLa+".csv", header=["ContextoEvento,Quantidade"], sep = ",", quotechar = " ")

#data2 = pd.read_csv("logs_"+diaLa+ ".csv")
#data["Hora"]= data["Hora"].str.split(" ", n = 1, expand = True)
time.sleep(3)




#Renomeia os arquivos tratados para logs.csv e calculado.csv
for nome in os.listdir('.'):
    if (nome == "logs_" + diaLa + ".csv"):
        os.rename("logs_" + diaLa + ".csv", "logs.csv")
    elif (nome == "logsCalculado" + diaLa + ".csv"):
        os.rename("logsCalculado" + diaLa + ".csv", "calculado.csv")
print("Arquivos renomeados com sucesso!!!")

#Insere as tabelas no Banco de Dados importação_contador
def csv_to_mysql(load_sql1, load_sql2,host):
    '''
    Esta função transfere informações de uma tabela no formato CSV para SQL de acordo com a variável load_sql
    '''
    try:
        con = pymysql.connect(host='host',
                              port=3306,
                              user='usuario',
                              password='****',
                              db='nome banco',
                              autocommit=True,
                              local_infile=1,
                              cursorclass=pymysql.cursors.DictCursor)
        print('Conectando ao Banco de Dados: {}'.format(host))
        cursor = con.cursor()
        cursor.execute(load_sql1)
        print('Sucesso na transferência para a tabela relat_tratados.')
        cursor.execute(load_sql2)
        print('Sucesso na transferência para a tabela contador.')
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


# Execution Example

load_sql1 = "LOAD DATA LOCAL INFILE 'logs.csv' INTO TABLE relat_tratados CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' ignore 1 lines;"
load_sql2 = "LOAD DATA LOCAL INFILE 'calculado.csv' INTO TABLE contador CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' ignore 1 lines;"
host = 'host'

csv_to_mysql(load_sql1, load_sql2, host)

time.sleep(3)
print("time to kill this buckos: calculado.csv,logs.csv")
for nome in os.listdir('.'):
    if (nome == "logs.csv"):
        os.rename("logs.csv", "logs_"+diaLa+".csv")
    elif (nome == "calculado.csv"):
        os.rename("calculado.csv", "logsCalculado"+diaLa+".csv")
print("Arquivos renomeados com sucesso!!!")

time.sleep(5)
    os.remove("logs"+diaLa+".csv")