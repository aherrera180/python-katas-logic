# %%
# ============================================================
# KATA 1 - Frecuencia de letras
#
# Enunciado:
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra. Los espacios no deben ser considerados.
#
# Aprendizaje aplicado:
# Uso de funciones, diccionarios, bucles y condicionales para contar las apariciones de cada letra en un texto.
#
# Apoyo de IA:
# Consulta de ejemplos para comprender cómo almacenar y actualizar las frecuencias en un diccionario.
#
# Dificultades:
# Inicialmente coloqué el return dentro del bucle, provocando que la función terminase antes de recorrer todas las letras. Corregí su indentación.
# ============================================================
texto = "Visca el Barça"
def frecuencias_letras(texto):
    frecuencias = {}

    for letra in texto:
        if letra !=" ":
            if letra in frecuencias:
                frecuencias [letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias
print(frecuencias_letras(texto))

# %%
# ============================================================
# KATA 2 - Multiplicar los elementos de una lista
#
# Enunciado:
# Crear una función que reciba una lista de números y devuelva otra lista con cada elemento multiplicado por 2.
#
# Aprendizaje aplicado:
# Uso de map() y una función lambda para aplicar una operación matemática a todos los elementos de una lista.
# Conversión del resultado a lista mediante list().
# ============================================================
numeros = [2,4,8,9,10]
def duplicar_numeros(numeros):
    return list(map(lambda numero: numero*2, numeros))
print (duplicar_numeros(numeros))

# %%
# ============================================================
# KATA 3 - Filtrar palabras según una palabra objetivo
#
# Enunciado:
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que
# contengan la palabra objetivo.
#
# Aprendizaje aplicado:
# Uso de funciones, listas, bucles for y condicionales.
# Aplicación del operador in para comprobar si una palabra contiene el texto objetivo y append() para almacenar las coincidencias en una nueva lista.
#
# Dificultades:
# Corrección de un error en el nombre de una variable
# (objetivos en lugar de objetivo).
# ============================================================
palabras = ["maritimo","aereo","terrerstre","maremoto","huracan","tension","mareo","caminar","volar","remar","mercaderia"]
objetivo = "mar"

def buscar_palabras(palabras,objetivo):
    resultado = []

    for palabra in palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado

print(buscar_palabras(palabras,objetivo))


# %%
# ============================================================
# KATA 4 - Resta de elementos de dos listas
#
# Enunciado:
# Crear una función que reciba dos listas de números y devuelva una nueva lista con la resta de los elementos que ocupan la misma posición en ambas listas.
#
# Aprendizaje aplicado:
# Uso de map() con una función lambda de dos parámetros para realizar operaciones entre elementos de dos listas.
# Conversión del resultado mediante list().
# ============================================================
Lista1 =[-2,4,8,89]
Lista2 =[1,2,5,99]

def diferencia_listas(Lista1,Lista2):
    return list(map(lambda x,y: x - y, Lista1, Lista2))

print (diferencia_listas(Lista1,Lista2))

# %%
# ============================================================
# KATA 5 - Cálculo de la media y estado académico
#
# Enunciado:
# Crear una función que reciba una lista de números y un parámetro opcional nota_aprobado, cuyo valor por defecto
# sea 5. Calcular la media y determinar si el resultado es "aprobado" o "suspenso" según la nota mínima.
# Devolver una tupla con la media y el estado.
#
# Aprendizaje aplicado:
# Uso de funciones con parámetros opcionales y valores por defecto. Aplicación de sum() y len() para calcular la media, condicionales para determinar el estado
# y tuplas para devolver varios resultados.
# ============================================================

notas = [5,6,7,8,9,2,4]

def evaluar_notas (notas,nota_aprobado=5):
    media= sum(notas) /len(notas)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media,estado)
print(evaluar_notas(notas))


# %%

# ============================================================
# KATA 6 - Cálculo del factorial mediante recursividad
#
# Enunciado:
# Crear una función recursiva que reciba un número entero y calcule su factorial.
#
# Aprendizaje aplicado:
# Uso de funciones recursivas, condicionales y return.
# Comprensión del caso base para detener la recursión y de las llamadas sucesivas a la propia función.
#
# Dificultades:
# Inicialmente utilicé una variable externa (numero) en lugar del parámetro de la función (numero1).
# Esto provocaba llamadas recursivas incorrectas.
# Corregí la referencia para que la función trabajase con su propio parámetro.
# ============================================================

numero = 7

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero*calcular_factorial(numero - 1)

print(calcular_factorial(numero))

# %%
# ============================================================
# KATA 7 - Convertir una lista de tuplas en cadenas de texto
#
# Enunciado:
# Crear una función que reciba una lista de tuplas y devuelva una nueva lista con cada tupla convertida en una cadena de texto.
#
# Aprendizaje aplicado:
# Uso de map() y str() para convertir las tuplas en cadenas de texto y list() para obtener el resultado como una lista.
# ============================================================

