notas = input().split()

notas_transformadas = []

for item in notas:
    item = int(item)
    notas_transformadas.append(item)

soma_geral = sum(notas_transformadas)
media_aritmetica = soma_geral / 4

if media_aritmetica >= 5:
    print(media_aritmetica, " Parabéns, você passou de ano!")
else:
    print(media_aritmetica, " Que pena, você reprovou!")