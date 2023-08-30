#Calculadora de límite hecha por Joaquín Sanchez, Román Pereyra, Máximo Soria y Santiago Di Cesare
import sympy as sp

x = sp.Symbol('x')
a = sp.Symbol('a' , real=True )

#Función

g = input("Ingrese la función: ")
f = sp.sympify(g)
limite = sp.limit(f, x, a)

try:
    valorA = float(input("Ingrese el valor numérico de a: "))
except ValueError:
    print ("Los valores no cumplen con los requisitos necesarios para la realización del problema.")
    exit()

#Limites por la izquierda y derecha

limiteIzquierda = limite.subs (a, valorA - 0.1)
limiteDerecha = limite.subs (a, valorA + 0.1)

#Mostrar resultado
comparacion = limiteIzquierda - limiteDerecha

if -0.01<comparacion<0.01 :
    if limiteDerecha>10:
        print("El límite de la función {} es oo (infinito)" .format(f))
    else:
        print("El límite de la función {} existe y es: " .format(f), limiteDerecha)
else:
    print("El límite de la función {} no existe porque los límites laterales no son iguales" .format(f))
    