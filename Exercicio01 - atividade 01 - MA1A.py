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

produto = str(input("Consultar o valor de: "))
valor(produto)
