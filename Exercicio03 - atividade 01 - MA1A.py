def valor(produto):
    if produto == "salgado":
        return(4.00)
    elif produto == "refrigerante":
        return(4.50)
    elif produto == "suco":
        return(5.00)
    elif produto == "sorvete":
        return(6.00)
    elif produto == "cafe":
        return(4.00)
    elif produto == "capuccino":
        return(6.00)
    elif produto == "bolo":
        return(4.50)
    elif produto == "dadinho":
        return(0.50)
    else:
        return("Este produto não foi encontrado")

clientes = []
pedidos = []
x = 1

while x < 8:
    nome = input("Próximo cliente: ")
    clientes.append(nome)
    pedido = input("Faça seu pedido: ")
    pedidos.append(pedido)
    x += 1

tam = len(clientes)
for i in range(0, tam):
    valores = valor(pedidos[i])
    print(clientes[i], pedidos[i], valores)

total = 0
for i in range(0, tam):
    valores = valor(pedidos[i])
    total += valores

print("\nValor final no caixa: ", total)
