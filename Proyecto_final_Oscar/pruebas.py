def prueba(estado):
    try:
        lista_estados = open("estados.csv", "r+", encoding="UTF-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        for linea_estados in lista_estados:
            estados_sin_espacios = linea_estados.rstrip()
            estados_lista = estados_sin_espacios.split(",")
            if estado==estados_lista[0]:
                print(estados_lista[1])

a="California"
prueba(a)