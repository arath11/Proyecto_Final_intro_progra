"""
    Proyecto final - Fundamentos de programación
        Prof. Fabiola Uribe Plata
    Integrantes del equipo:
        Julio Arath Rosles Olidén   A01630738
        Oscar Miranda Escalante     A01630791
"""

import datetime

#  funciones auxiliares: make_list, short, long y traduce_afección:


def make_list(linea):  # convierte una línea de cualquier documento .txt o .csv en una lista
    sin_espacios = linea.rstrip()
    lista = sin_espacios.split(",")
    return lista


def short(estado):  # cambia un nombre de estado en su abreviatura
    try:
        lista_estados = open("states.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir o no se encuentra el archivo")
    else:
        for linea_estados in lista_estados:
            estados_sin_espacios = linea_estados.rstrip()
            estados_lista = estados_sin_espacios.split(",")
            if estado == estados_lista[1]:
                lista_estados.close()
                return estados_lista[0]
        lista_estados.close()


def long(estado):  # cambia la abreviatura de un estado por el nombre completo
    try:
        lista_estados = open("states.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir o no se encuentra el archivo")
    else:
        for linea_estados in lista_estados:
            estados_sin_espacios = linea_estados.rstrip()
            estados_lista = estados_sin_espacios.split(",")
            if estado == estados_lista[0]:
                lista_estados.close()
                return estados_lista[1]
        lista_estados.close()


def traduce_afeccion(afeccion):  # traduce la afección a la manera en que está escrita en el arhivo csv
    if afeccion == "ataque":
        return "Payment for heart attack patients"
    elif afeccion == "falla":
        return "Payment for heart failure patients"
    elif afeccion == "cadera":
        return "Payment for hip/knee replacement patients"
    elif afeccion == "neumonía":
        return "Payment for pneumonia patients"


#  funciones principales:


