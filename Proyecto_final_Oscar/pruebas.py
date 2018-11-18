def state(estado):
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

a="Texas"
abreviado= (state(a))
print(abreviado)


#Crea un archivo con la informacion de: nombre de hospital y telefono, para un determinado estado
def abreviatura_estados(estado):
    try:
        arch_estados=open("estados.csv",'r')
    except:
        print("No se puede abrir el archivo o no existe")
    else:
        lista_estados=[]
        for fila in arch_estados:#lista anidada de los estados con su abreviación
            lista_estados.append(fila.rstrip().split(","))
        for linea in range(len(lista_estados)):
            if estado==lista_estados[linea][0]:
                estado=lista_estados[linea][1]
    return estado


def hospitales_estados(estado):
    try:
        arch=open("Payment_and_value_of_care_-_Hospital.csv",'r')
        arch_hospitales=open(f"Hospitales_{estado}.csv",'w+')
    except:
        print("No se puede abrir el archivo o no existe")
    else:

        for linea in arch:
            lista_hospital=[]
            lista=[]#linea del archivo Payment_and_value_of_care_
            lista.append(linea.rstrip().split(","))#Se crea una lista anidada de una sola sublista con un renglon
            estado=abreviatura_estados(estado)

            if estado==lista[0][4]:
                lista_hospital.append(lista[0][1])
                lista_hospital.append(lista[0][7])
                if lista_hospital[0] not in arch_hospitales:
                    string=",".join(lista_hospital)
                    arch_hospitales.write(string+"\n")
                    print(lista_hospital)
#---------------------------------------Main-----------------------------------------------#
estado=input("Escoge un estado de estados unidos: ")
estado=estado.lower()
print(abreviatura_estados(estado))
hospitales_estados(estado)