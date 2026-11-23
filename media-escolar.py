media = float(input())

# estruturas de decisao
# se a media for maior ou igual a 5, o aluno passou
if media >= 5:
    print("Parabéns, você passou de ano!")
# se a media for menor do que 5 mas maior do que 4, o aluno pode fazer a prova de recuperacao
elif media >= 4: 
    print("Você pode fazer a prova de recuperação.")
else:
    print("Que pena, tente no próximo ano!")