#Julio Arath Rosales Oliden
#Oscar Miranda

def state(estado):
    """Convierte a la abreviación de los estados """
    try:
        lista_estados = open("estados.csv", "r+", encoding="UTF-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        for linea_estados in lista_estados:
            estados_sin_espacios = linea_estados.rstrip()
            estados_lista = estados_sin_espacios.split(",")
            if estado==estados_lista[0]:
                return estados_lista[1]


def remove_space(linea):
    sin_espacios = linea.rstrip()
    lista = sin_espacios.split(",")
    return lista

def hospitales_estado(estado):
    try:
        archivo=open("pvc.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        try:
            subir = open("Hospitales_" + estado + ".csv", "w+", encoding="UTF-8")
        except IOError:
            print("No se puede abrir ó no se encuentra el archivo")
        else:
            subir.write(f"Nombre del hospital, Telefono \n")
            abreviado = state(estado)
            anterior=""
            for linea in archivo:
                lista =  remove_space(linea)
                subir_string = ""
                if lista[4] == abreviado and anterior != lista[1] :
                    #print(f"Nombre del hospital:{lista[1]}, Telefono:{lista[7]}")
                    subir_string += (f"{lista[1]},{lista[7]}" + "\n")
                    anterior = lista[1]
                subir.write(subir_string)
        subir.close()
    archivo.close()


estado="Alabama"
hospitales_estado(estado)
