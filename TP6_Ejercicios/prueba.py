from TadArbolBBusqueda import *
from TadArbolB import *
from TadArbolBE import *


# Ejercicio 1 
#Dado el árbol de la figura, responda las siguientes preguntas:
#1. ¿Qué nodos son hojas? = Son hojas los nodos, D, M, N, F, J, K, L
#2. ¿Cuál nodo es la raíz? = La raiz es el nodo A
#3. ¿Quién es el padre del nodo C? = El padre es la raiz, nodo A
#4. ¿Que nodos son hijos de C? = El nodo C tiene 3 hijos, F, G, H
#. ¿Qué nodos son ancestros de E? = ANcestro del nodo E es el nodo A
#6. ¿Qué nodos son descendientes de E? = Los nodos descendiente son I, M, N
#7. ¿Cual es la profundidad del nodo C? = La profundida es la raiz al nodo C es 1
#8. ¿Cual es la altura del nodo C? = La altura del nodo C es 2
#============================================================================================
# Ejercicio 2
# Se encuentra en TadArbolB.py

#miArbol = ArbolB(10)
#miArbol.izquierdo(7)
#miArbol.derecho(12)

#miArbol.izq.izquierdo(14)
#miArbol.izq.derecho(3)

#miArbol.der.izquierdo(18)
#miArbol.der.derecho(15)

#print("Cantidad de hojas: ", cant_hojas(miArbol))

#======================================================================
# Ejercicio 3
#miArbol = ArbolB(10)
#miArbol.izquierdo(7)
#miArbol.derecho(12)

#miArbol.izq.izquierdo(14)
#miArbol.izq.derecho(3)

#miArbol.der.izquierdo(18)
#miArbol.der.derecho(15)

#print ("Minimo: ", miArbol.minimo())
#print ("Maximo: ", miArbol.maximo())

#=======================================
# Ejercicio 4
# Se encuentra en TadArbolB.py

"""Arbol Desordenado"""
#miArbol = ArbolB(10)
#miArbol.izquierdo(7)
#miArbol.derecho(12)

#miArbol.izq.izquierdo(14)
#miArbol.izq.derecho(3)

#miArbol.der.izquierdo(18)
#miArbol.der.derecho(15)

"""Arbol Ordenado"""
#miArbol2 = ArbolB(10) #Raiz

#miArbol2.izquierdo(7) #Padre izquierdo
#miArbol2.derecho(12) # Padre derecho

#miArbol2.izq.izquierdo(6) # Hijo izquierdo de padre Izquierdo
#miArbol2.izq.derecho(8) # Hijo derecho de padre izquierdp
 
#miArbol2.der.izquierdo(11) # Hijo izquierdo de Padre Derecho
#miArbol2.der.derecho(15) #Hizo derecho de padre Derecho

#print ("Arbol Desordenado: ",Es_ABB(miArbol))

#print ("Arbol Ordenado: ",Es_ABB(miArbol2))

#======================================================================
# Ejercicio 5 
# Se encuentra en TadArbolBBusqueda.py

"""Arbol Ordenado"""
#miArbol2 = ArbolBB(10) #Raiz

#miArbol2.insertar(7) #Padre izquierdo
#miArbol2.insertar(12) # Padre derecho

#miArbol2.izq.insertar(6) # Hijo izquierdo de padre Izquierdo
#miArbol2.izq.insertar(8) # Hijo derecho de padre izquierdp
 
#miArbol2.der.insertar(11) # Hijo izquierdo de Padre Derecho
#miArbol2.der.insertar(15) #Hizo derecho de padre Derecho

#miArbol2.imprimir()
#print()
#print ("Borrar un dato: ",miArbol2.der.der.dato)
#miArbol2.BorrarNodo(15)
#print()
#miArbol2.imprimir()
#===============================================================
# Ejercicio 6
# Se encuentra en TadArbolBBusqueda.py

#miArbol2 = ArbolB(10) #Raiz

#miArbol2.izquierdo(7) #Padre izquierdo
#miArbol2.derecho(12) # Padre derecho

#miArbol2.izq.izquierdo(6) # Hijo izquierdo de padre Izquierdo
#miArbol2.izq.derecho(8) # Hijo derecho de padre izquierdp
 
#miArbol2.der.izquierdo(11) # Hijo izquierdo de Padre Derecho
#miArbol2.der.derecho(15)

"""Prueba 1"""
#print("El rango de ",6," a ",15," es: ")
#ImprimirRango(miArbol2,6,15)

"""Prueba 2"""
#print("El rango de ",8," a ",11," es: ")
#ImprimirRango(miArbol2,8,11)
#============================================================================


