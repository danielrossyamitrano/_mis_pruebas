#El jugador elegirá al principio el sexo y el nombre de su personaje. A continuación, ingresará una edad, con un mínimo de 15 años, y un máximo de 30. Esta edad colocará al personaje dentro de un rango. Los rangos son  15 a 18, 19 a 21, 22 a 24, 25 a 27 y 28 a 30. Por cada uno de estos, hasta la el rango en el que está la edad, más 2 por infancia y adolescencia temprana, el jugador seleccionará un Hecho de la Vida.
#Seleccionados todos los hechos (esto es, conformado el trasfondo), se determinará  la motivación de ese personaje.
#Hechos de la vida: Por cada rango de edad hasta llegar a la edad de su personaje, seleccione un evento de una lista de eventos. La suma de todos los hechos dará forma al trasfondo y determinará la motivación inicial.

# def elegirHechoDeVida():
    # print('hecho')

# #1 - Elegir sexo
# #2 - Elegir nombre
# #3 - Elegir edad (min 15, max 30).
# while True:
    # sex = input('sexo: ')
    # nom = input('nombre: ')
    # edad = int(input('edad: '))
    
    # CantHechos = 2+((edad+1)//4)-3
    # if edad > 23:
        # CantHechos+=1
        
    # if 15<= edad <= 30:
        # print(nom+'('+sex+','+str(edad)+' años)')
        # print('seleccione',str(CantHechos),'hechos de vida\n')
    # else:
        # print('ha ocurrido un error.',end='')
        # if not input('¿Quiere intentarlo de nuevo?').lower().endswith('s'):
            # break


edad = int(input('edad: '))
from random import randint

for p in range(1,edad+1):
    print(p)
