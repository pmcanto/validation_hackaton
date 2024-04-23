import pandas as pd
import json
import os
import re

# Carregar o arquivo csv
try:
    df = pd.read_csv(r'C:\Users\Pedro\Desktop\verificar\Baseparateste.csv', sep=';')
except FileNotFoundError:
    print("Arquivo 'Baseparateste.csv' não encontrado.")
    exit()

# Exibir os cabeçalhos
print(df.columns.tolist())

# Verificar cabeçalhos das colunas
expected_headers = ['ID', 'Nome', 'PastaOrigem', 'PastaDestino', 'PastaBackup']
if list(df.columns) != expected_headers:
    print("Cabeçalhos das colunas não correspondem ao esperado.")
    exit()

# Verificar tipos de dados
if not df['ID'].apply(lambda x: isinstance(x, int)).all():
    print("A coluna 'ID' contém valores não inteiros.")
    exit()

if not df['Nome'].apply(lambda x: isinstance(x, str)).all():
    print("A coluna 'Nome' contém valores não string.")
    exit()

# Verificar formato dos endereços dos arquivos
path_pattern = r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$'
for col in ['PastaOrigem', 'PastaDestino', 'PastaBackup']:
    df[col] = df[col].apply(lambda x: x if re.match(path_pattern, str(x)) else None)

# Criar um novo DataFrame onde cada linha é duplicada para cada endereço único na coluna 'PastaDestino'
df = df.explode('PastaDestino')

# Salvar como json
df.to_json('Baseparateste.json', orient='records')
print("Arquivo 'Baseparateste.json' salvo com sucesso.")
