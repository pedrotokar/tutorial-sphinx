from src import cria_dados, manipula_dados

dado = cria_dados.transforma_em_serie({"IV": 9})
print(manipula_dados.manipula_serie(dado))
