# input para receber vários valores em apenas uma linha
cachorro_quente, participantes = map(float, input().split())
# cálculo do número médio de cachorros quentes consumidos
media = cachorro_quente/participantes
# Formatando resultado para duas casas decimais
print("%.2f" % media)
