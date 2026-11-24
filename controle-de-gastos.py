descricoes = []
valores = []

#enquanto for verdadeiro
while True:
    print("\n1 - Cadastrar   2 - Listar   3 - Total   0 - Sair")
    opcao = input("Escolha uma opção: ")

    #O que vai acontecer se ele escolher a opção 1?
    if opcao == "1":
        descricoes.append(input("Descrição: "))
        valor = float(input("Digite um valor para o gasto: "))
        valores.append(valor)

    #Ele nao quer cadastrar, será se quer listar?
    elif opcao == "2":
        for i in range(len(descricoes)):
            print(f"{i + 1},  {descricoes[i]} - {valores[i]}")

    #Se ele nao quiser nem cadastrar nem listar, ele pode querer ver o total
    elif opcao == "3":
        print(f"Total = {sum(valores)}")

    #Queremos checar se é a opção 0
    elif opcao == "0":
        print("Obrigada por usar o nosso programa")
        break


    
