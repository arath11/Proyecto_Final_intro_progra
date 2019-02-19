
def minutos(usuario):
    try:
        archivo=open("nombre.csv", "r", encoding="UFT-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        minutos=0
        cuantos=0
        for linea in archivo:
            sin_espacios=linea.rstrip()
            lista=sin_espacios.split(",")
            #print(lista)
            if lista[0]==usuario:
                cuantos+=1
                tiempo=lista[7].split(":")
                minutos=minutos+int(tiempo[0].lstrip("("))*60+int(tiempo[1].rstrip(")"))
        print(f"{usuario} se conecto {minutos} minutos {cuantos} veces")
        archivo.close()
        subirstring += "lo que pida "
        subir.write(subirstring)





















usuario="pperez"
minutos(usuario)


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