intolerancias = [("gluten","lactosa","sorbitol"),("fructosa","sibo","huevo"),("polen","medicamentos","metales"),("textil","hongos","luz")]

def convertir_tuplas(intolerancias):
    return list(map(str,intolerancias))

print(convertir_tuplas(intolerancias))
                                                              

# %%

# ============================================================
# KATA 8 - División de dos números y gestión de errores
#
# Enunciado:
# Crear un programa que solicite dos números al usuario y realice su división, gestionando los posibles errores cuando los valores introducidos no sean válidos o cuando se intente dividir entre cero.
#
# Aprendizaje aplicado:
# Uso de input() y float() para introducir números.
# Aplicación de try y except para gestionar excepciones como ValueError y ZeroDivisionError.
#
# Dificultades:
# Inicialmente escribí Except con mayúscula, provocando un error de sintaxis. Corregí la palabra a except, respetando la sintaxis de Python.
# ============================================================

try:
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))

    resultado = num1/num2

    print ("Division realizada correctamente.")
    print ("El resultado es:", resultado)

except ValueError:
    print ("ERROR:Debes introducir valores numericos")

except ZeroDivisionError:
    print ("ERROR:No se puede dividir entre 0")

# %%

# ============================================================
# KATA 9 - Filtrar animales de una lista
#
# Enunciado:
# Crear una función que reciba una lista de animales y devuelva otra lista excluyendo los animales indicados en el ejercicio.
#
# Aprendizaje aplicado:
# Uso de filter() y lambda para seleccionar elementos de una lista según una condición.
# Aplicación del operador not in para excluir animales y conversión del resultado mediante list().
#
# Dificultades:
# Inicialmente cometí un error al combinar la expresión lambda con filter() y list(). Corregí la estructura para aplicar correctamente el filtrado.
# ============================================================


mascotas = [
    "Tortuga","loro", "Serpiente Pitón", "gato", "pez", "tigre", "perro", "Mapache", "mandril", "dragon", "Cocodrilo", "rana", "Oso", "pollo"
    ]

mascotas_prohibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"] 
def filtrar_mascotas(mascotas):
    return list (filter(lambda mascota: mascota.lower() not in  [animal.lower() for animal in mascotas_prohibidas], mascotas))
print (filtrar_mascotas(mascotas))


# %%

# ============================================================
# KATA 10 - Cálculo de la media y excepción personalizada
#
# Enunciado:
# Crear una función que calcule la media de una lista de números. Si la lista está vacía, debe lanzar una excepción personalizada.
#
# Aprendizaje aplicado:
# Uso de sum() y len() para calcular la media.
# Creación de una excepción personalizada mediante una clase que hereda de Exception.
# Aplicación de raise para lanzar la excepción cuando la lista está vacía.
# ============================================================

class ListaVaciaError(Exception):
    pass

def promedio(numeros):
    if not numeros:
        raise ListaVaciaError ("La Lista está vacía")
    return sum(numeros) / len(numeros)
numeros= [10,11,13,8,90]

try: 
    print(promedio(numeros))
except ListaVaciaError as error:
    print(error)

# %%

# ============================================================
# KATA 11 - Validación de la edad
#
# Enunciado:
# Crear un programa que solicite la edad del usuario y compruebe que sea un número entero entre 0 y 120.
# Si la edad no es válida, debe lanzar una excepción.
#
# Aprendizaje aplicado:
# Uso de input() e int() para introducir y convertir datos.
# Aplicación de condicionales para validar un intervalo y de raise ValueError para señalar valores no válidos.
# Utilización de try-except para gestionar los errores.
# ============================================================


try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años")
    
    print ("Edad Valida:",edad)

except ValueError as error:
    print ("ERROR", error)


# %%

# ============================================================
# KATA 12 - Longitud de las palabras de un texto
#
# Enunciado:
# Crear una función que reciba una cadena de texto y devuelva una lista con la longitud de cada palabra.
#
# Aprendizaje aplicado:
# Uso de split() para separar el texto en palabras.
# Aplicación de map() y len() para calcular la longitud de cada palabra y list() para obtener los resultados en una lista.
# ============================================================

frase = "Busco feina a SC , en general"

def longitud_palabras (frase):
    palabras = frase.split()
    return list(map(len,palabras))

print (longitud_palabras(frase))

# %%

# ============================================================
# KATA 13 - Conversión de caracteres
#
# Enunciado:
# Crear una función que reciba una cadena de texto y devuelva una lista de tuplas con cada carácter único en mayúscula y minúscula, ordenados alfabéticamente.
#
# Aprendizaje aplicado:
# Uso de lower() para normalizar los caracteres, set() para eliminar duplicados y sorted() para ordenarlos alfabéticamente.
# Aplicación de map() y lambda para generar tuplas con cada carácter en mayúscula y minúscula.
# ============================================================

