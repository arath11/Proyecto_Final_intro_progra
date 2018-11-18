def remove_space(linea):
    sin_espacios = linea.rstrip()
    lista = sin_espacios.split(",")
    return lista
estado="Alabama"

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

#estado="Alabama"
#hospitales_estado(estado)

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
            archivo = open("pvc.csv", "r", encoding="UTF-8")
        except IOError:
            print("No se puede abrir ó no se encuentra el archivo")
        else:
            try:
                subir = open("Estados" + "_" + afeccion + "_" + "mayor.csv", "w+", encoding="UTF-8")
            except IOError:
                print("No se puede abrir ó no se encuentra el archivo")
            else:
                enfermedad = afeccion_abreviado(afeccion)
                subir_string = ""
                for linea_estados in lista_estados:
                    estados_sin_espacios = linea_estados.rstrip()
                    estados_lista = estados_sin_espacios.split(",")
                    cantidad = 0
                    precio = 0
                    for linea in archivo:
                        lista = remove_space(linea)
                        if lista[4] == estados_lista[1] and lista[8] == enfermedad and lista[12] not in "Not Available ":
                            cantidad += 1
                            precio += float(lista[12])
                            print(f"Hospital:{lista[1]} enfermedad:{lista[8]} precio:{lista[12]} ")
                    if cantidad!=0:
                        total = precio / cantidad
                        print(total, precio)
                        subir_string+=(f"El estado de  {estados_lista[0]} tiene un promedio de {total}, en la afeccion {enfermedad}\n")
                    subir.write(subir_string)

        subir.close()
        archivo.close()
        lista_estados.close()


a="ataque"
#neumonia, cadera, ataque, falla
porcentaje_hospitales_a(a)



def funcion_5(cp, afeccion):
    try:
        archivo=open("pvc.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        enfermedad = afeccion_abreviado(afeccion)
        cantidad = 0
        precio = 0
        for linea in archivo:
            lista = remove_space(linea)
            if lista[5] == cp and lista[8] == enfermedad and lista[12] not in "Not Available ":
                cantidad += 1
                precio += float(lista[12])
                print(f"El hospital:{lista[1]} en la enfermedad:{lista[8]}, tiene un precio de:${lista[12]}")
        if cantidad!=0:
            total=precio/cantidad
            print(f"El precio promedio de la zona postal {lista[5]} es de {total:6.0f}")
        else:
            print(f"El lugar que escogio no posee un hospital o la enfermedad no esta disponible ")

    archivo.close()
#codigo_postal="36744"
#funcion_5(codigo_postal, "ataque")