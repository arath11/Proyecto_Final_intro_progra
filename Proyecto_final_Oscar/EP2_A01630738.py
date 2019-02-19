import math


def area_combinada(lado):
    """Esta funcion da el area de un cuadrado menos la de un circulo y regresara el area """
    area_cuadrado=lado*lado
    area_circulo=math.pi*((lado/2)**2)
    area=area_cuadrado-area_circulo
    return area


def con_prefijo(texto, sufijo):
    """Esta funcion compara palabra por palabra en un string para poder conseguir cuantas palabras comienzan con un
    sufijo, en este caso con sub, depues regreasara la lista """
    comparacion=""
    nuevo_texto=list(texto)
    sufijo_lista=list(sufijo)
    tamaño_sufijo=0
    lista_final=[]
    for a in range(len(sufijo_lista)):
        tamaño_sufijo+=1
        #print(tamaño_sufijo)
    for i in (nuevo_texto):
        if " " == i:
            if comparacion[0:tamaño_sufijo:1] == sufijo:
                lista_final.append(comparacion)
            comparacion=""
        else:
            comparacion=comparacion+str(i)

    return lista_final


def calcula_frecuencias(lista_hijos):
    """Esta funcion compara de una lista de hijos, la cantidad de niños dependiendo una encuesta, pero no usa variables para
    ello, en su lugar usa la lista que regresara para guardar los datos """
    lista_frecuencia=[0,0,0,0]
    for i in range(len(lista_hijos)):
        if lista_hijos[i]==1:
            lista_frecuencia[0] = lista_frecuencia[0] + 1
        elif lista_hijos[i]==2:
            lista_frecuencia[1] = lista_frecuencia[1] + 1
        elif lista_hijos[i] == 3:
            lista_frecuencia[2] = lista_frecuencia[2] + 1
        elif lista_hijos[i] == 4:
            lista_frecuencia[3] = lista_frecuencia[3] + 1
    return lista_frecuencia


def menu():
    """Esta funcion da la respuesta del menu y la regresa para que el while la pueda usar """
    print("Hola, este programa tiene diversas opciones:\n(1)Area Combinada\n(2)Prefijos\n(3)Frecuencias\n(4) SALIR")
    respuesta=input("Porfa selecciona una:\n")
    return respuesta

#comienza el programa
respuesta=0
#Se usa un while para hacer el menu y hacer repetirlo la hasta que reciba un 4
while respuesta!="4":
    #Pide la opcion del menu y la compara
    respuesta=menu()
    #Los if son usados para activar cada funcion y dar su valor con un formateo :)
    if respuesta=="1":
        lado=float(input("Dame el lado del cuadrado:\n"))
        print(f"El area del sombra oscura es de {area_combinada(lado):10.4f}")
    elif respuesta=="2":
        texto = "El tren subterraneo une el centro de la ciudad con los suburbios y apesar de que es una excelente " \
                "\nalternativa de transporte es de subutilizado por los habitantes"
        sufijo = "sub"
        print(f"Con el texto: {texto} y el sufijo {sufijo}")
        print(f"Regresa las palabras : {con_prefijo(texto, sufijo)}, con el sufijo {sufijo}")
    elif respuesta=="3":
        lista = [3, 1, 2, 2, 4, 1, 1, 1, 3, 2, 2, 2, 2, 1, 3, 3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 4, 2]
        print(f"Con la lista {lista}\nDa la siguiente frecuencia de hijos:"
              f"\nUn hijo {calcula_frecuencias(lista)[0]}\nDos hijos {calcula_frecuencias(lista)[1]}"
              f"\nTres hijos {calcula_frecuencias(lista)[2]}\nCuatro hijos {calcula_frecuencias(lista)[3]} ")
    elif respuesta=="4":
        print(f"Gracias por usar este programa :)")
    else:
        print(f"Porfa seleciona una opcion valida :)")
    print("\n")