caractares = "Hambre"

def convertir_caracteres(caracteres):
    letras_unicas = sorted(set(caracteres.lower()))
    return list(map(lambda letra:(letra.upper(),letra.lower()),letras_unicas))
print (convertir_caracteres(caractares))


# %%

# ============================================================
# KATA 14 - Filtrar palabras por su letra inicial
#
# Enunciado:
# Crear una función que reciba una lista de palabras y devuelva aquellas que comiencen por la letra "L".
#
# Aprendizaje aplicado:
# Uso de filter() y lambda para seleccionar palabras que cumplen una condición.
# Aplicación de startswith() para comprobar la letra inicial de cada palabra y list() para convertir el resultado en una lista.
# ============================================================
 
palabras =  ["Lupa","Lupus","Lactosa","Lobo", "Dragon", "Boli","Bateria", "Cielo", "Mar", "Tierra"]

letra = "L"

def filtrar_palabras (palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra),palabras))
print (filtrar_palabras(palabras,letra))

# %%

# ============================================================
# KATA 15 - Sumar 3 a los elementos de una lista
#
# Enunciado:
# Crear una función lambda que sume 3 a cada número de una lista y devuelva una nueva lista con los resultados.
#
# Aprendizaje aplicado:
# Uso de lambda para definir una operación sencilla y map() para aplicarla a todos los elementos de una lista.
# Conversión del resultado mediante list().
# ============================================================

numeros = [10,18,13,100]

sumar_tres = lambda numero: numero + 3

resultado = list(map(sumar_tres, numeros))

print (resultado)

# %%
# ============================================================
# KATA 16 - Filtrar palabras según su longitud
#
# Enunciado:
# Crear una función que reciba una cadena de texto y un número entero n, y devuelva una lista con las palabras cuya longitud sea mayor que n.
#
# Aprendizaje aplicado:
# Uso de split() para dividir un texto en palabras y filter() con lambda para seleccionar aquellas cuya longitud supera el valor indicado.
# Aplicación de len() para calcular la longitud de cada palabra y list() para obtener el resultado como una lista.
#
# Dificultades:
# Corrección de un error al llamar a la función con un nombre distinto del utilizado en su definición.
# ============================================================

texto = "pi vi wow guau zaragoza transmodal"
n = 4

def filtrar_palabras(texto,n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))
print(filtrar_palabras(texto,n))

# %%

# ============================================================
# KATA 17 - Convertir una lista de dígitos en un número entero
#
# Enunciado:
# Crear una función que reciba una lista de dígitos y devuelva un único número entero formado por esos dígitos, respetando su orden.
#
# Aprendizaje aplicado:
# Uso de reduce() y lambda para combinar los elementos de una lista y obtener un único valor.
# Aplicación de la operación x * 10 + y para construir progresivamente el número entero a partir de sus dígitos.
# ============================================================

from functools import reduce 
digitos=[8,9,7]

def convertir_numero(digitos):
    return reduce(lambda x,y: x*10 + y, digitos)

print(convertir_numero(digitos))


# %% [markdown]
# 

# %%

# ============================================================
# KATA 18 - Filtrar estudiantes según su calificación
#
# Enunciado:
# Crear una función que reciba una lista de diccionarios con información de estudiantes y devuelva aquellos cuya calificación sea igual o superior a 90.
#
# Aprendizaje aplicado:
# Uso de listas de diccionarios para almacenar información de estudiantes y acceder a sus calificaciones mediante claves.
# Aplicación de filter() y lambda para seleccionar los estudiantes que cumplen la condición de calificación mínima, convirtiendo el resultado en una lista mediante list().
# ============================================================

estudiantes = [
    {"nombre": "Josh", "edad" : 27, "calificacion": 34},
    {"nombre": "Laura", "edad" : 34, "calificacion": 98},
    {"nombre": "Janeit", "edad" : 29, "calificacion": 100},
    {"nombre": "Mamadou", "edad" : 24, "calificacion": 100},
    {"nombre": "Nil", "edad" : 28, "calificacion": 999},
    {"nombre": "Ricard", "edad" : 27, "calificacion": 94},
    {"nombre": "Juana", "edad" : 29, "calificacion": 49}
]

def filtrar_estudiantes(estudiantes):
    return list (filter(lambda estudiante: estudiante ["calificacion"] >= 90, estudiantes))
print (filtrar_estudiantes(estudiantes))

# %%

# ============================================================
# KATA 19 - Filtrar números impares de una lista
#
# Enunciado:
# Crear una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números impares.
#
# Aprendizaje aplicado:
# Uso de filter() y lambda para seleccionar los elementos de una lista que cumplen una condición.
# Aplicación del operador módulo (%) para identificar los números impares, comprobando que el resto de su división entre 2 sea distinto de cero.
# Conversión del resultado a una lista mediante list().
# ============================================================

