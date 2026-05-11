from Ejercicio_6 import pedir_numero_entero #funcion de pedir entero
import turtle

t = turtle.Turtle()
t.speed(100)

#funcion para realizar un cuadrado
def cuadrado(lado, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(lado)
        t.left(90)
    t.end_fill()

#funcion que hace una fila
def fila(columnas, lado, color):
    for _ in range(columnas):
        cuadrado(lado, color)
        t.forward(lado)

#funcion que hace varias filas formando el damero
def damero(filas, columnas, lado, color):
    for _ in range(filas):
        fila(columnas, lado, color)

        t.penup()
        t.backward(columnas * lado)
        t.right(90)
        t.forward(lado)
        t.left(90)
        t.pendown()


#MAIN
#Hice un main para que el usuario elija las caracteristicas del tablero
if __name__ == "__main__":

    colores_validos = ["red", "blue", "green", "yellow"]

    filas = pedir_numero_entero("Ingrese el número de filas: ")
    columnas = pedir_numero_entero("Ingrese el número de columnas: ")
    lado = pedir_numero_entero("Ingrese el tamaño del lado de los cuadrados: ")
    color = input("Elegí color (red, blue, green, yellow): ").lower()

    while color not in colores_validos:
        color = input("Color inválido. Elegí otro: ").lower()


    damero(filas, columnas, lado, color)
    turtle.mainloop()