     #Julio Arath Rosales Oliden
#Oscar Miranda

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
            try:
                lista_estados = open("estados.csv", "r+", encoding="UTF-8")
            except IOError:
                print("No se puede abrir ó no se encuentra el archivo")
            else:
                for linea_estados in lista_estados:
                    estados_sin_espacios = linea_estados.rstrip()
                    estados_lista = estados_sin_espacios.split(",")
                    if estado == estados_lista[0]:
                        abreviado=estados_lista[1]
                        for linea in archivo:
                            sin_espacios = linea.rstrip()
                            lista = sin_espacios.split(",")
                            subir_string = ""
                            if lista[4] == abreviado:
                                print(f"Estado: {lista[4]}, Telefono:{lista[7]}")
                                subir_string += (f"Estado: {lista[4]}, Telefono:{lista[7]}" + "\n")
                            subir.write(subir_string)

                lista_estados.close()
                subir.close()
        archivo.close()

estado="Alabama"
hospitales_estado(estado)
