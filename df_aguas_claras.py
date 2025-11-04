import pandas as pd
file = "wp_mapa_problemas.csv"
df = pd.read_csv(file, encoding='ISO-8859-1', delimiter=';')
df.head()
df["tipo"].unique()
df.columns
cols=['tipo', 'email', 'telefone',
       'autorizacao', 'status',  'data_envio',
       'resposta_texto',  'bairro']
df=df[cols]
df["resposta_texto"] = df["resposta_texto"].fillna("Não Respondido")
df.groupby(['tipo'])["status"].count()


#Gráfico de pizza

import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo
file = "wp_mapa_problemas.csv"
df = pd.read_csv(file, encoding='ISO-8859-1', delimiter=';')

# Selecionando e limpando as colunas
cols = ['tipo', 'email', 'telefone', 'autorizacao', 'status', 'data_envio', 'resposta_texto', 'bairro']
df = df[cols]
df["resposta_texto"] = df["resposta_texto"].fillna("Não Respondido")

# Agrupando os dados por tipo
tipo_counts = df.groupby(['tipo'])["status"].count()

# Criando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(tipo_counts, labels=tipo_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
plt.title("Distribuição de Problemas por Tipo")
plt.axis('equal')  # Deixa o gráfico circular
plt.show()



#Gráfico de barras

import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo
file = "wp_mapa_problemas.csv"
df = pd.read_csv(file, encoding='ISO-8859-1', delimiter=';')

# Selecionando e limpando as colunas
cols = ['tipo', 'email', 'telefone', 'autorizacao', 'status', 'data_envio', 'resposta_texto', 'bairro']
df = df[cols]
df["resposta_texto"] = df["resposta_texto"].fillna("Não Respondido")
# Agrupando os dados por tipo
tipo_counts = df.groupby(['tipo'])["status"].count().sort_values(ascending=False)

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(tipo_counts.index, tipo_counts.values, color='skyblue', edgecolor='black')

# Adicionando rótulos de valor acima das barras
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=9)

# Personalizando o gráfico
plt.title("Quantidade de Problemas por Tipo", fontsize=14)
plt.xlabel("Tipo de Problema")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Exibindo o gráfico
plt.show()
