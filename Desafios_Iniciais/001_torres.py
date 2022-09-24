# input para receber vários valores em apenas uma linha
distancia, d1, d2 = map(float, input().split())
# Cálculo do ICM
icm = distancia/(d1+d2)
# Formatando resultado para duas casas decimais
print("%.2f" % icm)
