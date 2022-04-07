import pandas as pd
uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv'
pd.read_csv(uri)
print(pd.read_csv(uri))

y = 1 if 1 > 0 else 0
