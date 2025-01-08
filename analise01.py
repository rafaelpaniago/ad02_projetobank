from main import df_bank
import matplotlib.pyplot as plt
import seaborn as sns


# Histograma
plt.figure(figsize=(8, 5))
sns.histplot(df_bank['age'], bins=20, kde=True, color='blue')
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()