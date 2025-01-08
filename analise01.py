from main import df_bank
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


""" HISTOGRAMA """
# Histograma
# plt.figure(figsize=(8, 5))
# sns.histplot(df_bank['age'], bins=20, kde=True, color='blue')
# plt.title('Distribuição de Idade dos Clientes')
# plt.xlabel('Idade')
# plt.ylabel('Frequência')
# plt.show()

""" BOXPLOT """
# # Boxplot para detectar outliers
# plt.figure(figsize=(8, 5))
# sns.boxplot(x=df_bank['age'], color='green')
# plt.title('Boxplot de idade')
# plt.xlabel('Idade')
# plt.show()

# # Criar faixas etárias
# bins = [0, 27, 39, 59, 100]
# labels = ['Adolescente', 'Adulto Jovem', 'Adulto', 'Idoso']
# df_bank['faixa_etaria'] = pd.cut(df_bank['age'], bins=bins, labels=labels, right=False)

# # Contagem por faixa etária
# faixa_etaria_counts = df_bank['faixa_etaria'].value_counts()
# print(faixa_etaria_counts)

# # Gráfico de barras para faixas etárias
# faixa_etaria_counts.plot(kind='bar', color='orange', figsize=(8, 5))
# plt.title('Distribuição por Faixa Etária')
# plt.xlabel('Faixa Etária')
# plt.ylabel('Frequência')
# plt.show()

""" CONTAGEM E PERCENTUAL DE CATEGORIAS """

""" CATEGORIA -----> JOB """

# job_counts = df_bank['job'].value_counts()
# job_percentual = df_bank['job'].value_counts(normalize=True) * 100
# print(job_counts)
# print(job_percentual)

# # Criando o gráfico de barras
# plt.figure(figsize=(10, 6))
# ax = sns.barplot(x=job_counts.values, y=job_counts.index, palette='coolwarm')

# # Adicionar rótulos nas barras
# for i, value in enumerate(job_counts.values):
#     plt.text(value + 1, i, str(value), va='center')  # `value + 1` posiciona o texto ligeiramente à direita
# plt.title('Distribuição de profissoes')
# plt.xlabel('Frequencia')
# plt.ylabel('Profissao')
# plt.show()

""" CATEGORIA -----> CONTATO """

# contato_counts = df_bank['contact'].value_counts()
# contato_percentual = df_bank['contact'].value_counts(normalize=True) * 100
# """ o normalize=True acima em vez de retornar os números absolutos
# ele vai retornar as proporções (frequência relativa) de cada valor em relação ao total"""

# print(contato_counts)
# print(contato_percentual)

# # Criando um gráfico de barras
# plt.figure(figsize=(10, 6))
# ax = sns.barplot(x=contato_counts.values, y=contato_counts.index, palette='coolwarm')

# # Adicionando rótulos nas barras
# for i, value in enumerate(contato_counts.values):
#     plt.text(value + 1, i, str(value), va='center')
    
# plt.title('Distribuição de tipo de contato')
# plt.xlabel('Frequencia')
# plt.ylabel('Contato')
# plt.show()