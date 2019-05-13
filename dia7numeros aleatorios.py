#uso de numeros aleatorios
#creamos un archivo
#guardamos en la carpeta repositorio
#con la extension .py
#uso de numeros aleatorios 

from random import randint               #importamos la libreria randint
aleatorio=randint(0,20)                 #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)      #imprimimos el numero generado

#ejercicio
#escribir una funcion sorteo() que reciba
#una lista de participantes , y elegir a uno de los participantes aleatoriamente, y 
#retornar esa persona elegida
#desafio: no volver a retornar una persona ya sorteada


from random import randint
def sorteo(lista):     
    cant=len(lista)-1     #definimos una funcion 
    # y utilizamos len() para saber la cantidad de personas que en la lista y guardamos en cant
    # para que no salga de rango    
    indice=randint(0,cant)
    #generamos un indice aleatorio y seleccionamos un elemento de la lista y guardamos en variable ganador
    ganador=lista[indice]
    #retornamos ganador
    return ganador

#creamos la lista de los participantes
participantes=["fede","ale","vero","adolf","jfdslkajk"]
#llamamos a la funcion y guardamos en una variable el resultado retornado por la funcion
ganar=sorteo(participantes)
#imprimimos el ganador
print(ganar)