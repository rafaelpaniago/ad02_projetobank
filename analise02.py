import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from main import df_bank
from analise01 import faixa_etaria_counts


# # Criar tabela de contingência
# contingencia = pd.crosstab(df_bank['contact'], df_bank['poutcome'], normalize='index') * 100

# # Exibir tabela de contingência
# print(contingencia)

# # Visualizar com gráfico de barras empilhadas
# contingencia.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
# plt.title('Distribuição do Resultado da Campanha por Forma de Contato')
# plt.ylabel('Percentual (%)')
# plt.xlabel('Forma de Contato')
# plt.legend(title='Resultado da Campanha')
# plt.show()


print(faixa_etaria_counts.head())