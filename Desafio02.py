import pandas as pd

fonte = './MICRODADOS_ENEM_2019_SAMPLE_43278.csv'

dados = pd.read_csv(fonte)

# Desafio02 - Descobrir de Quais estados são os Inscritos de 13 Anos.
#inscritosTrezeAnosPorUF = dados.loc[(dados['NU_IDADE'] == 13),['NU_IDADE','SG_UF_RESIDENCIA']]
inscritosTrezeAnosPorUF = dados.query('NU_IDADE == 13')[['NU_IDADE','SG_UF_RESIDENCIA']]
print(inscritosTrezeAnosPorUF)
