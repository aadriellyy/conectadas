gasto = {
    "descricao": "Mercado",
    "valor": 152.30,
    "categoria": "Alimentação"
}

print(gasto["valor"])

gastos = [gasto]
for chave in gastos:
    print(chave["descricao"], chave["valor"])