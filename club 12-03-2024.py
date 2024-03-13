#un torneo de baloncesto donde hay4 equipos,en cada equipo se hacen infinitos lanzamientos,cada lanzamineto vale puntos,cuando esta dentro del
# del area vale 2 puntos,cuando es fuera del area son 3 puntos,si fue falta vale 1 punto,entonces tiene se tiene que decidir el tipo de lanzamiento:el lanzamiento 1 es cuando es falta,el lanzamiento 2 es cuando esta dentro del area y el lanzamiento 3 es cuando es fuera del area
#los puntos se acumulan y tiene que decir cuantos puntos van, y cuando el usuario presione 'f'se tiene que terminar el programa y al final se debe decidir quien gano de acuerdo a los puntos obtenidos
import os
os.system('cls')
acumuladorBulls=0
acumuladorBostonCeltics =0
acumuladorlakers =0
acumuladorknicks =0
falta= 1
dentro =2
fuera =3

controlbln=True
while controlbln == True:
    opcion=input('Menu de torneo\nEquipos\n1.Chicago Bulls\n2.BostonCeltics\n3.Los Angeles Lakers\n4.New York Knicks\n5.F\nEscoja una opcion:')
    if opcion == '1':
        var_tipo_lanzamientoint =int(input('Ingrese un tipo de lanzamineto\n1.Falta\n2.Tiro dentro del area\n3.Tiro fuera del area\nEscoja un tipo de lanzamiento:'))
        if var_tipo_lanzamientoint == 1:
            cantidadint=int(input('Ingrese la cantidad de lanzaminetos:'))
            totalbulls =cantidadint * falta
            acumuladorBulls += totalbulls
        if var_tipo_lanzamientoint == 2:
            cantidadint=int(input('Ingrese la cantidad de lanzaminetos:'))
            totalbulls =cantidadint * dentro
            acumuladorBulls += totalbulls
        if var_tipo_lanzamientoint == 3:
            cantidadint=int(input('Ingrese la cantidad de lanzaminetos:'))
            totalbulls =cantidadint * fuera
            acumuladorBulls += totalbulls
    elif opcion == '2':
        var_tipo_lanzamientoint =int(input('Ingrese un tipo de lanzamiento\n1.Falta\n2.Tiro dentro del area\n3.Tiro fuera del area\nEscoja un tipo de lanzamiento:'))
        if var_tipo_lanzamientoint == 1: 
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totalceltics = cantidadint * falta
            acumuladorBostonCeltics += totalceltics
        if var_tipo_lanzamientoint == 2: 
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totalceltics = cantidadint * dentro
            acumuladorBostonCeltics += totalceltics
        if var_tipo_lanzamientoint == 3: 
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totalceltics = cantidadint * fuera
            acumuladorBostonCeltics += totalceltics       
    elif opcion == '3':
        var_tipo_lanzamientoint =int(input('Ingrese un tipo de lanzamiento\n1.Falta\n2.Tiro dentro del area\n3.Tiro fuera del area\nEscoja un tipo de lanzamiento:'))
        if var_tipo_lanzamientoint == 1:
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totallakers = cantidadint * falta
            acumuladorlakers += totallakers
        if var_tipo_lanzamientoint == 2:
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totallakers = cantidadint * dentro
            acumuladorlakers += totallakers
        if var_tipo_lanzamientoint == 3:
            cantidadint=int(input('Ingrese la cantidad de lanzamientos'))
            totallakers = cantidadint * fuera
            acumuladorlakers += totallakers  
    elif opcion == '4':  
        var_tipo_lanzamientoint =int(input('Ingrese un tipo de lanzamiento\n1.Falta\n2.Tiro dentro del area\n3.Tiro fuera del area\nEscoja un tipo de lanzamiento:'))
        if var_tipo_lanzamientoint == 1:
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totalknicks = cantidadint * falta
            acumuladorknicks += totalknicks
        if var_tipo_lanzamientoint == 2:
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totalknicks = cantidadint * dentro
            acumuladorknicks += totalknicks
        if var_tipo_lanzamientoint == 3:
            cantidadint=int(input('Ingrese la cantidad de lanzamientos:'))
            totalknicks = cantidadint * fuera
            acumuladorknicks += totalknicks

    elif opcion == 'f' or 'F':
        os.system('cls')
        print('Cantidad de puntos obtenidos  de Los Chicago Bulls------------------------>',acumuladorBulls)
        print('Cantidad de puntos obtenidos de Los Boston Celtics------------------------>',acumuladorBostonCeltics)
        print('Cantidad de puntos obtenidos de Los Angeles Lakers------------------------>',acumuladorlakers)
        print('Cantidad de puntos obtenidos de Los NEW YORK KNICKS----------------------->',acumuladorknicks)
        ganador_puntos = max(acumuladorBulls, acumuladorBostonCeltics, acumuladorlakers, acumuladorknicks)
        if acumuladorBulls == acumuladorBostonCeltics == acumuladorlakers == acumuladorknicks:
            print('Hubo un empate')
        if ganador_puntos == 0:
            print('No hay ganadores')   
        else:
            if ganador_puntos == acumuladorBulls:
                print('El equipo ganador es Chicago Bulls con', ganador_puntos, 'puntos')
            elif ganador_puntos == acumuladorBostonCeltics:
                print('El equipo ganador es Boston Celtics con', ganador_puntos, 'puntos')
            elif ganador_puntos == acumuladorlakers:
                print('El equipo ganador es Los Angeles Lakers con', ganador_puntos, 'puntos')
            else:
                print('El equipo ganador es New York Knicks con', ganador_puntos, 'puntos')
        controlbln = False
        