numeros = [1,2,3,4,5,17,71,97]

impares = lambda numero: numero % 2 !=0

resultado = list(filter(impares,numeros))

print(resultado)

# %%

# ============================================================
# KATA 20 - Filtrar números enteros de una lista
#
# Enunciado:
# Crear una función que reciba una lista con elementos de diferentes tipos de datos y devuelva una nueva lista que contenga únicamente los números enteros.
#
# Aprendizaje aplicado:
# Uso de filter() y lambda para seleccionar elementos de una lista según su tipo de dato.
# Aplicación de isinstance() para comprobar si cada elemento es de tipo int y list() para obtener el resultado como una lista.
# ============================================================

data = ["Analytics", 30, "Youtube", 22, "Sudadera", 2,8,7,88, "MiauMiauN"]

def filtrar_enteros(data):
    return list(filter(lambda elemento:isinstance(elemento, int), data))
print (filtrar_enteros(data))

# %%

# ============================================================
# KATA 21 - Calcular el cubo de un número
#
# Enunciado:
# Crear una función lambda que reciba un número y devuelva su cubo.
#
# Aprendizaje aplicado:
# Uso de lambda para definir una función sencilla y del operador ** para calcular la potencia de un número.
#
# Dificultades:
# Inicialmente utilicé una variable distinta de la definida para la prueba, obteniendo un resultado inesperado debido a una variable que permanecía en memoria de una celda anterior de Jupyter Notebook.
# Corregí la referencia para utilizar la variable adecuada.
# ============================================================

num = 3

calcular_cubo = lambda x: x ** 3

print (calcular_cubo(num))

# %%
# ============================================================
# KATA 22 - Producto de los elementos de una lista
#
# Enunciado:
# Crear una función que reciba una lista de números y devuelva el producto de todos sus elementos utilizando reduce().
#
# Aprendizaje aplicado:
# Uso de reduce() y lambda para multiplicar progresivamente todos los elementos de una lista y obtener un único resultado.
#
# Dificultades:
# Inicialmente omití la lista de números como argumento de reduce(), provocando un error. Corregí la llamada incluyendo la lista sobre la que debía realizarse la operación.
# ============================================================

from functools import reduce

numeros = [4,6,8,10]

def producto_total(numeros):
    return reduce(lambda x,y: x * y,numeros)

print (producto_total(numeros))

# %%

# ============================================================
# KATA 23 - Concatenar palabras de una lista
#
# Enunciado:
# Crear una función que reciba una lista de palabras y devuelva una única cadena de texto con todas las palabras concatenadas, separadas por espacios, utilizando reduce().
#
# Aprendizaje aplicado:
# Uso de reduce() y lambda para combinar progresivamente los elementos de una lista en una única cadena de texto.
# Aplicación del operador + para concatenar palabras e introducir espacios entre ellas.
# ============================================================

from functools import reduce

palabras = ["Vamos", "a", "aprobar"]

def concatenar_palabras(palabras):
    return reduce (lambda x,y: x + " " + y, palabras)
print (concatenar_palabras(palabras))

# %%

# ============================================================
# KATA 24 - Resta acumulada de los elementos de una lista
#
# Enunciado:
# Crear una función que reciba una lista de números y devuelva el resultado de restar sucesivamente todos sus elementos utilizando reduce().
#
# Aprendizaje aplicado:
# Uso de reduce() y lambda para realizar una resta acumulada sobre los elementos de una lista, comenzando por el primer número y restando los siguientes de forma consecutiva.
# ============================================================

from functools import reduce

numeros = [8000,700,100,34,8,1]

def diferencia_total(numeros): 
    return reduce(lambda x,y: x- y, numeros)
print (diferencia_total(numeros))

# %%

# ============================================================
# KATA 25 - Longitud de una cadena de texto
#
# Enunciado:
# Crear una función que reciba una cadena de texto y devuelva el número total de caracteres que contiene.
#
# Aprendizaje aplicado:
# Uso de funciones y len() para calcular la longitud de una cadena de texto, incluyendo los espacios y otros caracteres que pueda contener.
# ============================================================

texto = "Vamos a aprobar"

def contar_caracteres(texto):
    return len(texto)

print (contar_caracteres(texto))




# %%

# ============================================================
# KATA 26 - Calcular el resto de una división
#
# Enunciado:
# Crear una función lambda que reciba dos números y devuelva el resto de su división.
#
# Aprendizaje aplicado:
# Uso de lambda para definir una función sencilla con dos parámetros y del operador módulo (%) para calcular el resto de una división entre dos números.
# ============================================================

numero1 = 9099876767
numero2 = 3

calcular_resto = lambda x,y: x % y

print (calcular_resto(numero1,numero2))


