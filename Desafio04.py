import pandas as pd

#fonte = 'https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true'
fonte = './MICRODADOS_ENEM_2019_SAMPLE_43278.csv'

dados = pd.read_csv(fonte)

#print(dados.head())
#print(dados.columns.values)

print(dados.query('IN_TREINEIRO == 0')['NU_IDADE'].hist())
