import pandas as pd


#fonte = 'https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true'
fonte = './MICRODADOS_ENEM_2019_SAMPLE_43278.csv'

dados = pd.read_csv(fonte)

# Proporção (Porcentagem) dos por idade.
#print(dados.columns.values)

idadeInscritos = dados['NU_IDADE'].value_counts().sort_index()
totalInscritos = dados.shape[0]
proporcaoIdadeInscritos = round((idadeInscritos/totalInscritos)*100, 4).astype('str') + '%'
print(proporcaoIdadeInscritos)