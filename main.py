import pandas as pd

df_bank = pd.read_csv(r'C:\Users\rpani\workspace\p_datasci\01_bank\dados\UCI_ML_Bank.csv', sep=';',encoding='latin1')


if __name__ == "__main__":
    
    # # Verificando estrutura da base
    # print(df_bank.head())

    # # Tipos de dados
    # print(df_bank.dtypes)

    # # Informações dos dados
    # print(df_bank.info())

    # # Quantidade de linhas e colunas
    # print(df_bank.shape)

    # # Nomes das colunas
    # print(df_bank.columns)

    # # Quantidade de valores nulos
    # print(df_bank.isnull().sum())

    # # Verificando detalhes de uma coluna específica
    # print(df_bank['age'].describe())
    
    # # Valores únicos de idade
    # print(f'Valores únicos de idade: {df_bank['age'].nunique()}')

    # Valores únicos de profissão
    # print(f'Valores únicos de profissão: {df_bank['job'].nunique()}')

    print(df_bank.columns)

