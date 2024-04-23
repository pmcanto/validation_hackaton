import pandas as pd
import json
import os
import re

# Carregar o arquivo csv
try:
    df = pd.read_csv(r'Baseparateste1.csv', sep=';')
except FileNotFoundError:
    print("Arquivo 'Baseparateste.csv' não encontrado.")
    exit()

# Exibir os cabeçalhos
print(df.columns.tolist())

# Verificar cabeçalhos das colunas
expected_headers = ['ID', 'Nome', 'PastaOrigem', 'PastaDestino', 'PastaBackup']
missing_headers = [col for col in expected_headers if col not in df.columns]
if missing_headers:
    print(f"Cabeçalhos das colunas faltando: {', '.join(missing_headers)}")
    exit()

# Reordenar as colunas para a ordem esperada
df = df[expected_headers]

# Verificar tipos de dados
if not df['ID'].apply(lambda x: isinstance(x, int)).all():
    print("A coluna 'ID' contém valores não inteiros.")
    exit()

if not df['Nome'].apply(lambda x: isinstance(x, str)).all():
    print("A coluna 'Nome' contém valores não string.")
    exit()

# Verificar formato dos endereços dos arquivos
path_pattern = r'^[a-zA-Z]:\\'
for col in ['PastaOrigem', 'PastaDestino', 'PastaBackup']:
    df[col] = df[col].apply(lambda x: x if re.match(path_pattern, str(x)) else None)

# Criar um dicionário para armazenar a estrutura de árvore
tree = {"children": []}

# Função para adicionar um nó à árvore
def add_node(parent, node):
    for child in parent['children']:
        if child['name'] == node:
            return child
    new_child = {"name": node, "children": []}
    parent['children'].append(new_child)
    return new_child

# Adicionar todos os nós à árvore
for _, row in df.iterrows():
    parent_node = add_node(tree, row['PastaOrigem'])
    add_node(parent_node, row['PastaDestino'])

# Salvar a árvore como json
with open('Baseparateste.json', 'w') as f:
    json.dump(tree, f)

print("Arquivo 'Baseparateste.json' salvo com sucesso.")
import pandas as pd
import json
import os
import re

# Carregar o arquivo csv
try:
    df = pd.read_csv(r'Baseparateste1.csv', sep=';')
except FileNotFoundError:
    print("Arquivo 'Baseparateste.csv' não encontrado.")
    exit()

# Exibir os cabeçalhos
print(df.columns.tolist())

# Verificar cabeçalhos das colunas
expected_headers = ['ID', 'Nome', 'PastaOrigem', 'PastaDestino', 'PastaBackup']
missing_headers = [col for col in expected_headers if col not in df.columns]
if missing_headers:
    print(f"Cabeçalhos das colunas faltando: {', '.join(missing_headers)}")
    exit()

# Reordenar as colunas para a ordem esperada
df = df[expected_headers]

# Verificar tipos de dados
if not df['ID'].apply(lambda x: isinstance(x, int)).all():
    print("A coluna 'ID' contém valores não inteiros.")
    exit()

if not df['Nome'].apply(lambda x: isinstance(x, str)).all():
    print("A coluna 'Nome' contém valores não string.")
    exit()

# Verificar formato dos endereços dos arquivos
path_pattern = r'^[a-zA-Z]:\\'
for col in ['PastaOrigem', 'PastaDestino', 'PastaBackup']:
    df[col] = df[col].apply(lambda x: x if re.match(path_pattern, str(x)) else None)

# Criar um dicionário para armazenar a estrutura de árvore
tree = {"children": []}

# Função para adicionar um nó à árvore
def add_node(parent, node):
    for child in parent['children']:
        if child['name'] == node:
            return child
    new_child = {"name": node, "children": []}
    parent['children'].append(new_child)
    return new_child

# Adicionar todos os nós à árvore
for _, row in df.iterrows():
    parent_node = add_node(tree, row['PastaOrigem'])
    add_node(parent_node, row['PastaDestino'])

# Salvar a árvore como json
with open('Baseparateste.json', 'w') as f:
    json.dump(tree, f)

print("Arquivo 'Baseparateste.json' salvo com sucesso.")
