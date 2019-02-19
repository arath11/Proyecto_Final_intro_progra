def remove_space(linea):
    sin_espacios = linea.rstrip()
    lista = sin_espacios.split(",")
    return lista

def comparacion_():
    try:
        archivo_comparacion = open("Hospitales_" + estado + ".csv", "r", encoding="UTF-8")
    except IOError:
        print("No se pudo abrir este arvhivo ")
    else:
        for fila in archivo_comparacion:
            comparcion=remove_space(fila)
            if not ("MARSHALL MEDICAL CENTER SOUTH" in comparcion[0]):
                print(comparcion[0])
        archivo_comparacion.close()


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


def afeccion_abreviado(afeccion):
    if afeccion == "ataque":
        return "Payment for heart attack patients"
    elif afeccion == "falla":
        return "Payment for heart failure patients"
    elif afeccion == "cadera":
        return "Payment for hip/knee replacement patients"
    elif afeccion == "neumonia":
        return "Payment for pneumonia patients"

def porcentaje_hospitales_a(afeccion):
    try:
        lista_estados = open("estados.csv", "r+", encoding="UTF-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        try:
            subir = open("nombre.csv", "w+", encoding="UTF-8")
        except IOError:
            print("No se puede abrir ó no se encuentra el archivo")
        else:
            enfermedad = afeccion_abreviado(afeccion)
            subir_string = ""
            subir.write(f"cabeza \n")
            for linea_estados in lista_estados:
                estados_sin_espacios = linea_estados.rstrip()
                estados_lista = estados_sin_espacios.split(",")
                cantidad_estados = 0
                cantidad = 0
                precio = 0
                try:
                    archivo = open("pvc.csv", "r", encoding="UTF-8")
                except IOError:
                    print("No se puede abrir ó no se encuentra el archivo")
                else:
                    for linea in archivo:
                        lista = remove_space(linea)
                        if lista[4] == estados_lista[1] and lista[8] == enfermedad and lista[
                            10] == "Greater than the National Average Payment":
                            cantidad += 1
                            cantidad_estados += 1
                        elif lista[4] == estados_lista[1] and lista[8] == enfermedad:
                            cantidad_estados += 1
                    total = cantidad / cantidad_estados * 100
                    if cantidad != 0:
                        subir_string += (f"{estados_lista[0]},{cantidad},{cantidad_estados},{total}\n")
                    else:
                        subir_string += (f"{estados_lista[0]},0,0,0\n")
                    archivo.close()
            subir.write(subir_string)

        subir.close()

        lista_estados.close()

a="falla"
#neumonia, cadera, ataque, falla
porcentaje_hospitales_a(a)