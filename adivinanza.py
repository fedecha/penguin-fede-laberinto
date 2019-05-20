from random import randint
generado=randint(0,10) #generamos el numero aleatorio
print(generado) #trampa
#condicion=True  
intento=3

print('tenés ',intento, ' intentos' )
while intento>0:
        numero=input("dame nro de 0-10: ")
        #intento-=1 #intento+=1 #SE MOVIÓ A LA LINEA 16
        if generado==int(numero): #comparamos el numero introducido
            print("ganaste algo")
            break #ya que el jugador ganó, se detiene el bucle con "break"
        else:
            print("fallaste")
            intento-=1 #intento+=1  #se cambia de lugar, ya que si se acierta en el primer intento
                                    #no es necesario ejecutar esta linea
            print("te quedan ",intento," intentos")
            if intento == 0:
                print('perdiste')
