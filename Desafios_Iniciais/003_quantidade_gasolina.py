# input para receber vários valores em uma linha
tempo, velocidade = map(float, input().split())
# calculando a distância
distancia = tempo * velocidade
# calculando a quantidade de gasolina
quantidade_galosina = distancia / 12
# mostrando a quantidade de gasolina, formatando para três casas decimais
print("%.3f" % quantidade_galosina)