# %%

# ============================================================
# KATA 27 - Cálculo de la media de una lista de números
#
# Enunciado:
# Crear una función que reciba una lista de números y devuelva su media aritmética.
#
# Aprendizaje aplicado:
# Uso de funciones, sum() para obtener la suma de los elementos y len() para conocer la cantidad de números de la lista.
# Cálculo de la media aritmética mediante la división de la suma total entre el número de elementos.
# ============================================================

numeros = [22,3,16,90,8,17,2,56,97,32] 

def calcular_promedio (numeros):
    return sum(numeros) / len(numeros)

print (calcular_promedio(numeros))

# %%

# ============================================================
# KATA 28 - Encontrar el primer elemento duplicado
#
# Enunciado:
# Crear una función que reciba una lista de elementos y devuelva el primer elemento que aparezca repetido. Si no existen elementos duplicados, debe devolver None.
#
# Aprendizaje aplicado:
# Uso de funciones, bucles for y conjuntos (set) para identificar elementos repetidos en una lista.
# Aplicación del operador in para comprobar si un elemento ya ha aparecido, add() para registrar los elementos recorridos y return para devolver el primer duplicado.
# ============================================================

numeros = [1,18,19,1,27,27,34] 

def primer_duplicado(numeros):
    vistos = set ()
    for numero in numeros:
        if numero in vistos:
            return numero
        else:
            vistos.add(numero)
    return None
print(primer_duplicado(numeros))

# %%

# ============================================================
# KATA 29 - Ocultar caracteres de una cadena de texto
#
# Enunciado:
# Crear una función que reciba una cadena de texto y oculte todos sus caracteres excepto los cuatro últimos, sustituyendo los anteriores por el símbolo #.
#
# Aprendizaje aplicado:
# Uso de funciones, len() y slicing para conservar los cuatro últimos caracteres de una cadena de texto.
# Aplicación de la multiplicación de cadenas para generar los símbolos # necesarios y de max() para evitar valores negativos cuando el texto tiene menos de cuatro caracteres.
# ============================================================

numero = 123456789

def enmascarar(numero):
    texto = str(numero)
    return"#"*max(0,len(texto)-4) + texto[-4:]

print(enmascarar(numero))


# %%

# ============================================================
# KATA 30 - Comprobar si dos palabras son anagramas
#
# Enunciado:
# Crear una función que reciba dos palabras y determine si son anagramas, es decir, si contienen las mismas letras con la misma frecuencia, aunque estén ordenadas de forma diferente.
#
# Aprendizaje aplicado:
# Uso de funciones, lower() para normalizar las mayúsculas y minúsculas, y sorted() para ordenar los caracteres de ambas palabras y compararlos.
# Aplicación del operador == para devolver un resultado booleano (True o False).
#
# Dificultades:
# Inicialmente cometí errores al introducir las palabras sin comillas y al plantear la comparación de caracteres. Corregí la sintaxis y la lógica de la función para comprobar correctamente si dos palabras son anagramas.
# ============================================================

palabra1 = "Amor"
palabra2 = "Roma" 

def comprobar_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
print (comprobar_anagrama(palabra1, palabra2))

# %%

# ============================================================
# KATA 31 - Buscar un nombre en una lista
#
# Enunciado:
# Crear un programa que solicite al usuario una lista de nombres separados por comas y permita buscar un nombre concreto. Si el nombre no se encuentra en la lista, debe lanzar una excepción.
#
# Aprendizaje aplicado:
# Uso de input() y split(",") para convertir una cadena de texto en una lista de nombres.
# Aplicación de strip() para eliminar espacios innecesarios, comprensión de listas para procesar los nombres y el operador in para comprobar si existe una coincidencia.
# Uso de raise ValueError y try-except para gestionar los casos en los que el nombre no aparece en la lista.
#
# Dificultades:
# Inicialmente cometí un error al utilizar un nombre de variable incorrecto dentro de la comprensión de listas. Corregí la referencia para recorrer correctamente los nombres introducidos.
# ============================================================

def buscar_nombre():
    nombres = input("Introude nombres separados por comas").split(",")
    nombres = [nombre.strip() for nombre in nombres]

    objetivo = input("Introduce el nombre que quieres buscar:").strip()

    if objetivo in nombres: 
        print ("Nombre encontrado:", objetivo) 
    else:
        raise ValueError ("El nombre no se encuentra en la lista")

try:
    buscar_nombre()

except ValueError as error:
    print ("ERROR:", error)
                



# %%

