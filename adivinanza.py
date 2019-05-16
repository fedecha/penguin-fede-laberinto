#Juego de adivinar el numero, todos juntos,
#adivinar un numero generado aleatoriamente,
#ir introduciendo por teclado el dato a adivinar

from random import randint
generado=randint(0,10) #generamos el numero aleatorio
print(generado) #trampa
condicion=True  
intento=0

while condicion:
    if intento>0:
        numero=input("dame nro de 0-10")
        intento=intento-1 #intento+=1
        if generado==int(numero): #comparamos el numero introducido
        print("ganaste algo")
        condicion=False
        else:
        print("no ganaste nada")
        print("te quedan",intento,"intentos")
    else:
        condicion=False
        print(perdiste)
    