def hospitales_estado(estado):  # función 1
    try:
        info = open("pvc.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        try:
            archivo_output_hospitales = open("Hospitales_" + estado + ".csv", "w", encoding="UTF-8")
        except IOError:
            print("No se puede abrir o no se encuentra el archivo")
        else:
            archivo_output_hospitales.write(f"Reporte: hospitales en un estado. \n")
            archivo_output_hospitales.write(f"Fecha de generación: {datetime.date.today()} \n")
            archivo_output_hospitales.write(f"Nombre del hospital, Teléfono \n")
            ST = short(estado)
            anterior = ""
            for linea in info:
                lista_analisis = make_list(linea)
                subir_string = ""
                if lista_analisis[4] == ST and anterior != lista_analisis[1] :
                    subir_string += (f"{lista_analisis[1]},{lista_analisis[7]}" + "\n")
                    anterior = lista_analisis[1]
                archivo_output_hospitales.write(subir_string)
        archivo_output_hospitales.close()
    info.close()


def lowest_high(state, afeccion):  # función 2
    ST = short(state)
    high_estimate = 0
    payment_measure_name = traduce_afeccion(afeccion)
    try:
        archivo = open("pvc.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir o no se encuentra el archivo")
    else:
        for linea in archivo:
            lista_analisis = make_list(linea)
            if lista_analisis[4] == ST:
                if lista_analisis[8] == payment_measure_name:
                    if lista_analisis[14] != 'Not Available':
                        if int(lista_analisis[14]) > high_estimate:
                            high_estimate = int(lista_analisis[14])
                            hospital = lista_analisis[1]
        archivo.close()
        return hospital


def menor_que_promedio_ciudad_estado(city, state, affection):  # función 3
    ST = short(state)
    payment_measure_name = traduce_afeccion(affection)
    try:
        archivo = open("pvc.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir o no se encuentra el archivo")
    else:
        num_hospitales = 0
        for line in archivo:
            lista_analisis = make_list(line)
            if lista_analisis[4] == ST:
                if lista_analisis[3] == city:
                    if lista_analisis[8] == payment_measure_name:
                        if lista_analisis[10] == 'Less than the National Average Payment':
                            num_hospitales += 1
        archivo.close()
        return num_hospitales


def mayor_que_promedio_estado(afeccion):  # función 4

    us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
                 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
                 'OH', 'OK', 'OR', 'PA', 'RI', 'CA', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    try:
        archivo = open('porcentajes_' + afeccion + '.csv', 'w', encoding='UTF-8')
    except:
        print('No se pudo abrir o no se encontró el archivo')
    else:
        archivo.write(f"Reporte: porcentaje de hospitales por estado, que atienden una afección y que su indicador es"
                      f" que el pago es mayor al promedio. \n")
        archivo.write(f"Fecha de generación: {datetime.date.today()} \n")
        archivo.write(f'Estado,Porcentaje de hospitales que atienden {afeccion} con costo mayor al promedio\n')
        try:
            data = open('pvc.csv', 'r', encoding='UTF-8')
        except IOError:
            print('No se puede abrir o no se encuentra el archivo.')
        else:
            payment_measure_name = traduce_afeccion(afeccion)
            for n in range(0, 50):
                num_hospitales = 0
                total_hospitales = 0
                estado = us_states[n]
                data.seek(0)
                for line in data:
                    lista_analisis = make_list(line)
                    if lista_analisis[4] == estado:
                        if lista_analisis[8] == payment_measure_name:
                            total_hospitales += 1
                            if lista_analisis[10] == 'Greater than the National Average Payment':
                                num_hospitales += 1
                if total_hospitales != 0:
                    porcentaje = num_hospitales / total_hospitales * 100
                    archivo.write(f'{long(estado)},{(porcentaje):2.2f}%\n')
                else:
                    archivo.write(f'{long(estado)},0.00%\n')
            data.close()
        archivo.close()


def promedio_costo_CP(cp, afeccion):  # función 5
    try:
        archivo=open("pvc.csv", "r", encoding="UTF-8")
    except IOError:
        print("No se puede abrir o no se encuentra el archivo")
    else:
        enfermedad = traduce_afeccion(afeccion)
        cantidad = 0
        suma_payments = 0
        for linea in archivo:
            lista = make_list(linea)
            if lista[5] == cp and lista[8] == enfermedad and lista[12] not in "Not Available ":
                cantidad += 1
                suma_payments += int(lista[12])
        if cantidad != 0:
            total = suma_payments/cantidad
            print(f"El costo promedio en esta zona postal ({lista[5]}) es de ${total:5.0f}\n")
        else:
            print(f"No hay información disponible sobre esta afección para la zona postal seleccionada.\n")
        archivo.close()


# menú:

print('Bienvenid@, con este programa podrá obtener información relevante de los hospitales en Estados Unidos.')
option = ''
while option != '6':
    print('\nElija una opción:'
          '\n1: Obtener nombre y teléfono de todos los hospitales en un estado'
          '\n2: Buscar hospital con menor estimación en el límite alto'
          '\n3: Obtener número de hospitales que atienden una afección con pago menor al promedio'
          '\n4: Obtener porcentaje de hospitales por estado con pago mayor al promedio para una determinada afección'
          '\n5: Promedio del costo por zona postal y afección'
          '\n6: Salir')
    option = input('¿Qué desea realizar?\n')
    if option is '1':
        estado = input('¿De qué estado desea obtener esta información? '
                       '(Por favor, escriba el nombre del estado en inglés):\n')
        hospitales_estado(estado)
        print('Se ha generado un archivo con el nombre '
              f'Hospitales_{estado}.csv con la información que solicitó. Cierre el programa para poder verlo.\n')
    elif option is '2':
        estado = input('¿En qué estado quiere reailzar su búsqueda? '
                       '(Por favor, escriba el nombre del estado en inglés):\n')
        afeccion = input('¿Qué afección le interesa? (ataque/falla/cadera/neumonía):\n')
        print('El hospital con la menor estimación en el límite alto atendiendo '
              f'{afeccion} en {estado} es {lowest_high(estado, afeccion)}\n')
    elif option is '3':
        afeccion = input('¿Qué afección le interesa? (ataque/falla/cadera/neumonía):\n')
        estado = input('¿En qué estado quiere reailzar su búsqueda? '
                       '(Por favor, escriba el nombre del estado en inglés):\n')
        ciudad = input('¿En qué ciudad quiere reailzar su búsqueda? '
                       '(Por favor, escriba el nombre del estado en inglés):\n')
        print(f'En {ciudad}, {estado}, existe(n) {menor_que_promedio_ciudad_estado(ciudad.upper(), estado, afeccion)} '
              f'hospital(es) que atienden {afeccion} y que su indicador es que el pago es menor al promedio nacional.\n')
    elif option is '4':
        afeccion = input('¿Qué afección le interesa? (ataque/falla/cadera/neumonía):\n')
        print('procesando...')
        mayor_que_promedio_estado(afeccion)
        print('Se ha generado un archivo con el nombre '
              f'porcentajes_{afeccion}.csv con la información que solicitó. Cierre el programa para poder verlo.\n')
    elif option is '5':
        cp = input('¿En qué zona postal desea buscar?\n')
        afeccion = input('¿Qué afección le interesa? (ataque/falla/cadera/neumonía):\n')
        promedio_costo_CP(cp, afeccion)
    elif option is '6':
        print('Gracias por utilizar el programa. ¡Adiós!')
    else:
        print('No existe la opción seleccionada. Por favor, vuelva a intentarlo.\n')