# ============================================================
# KATA 32 - Buscar el puesto de un empleado
#
# Enunciado:
# Crear una función que reciba una lista de diccionarios con información de empleados y un nombre, y devuelva el puesto del empleado correspondiente. Si no encuentra el nombre, debe devolver un mensaje indicando que el empleado no existe.
#
# Aprendizaje aplicado:
# Uso de listas de diccionarios para almacenar información de empleados y acceder a sus datos mediante claves como nombre y puesto.
# Aplicación de un bucle for y condicionales para buscar coincidencias, utilizando return para devolver el puesto del empleado encontrado.
#
# Dificultades:
# Inicialmente cometí un error en el nombre de la función y coloqué el return del caso no encontrado dentro del bucle for, provocando que la búsqueda terminase antes de recorrer todos los empleados.
# Corregí la indentación para que el mensaje de empleado no encontrado solo se devuelva después de comprobar toda la lista.
# ============================================================

empleados = [
    {"nombre": "Josh Garcia", "puesto" : "Picker"},
    {"nombre": "Laura Lopez", "puesto" : "Coach"},
    {"nombre": "Janeit Martinez", "puesto" : "Team leader"},
    {"nombre": "Mamadou Akinou", "puesto" : "BDM"},
    {"nombre": "Nil Torres", "puesto" : "Export"},
    {"nombre": "Ricard Sanchez", "puesto" : "Doctor"},
    {"nombre": "Juana de Arco", "puesto" : "Developer"}
]

nombre_completo = "Juana de Arco"

def buscar_empleado(nombre_completo,empleados):
    for empleado in empleados:
        if empleado ["nombre"] == nombre_completo:
            return empleado ["puesto"]
    return "No trabaja aquí"
    
print (buscar_empleado(nombre_completo,empleados))

# %%

# ============================================================
# KATA 33 - Sumar elementos de dos listas
#
# Enunciado:
# Crear una función que reciba dos listas de números y devuelva una nueva lista con la suma de los elementos que ocupan la misma posición en ambas listas.
#
# Aprendizaje aplicado:
# Uso de una función lambda con dos parámetros para sumar los elementos correspondientes de dos listas.
# Aplicación de map() para recorrer ambas listas simultáneamente y list() para convertir el resultado en una nueva lista.
# ============================================================

lista1 = [12,15,18]
lista2= [28,25,82]

sumar_elementos  = lambda x,y: x + y

resultado = list(map(sumar_elementos, lista1, lista2))

print (resultado)

# %%
 
# ============================================================
# KATA 34-35 - Clase Arbol con tronco y ramas
#
# Enunciado:
# Crear una clase Arbol con un tronco de longitud inicial 1 y una lista vacía de ramas. Implementar los métodos crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol para modificar el árbol y consultar la longitud del tronco, el número de ramas y sus longitudes.
# Como caso de uso, crear un árbol, hacer crecer el tronco, añadir una rama, hacer crecer las ramas existentes, añadir dos ramas más, eliminar la rama situada en la posición 2 y obtener la información final del árbol.
#
# Aprendizaje aplicado:
# Introducción a la programación orientada a objetos mediante la definición de clases, atributos y métodos. Uso de __init__ para inicializar los atributos y self para acceder a ellos y modificarlos.
# Aplicación de listas, append(), pop(), bucles for y condicionales para gestionar las ramas del árbol.
#
# Apoyo de IA:
# Utilicé ChatGPT para comprender la estructura de una clase en Python, especialmente el funcionamiento de __init__, self y la relación entre los atributos y los métodos. También consulté un ejemplo completo de implementación y explicaciones para interpretar y resolver el ejercicio.
#
# Dificultades:
# Este ejercicio me resultó especialmente complicado porque la programación orientada a objetos se había practicado poco durante las clases. Inicialmente escribí incorrectamente __init__, confundí el nombre de crecer_tronco y utilicé una variable no definida en quitar_rama.
# Estos errores provocaron excepciones como AttributeError. Tras corregirlos y comprender mejor cómo se inicializan y modifican los atributos de un objeto, conseguí ejecutar el caso de uso correctamente.
# ============================================================

class Arbol: 
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco (self):   
        self.tronco +=1
    def nueva_rama(self):
        self.ramas.append(1)
    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] +=1
    def quitar_rama(self, posicion):
        if 1 <=posicion <= len(self.ramas):
            self.ramas.pop(posicion - 1)    
    def info_arbol(self):
        return self.tronco, len(self.ramas), self.ramas

# Caso del enunciado

arbol = Arbol ()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)

print(arbol.info_arbol())

# %%

