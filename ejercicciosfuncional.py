def ultimodigitos(lista):
    if lista == []:
        return ""
    return str(lista[0])[-1] + ultimodigitos(lista[1:])

print(int(ultimodigitos([253,1997,28,333,917])))
