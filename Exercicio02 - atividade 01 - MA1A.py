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
    print(clientes[i], " - ", pedidos[i])
