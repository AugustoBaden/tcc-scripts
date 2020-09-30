import csv
import codecs
import pandas as pd
import tempfile
import shutil
from tempfile import NamedTemporaryFile
import time


import fnmatch
import os

from datetime import date, timedelta
today = date.today()
diaUsado = today.strftime('%Y%m%d')
# print(diaUsado)
print("logs_"+diaUsado)
diaInt = int(diaUsado)
diaLa = str(diaInt)
# print(diaLa)

for NomeRelatorio in os.listdir(r'C:\Users\home\Downloads'):
    if fnmatch.fnmatch(NomeRelatorio, "logs_"+diaLa+"*.csv"):
        print(NomeRelatorio)
        a = NomeRelatorio


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files before in %r: %s" % (cwd, files))
print(a)
# time.sleep(5)
shutil.move("C:/Users/home/Downloads/"+a,
            "C:/Users/home/OneDrive/projetosUninta/gamefication/"+a)

time.sleep(5)
# cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
#print("Files after in %r: %s" % (cwd, files))

with open(a, 'r',  encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # print("reeeeeee")
    with open('saiuPtBR2.csv', 'w', newline='', encoding='utf-8') as file:

        col = ["\ufeffHora", "Nome completo",
               "Contexto do Evento", "Nome do evento"]
        writer = csv.DictWriter(file, fieldnames=col)

        headers = "Hora,NomeCompleto,ContextoEvento,NomeEvento\n"
        file.write(headers)

        # removendo colunas indesejadas
        for line in reader:
            del line['Usuário afetado']
            del line['Componente']
            del line['Descrição']
            del line['Origem']
            del line['endereço IP']
            writer.writerow(line)
# time.sleep(9)

takeThis = ["Webservice User", "-", 'TUTOR CF', 'TUTOR - DD', "TUTORIA INTA", "Tutora LK",
            'Tutor - FD', 'TUTOR - FM', 'TUTORA EAD - SM', 'TUTORA EAD -  PP', 'TUTOR EAD - UM']

with open('saiuPtBR2.csv', 'r',  encoding='utf-8') as infile, open('saiuPtBR3.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    for line in csv.reader(infile, delimiter=','):
        if not any(takeThis in line for takeThis in takeThis):
            writer.writerow(line)

# pandas was used to correct some lines
keepThis = ["Base de dado Contribua com um documento", "Diário: Bloco de Notas,Fórum – Café Virtual",
            "Fórum Temático", "Fórum: Fórum Partilhando ideias", "Questionário: Simulado", "Sistema"]


time.sleep(2)
# usando pandas para renomear os contextos do evento


filename = 'saiuPtBR3.csv'
filenameout = 'saiuPtBR.csv'


data = pd.read_csv(filename)

data["ContextoEvento"] = data["ContextoEvento"].replace(
    "Fórum: Fórum - Café Virtual", "Fórum - Café Virtual")


# metodo que localiza e substitui baseado em string parcial no tocante a questionario: simulado

data.loc[data['ContextoEvento'].str.contains(
    'questionário: simulado', case=False), 'ContextoEvento'] = "Questionário: Simulado"
data.loc[data['ContextoEvento'].str.contains(
    'Diário: Bloco de notas', case=False), 'ContextoEvento'] = "Diário: Bloco de Notas"
data.loc[data['ContextoEvento'].str.contains(
    'Fórum: FÓRUM TEMÁTICO', case=False), 'ContextoEvento'] = "Fórum Temático"
data.loc[data['ContextoEvento'].str.contains(
    'Fórum: FÓRUM TEMÁTICa', case=False), 'ContextoEvento'] = "Fórum Temático"
data.loc[data['ContextoEvento'].str.contains(
    'Fórum: FÓRUM  TEMÁTICO', case=False), 'ContextoEvento'] = "Fórum Temático"
data.loc[data['ContextoEvento'].str.contains(
    'Fórum: FÓRUM de TEMÁTICO', case=False), 'ContextoEvento'] = "Fórum Temático"
data.loc[data['ContextoEvento'].str.contains(
    'Fórum: Partilhando ideias', case=False), 'ContextoEvento'] = "Fórum: Partilhando ideias"
data.loc[data['ContextoEvento'].str.contains('Tarefa: Enviar relato de experiência de utilização profissional de algum recurso do Ecossistema de Aprendizagem AIAMIS',
                                             case=False), 'ContextoEvento'] = "Tarefa: Enviar relato de experiência de utilização profissional"
data.loc[data['ContextoEvento'].str.contains('Tarefa: Envio de atividade realizada da webconferência',
                                             case=False), 'ContextoEvento'] = "Tarefa: Envio de atividade na webconferência"

data.to_csv(
    r"C:\Users\home\OneDrive\projetosUninta\gamefication\saiuPtBR2.csv", index=False)


filename = 'saiuPtBR2.csv'

data = pd.read_csv(filename)

# pandas called in itself to selfload with the isin "method"
# mantem linhas q interessam em contexto do evento
CE = data[data['ContextoEvento'].isin(["Base de dados: Contribua com um documento", "Diário: Bloco de Notas", "Fórum - Café Virtual", "Fórum Temático", "Fórum: Partilhando ideias", "Questionário: Simulado", "Sistema",
                                       "Tarefa: Enviar relato de experiência de utilização profissional", "Tarefa: Envio de certificado de realização de curso livre", "Tarefa: Envio de resumo de palestra online", "Tarefa: Envio de atividade na webconferência"])]
# mantem linhas q interessam em nome do evento após a filtragem de contexto do evento feita anteriormente
NE = CE[CE['NomeEvento'].isin(['Algum conteúdo foi publicado.', 'Journal entry created', 'Mensagem enviada',
                               "Registro criado", "Tentativa do questionário iniciada", "Um arquivo foi enviado."])]


# CHECAR A PASTA EM Q SERA SALVA E SEU NOME

NE.to_csv(r"C:\Users\home\OneDrive\projetosUninta\gamefication\logs_" +
          diaLa+".csv", index=False)
print("it´s over, Anakin")


# remover eventos que nao interessam
