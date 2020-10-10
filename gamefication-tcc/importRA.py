import csv
import pymysql
import pandas as pd
import sys
import os
import time
import codecs
from datetime import date, timedelta


#É NECESSARIO LEMBRAR DE CONVERTER ANTES DE EDITAR QLQER COISA 

time.sleep(3)





print('manda pro server')
def csv_to_mysql_server(load_sql1,host):
    '''
    Esta função transfere informações de uma tabela no formato CSV para SQL de acordo com a variável load_sql
    '''
    try:
        con = pymysql.connect(host='142.93.244.120',
                              port=3306,
                              user='acm',
                              password='mtc@acm@lggs2019',
                              db='db_game',
                              autocommit=True,
                              local_infile=1,
                              cursorclass=pymysql.cursors.DictCursor)
        print('Conectando ao Banco de Dados: {}'.format(host))
        cursor = con.cursor()
        cursor.execute(load_sql1)
        print('Sucesso na transferência para a tabela matriculado.')
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


# Execution Example

load_sql1 = "LOAD DATA LOCAL INFILE 'Dados2020a.csv' INTO TABLE matriculado CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' ignore 1 lines;"
host = '142.93.244.120'

csv_to_mysql_server(load_sql1, host)