# ============================================================
# KATA 36 - Clase UsuarioBanco y operaciones bancarias
#
# Enunciado:
# Crear una clase UsuarioBanco con los atributos nombre, saldo y cuenta_corriente. Implementar los métodos retirar_dinero, transferir_dinero y agregar_dinero para realizar operaciones bancarias, lanzando errores cuando una retirada o transferencia no pueda efectuarse.
# Como caso de uso, crear dos usuarios (Alicia con 100 y Bob con 50), añadir 20 al saldo de Bob, intentar transferir 80 desde Bob hacia Alicia y retirar 50 del saldo de Alicia.
#
# Aprendizaje aplicado:
# Uso de clases, objetos, atributos, métodos, __init__ y self para representar usuarios bancarios y modificar sus saldos.
# Aplicación de condicionales, operadores de comparación, raise ValueError y try-except para validar operaciones y gestionar errores.
# Comprensión de cómo un método puede acceder a los atributos de otro objeto mediante otro_usuario.saldo.
#
# Apoyo de IA:
# Utilicé ChatGPT para comprender la estructura de la clase, el funcionamiento de self y __init__, y cómo realizar operaciones entre dos objetos diferentes. También consulté un ejemplo completo y explicaciones sobre la validación de saldos y el tratamiento de excepciones.
#
# Dificultades:
# Me resultó complicado estructurar los métodos y comprender cómo interactúan dos objetos. Inicialmente escribí incorrectamente el nombre de Alicia, provocando un NameError, y utilicé >= en una condición que impedía transferir exactamente el saldo disponible.
# También tuve que comprender por qué la transferencia del enunciado no podía realizarse: Bob dispone de 70 después del ingreso, pero se le pide transferir 80. El programa gestiona esta operación mediante una excepción por saldo insuficiente.
# ============================================================

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente or cantidad <= 0  or cantidad > self.saldo:
            raise ValueError ("No se puede retirar el dinero")
        self.saldo -= cantidad
    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente or cantidad <= 0 or cantidad > otro_usuario.saldo:
            raise ValueError("No se puede realizar la transferencia")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
    def agregar_dinero(self, cantidad):
        if cantidad <=0:
            raise ValueError ("La cantidad debe ser positiva")
        self.saldo += cantidad

# Caso del enunciado
alicia= UsuarioBanco("Alicia",100, True)
bob= UsuarioBanco("Bob",50,True)

bob.agregar_dinero(20)

try: 
    alicia.transferir_dinero(bob,80)
except ValueError as error: 
    print ("Error", error)    
alicia.retirar_dinero(50)
print ("Saldo Alicia:",alicia.saldo)
print ("Saldo Bob:", bob.saldo)
        





# %%

# ============================================================
# KATA 37 - Procesamiento de texto mediante distintas funciones
#
# Enunciado:
# Crear una función procesar_texto que permita realizar tres operaciones sobre una cadena de texto: contar_palabras, reemplazar_palabras y eliminar_palabra.
# Definir primero las tres funciones auxiliares: una que devuelva un diccionario con la frecuencia de cada palabra, otra que sustituya una palabra original por una nueva y otra que elimine una palabra del texto.
# La función principal debe recibir el texto, una opción ("contar", "reemplazar" o "eliminar") y un número variable de argumentos según la operación seleccionada. Comprobar el funcionamiento de las tres opciones.
#
# Aprendizaje aplicado:
# Uso de funciones, parámetros, condicionales, bucles for y diccionarios para procesar cadenas de texto.
# Aplicación de split(), append() y join() para separar, modificar y reconstruir textos.
# Uso de *args para recibir un número variable de argumentos y pasarlos a las funciones auxiliares correspondientes.
#
# Apoyo de IA:
# Consulté ChatGPT para comprender cómo organizar varias funciones relacionadas entre sí y cómo utilizar *args para pasar diferentes argumentos según la operación seleccionada. También utilicé un ejemplo completo como referencia para desarrollar y comprobar las tres operaciones.
#
# Dificultades:
# Inicialmente cometí un error al escribir el nombre de la variable opcion, provocando un NameError.
# También tuve que corregir los ejemplos de prueba, ya que intentaba reemplazar una cadena vacía y eliminar una palabra que no aparecía en el texto, por lo que no podía comprobar correctamente el funcionamiento de las funciones.
# ============================================================

texto = "Que buena suerte"

def contar_palabras(texto):
    frecuencias = {}
    for palabra in texto.split():
        if palabra in frecuencias:
            frecuencias [palabra] += 1
        else: 
            frecuencias [palabra] = 1
    return frecuencias


def reemplazar_palabras(texto,palabra_original,palabra_nueva):
    palabras = texto.split()
    resultado = []

    for palabra in palabras: 
        if palabra == palabra_original:
            resultado.append(palabra_nueva)
        else:
            resultado.append(palabra)

    return " ".join(resultado)


def eliminar_palabras(texto, palabra):
    palabras = texto.split() 
    resultado = []

    for p in palabras: 
        if p != palabra:
            resultado.append(p)

    return " ".join(resultado)

