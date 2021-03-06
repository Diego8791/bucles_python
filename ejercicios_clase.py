#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios con bucles "while"}
    
    # print('esta es la primera parte del ejercicio')

    x = 0
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración

    while x < 6:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        x += 1     # Coloque la línea de código para que "X" incremente "1"

    # print('esta es la segunda parte del ejercicio')

    x = 5
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    while x >= 0:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        x -= 1  # Coloque la línea de código para que "X" decremente "1"


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']

    print('esta es la primera parte del ejercicio')
    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...

    for color in colores:
        print(color)
    
    print('este es la segunda parte del ejercicio')
    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...

    for i in range(len(colores)):
        print(colores[i])

def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero

    for numero in numeros:
        suma += numero
    print('la sumatoria de la lista numeros es',suma)

def ej4():
    # Ejercicios con bucles "while" 

    x = 0
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    print('primera parte del ejercicio')
    
    while (x < 10) and (x != 6):
        print('el valor actual de x es', x)
        x += 2

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    print('segunda parte del ejercicio')
    
    x = 0

    while True:
        if x == 6:
            break
        if x < 10:
            print('el valor actual de x es:', x)
            x += 2

def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    # fin....
    fin = int(input('Ingrese el último número de la secuencia\n'))
    # for ... in range(....)
    
    sumatoria = 0
    for i in range(inicio, fin + 1):     # incluye número final de la secuencia
        sumatoria += i

    # Imprimir el valor de la sumatoria

    print('La sumatoria de la secuencia es', sumatoria)


def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primer número de la secuencia\n'))
    
    while True:    # while para evaluar que los número final ingresado sea correctos
        # fin....
        fin = int(input('Ingrese el último número de la secuencia\n'))    
        
        if fin <= inicio:     # evalúo que el número final de la secuencia sea mayor al inicial
            print('Ingrese un número mayor a', inicio)
            continue      # volverá a ejecutarse el while para ingresar otro número de final de secuencia
        else:
            cantidad_numeros_positivos = 0  # Inicializo el contador en 0
            #cantidad_numeros_negativos
            cantidad_numeros_negativos = 0  # Inicializo el contador en 0
           
            # for ... in range(....)
            for i in range(inicio, fin + 1):  # Incluye a valor de fin de secuencia
                if i >= 0:
                    cantidad_numeros_positivos += 1
                else:
                    cantidad_numeros_negativos += 1
        
            # Imprimir el valor de la cantidad de números positivos y negativos
            print('La cantidad de números positivos y cero en la secuencia son', cantidad_numeros_positivos)
            print('La cantidad de números negativos son', cantidad_numeros_negativos)
        break

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    ej6()
