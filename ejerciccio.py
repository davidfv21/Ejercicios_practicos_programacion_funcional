def lista_arbol(arbol, lista):
    if lista == []:
        return arbol
    return lista_arbol(insertar(arbol, lista[0]), lista[1:])
    