def procesar_texto (texto,opcion,*args):
    if opcion == "contar":
        return contar_palabras (texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabras(texto, *args)
    else: 
        return "Opcicon no valida"


# Caso de uso del enunciado

print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar","buena", "mala"))
print(procesar_texto(texto, "eliminar", "buena"))
 


# %%

# ============================================================
# KATA 38 - Determinar si es de día, tarde o noche
#
# Enunciado:
# Crear un programa que determine si es de día, tarde o noche en función de la hora introducida por el usuario.
#
# Aprendizaje aplicado:
# Uso de input() e int() para solicitar y convertir la hora introducida por el usuario.
# Aplicación de condicionales if, elif y else para clasificar las horas en tres franjas: día (6-13), tarde (14-20) y noche (21-5).
# Uso de try-except para gestionar entradas no numéricas y validación del intervalo de horas permitido (0-23).
# ============================================================

try: 
    hora = int(input("Introduce una hora (0-23): "))
    if hora < 0 or hora >23:
        print("Error: introduce una hora valida entre 0 y 23")

    elif 6 <= hora < 14:
        print ("Es de día")
    elif 14 <= hora < 21:
        print ("Es de tarde")
    else:
        print ("Es de noche")
except ValueError:
    print ("Error: debes introducir un numero entero")


# %%

# ============================================================
# KATA 39 - Calificación académica según la nota numérica
#
# Enunciado:
# Crear un programa que determine la calificación de un alumno a partir de su nota numérica, siguiendo estos intervalos: de 0 a 69, "Insuficiente"; de 70 a 79, "Bien"; de 80 a 89, "Muy bien"; y de 90 a 100, "Excelente".
#
# Aprendizaje aplicado:
# Uso de input() e int() para solicitar y convertir la calificación numérica del alumno.
# Aplicación de condicionales if, elif y else para clasificar las notas según los intervalos establecidos en el enunciado.
# Validación de notas entre 0 y 100 y uso de try-except para gestionar entradas que no puedan convertirse en números enteros.
# ============================================================


try:
    nota = int(input("Introduce la nota del alumno (0-100)"))
    if nota < 0 or nota > 100:
        print ("Error: la nota debe estar entre 0 y 100")

    elif nota < 70:
        print ("Insuficiente")
    elif nota < 80:
        print ("Bien")
    elif nota < 90:
        print ("Muy bien")
    
    else: 
        print ("EXcelente")

except ValueError: 
    print("Error: debes introducir un numero entero")


# %%

# ============================================================
# KATA 40 - Cálculo de áreas geométricas
#
# Enunciado:
# Crear una función que reciba dos parámetros: figura (rectangulo, circulo o triangulo) y datos (una tupla con las dimensiones necesarias para calcular su área).
#
# Aprendizaje aplicado:
# Uso de funciones, parámetros, condicionales y tuplas para calcular las áreas de distintas figuras geométricas.
# Aplicación del módulo math y de math.pi para calcular el área del círculo.
# ============================================================

import math 

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no valida"

#Casos del ejercicio:

print(calcular_area("rectangulo",(5,3)))
print(calcular_area("circulo",(4,)))
print(calcular_area("triangulo",(6,8)))  
    

# %%

# ============================================================
# KATA 41 - Aplicación de descuentos mediante cupones
#
# Enunciado:
# Crear un programa que solicite el precio original de un artículo y pregunte al usuario si dispone de un cupón de descuento.
# Si tiene cupón, solicitar su valor y aplicar el descuento cuando sea válido y mayor que cero. Mostrar el precio final de la compra utilizando estructuras condicionales if, elif y else.
#
# Aprendizaje aplicado:
# Uso de input() y float() para solicitar y convertir el precio y el valor del cupón.
# Aplicación de condicionales if, elif y else para comprobar si existe un cupón, validar su importe y calcular el precio final.
# Uso de strip() y lower() para normalizar las respuestas del usuario y try-except para gestionar errores de conversión.
# Incorporación de validaciones adicionales para evitar precios negativos y descuentos superiores al precio original.
#
# Apoyo de IA:
# Utilicé ChatGPT para consultar distintas alternativas de implementación y seleccioné una solución con validación de errores mediante try-except.
# Tomé esta propuesta como base para el ejercicio y comprobé su funcionamiento en Jupyter Notebook mediante un ejemplo de compra de 88 € con un cupón de descuento de 60 €.
# ============================================================

try:
    precio = float(input("Introduce el precio original (€): "))

    if precio <= 0:
        print("Error: el precio debe ser mayor que cero")

    else:
        cupon = input("¿Tienes un cupon? (si/no): ").strip().lower()

        if cupon == "si" or cupon == "sí":
            descuento = float(input("Introduce el valor del cupon (€): "))

            if 0 < descuento <= precio:
                precio_final = precio - descuento
                print("Descuento aplicado:", descuento, "€")

            else:
                precio_final = precio
                print("Cupon no valido")

            print("Precio final:", precio_final, "€")

        elif cupon == "no":
            print("Precio final:", precio, "€")

        else:
            print("Error: responde si o no")

except ValueError:
    print("Error: introduce un num valido")

# %%


# %%



