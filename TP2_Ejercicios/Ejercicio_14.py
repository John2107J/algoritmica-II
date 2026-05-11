from Ejercicio_13 import koch
from Ejercicio_6 import pedir_numero_entero #funcion de pedir entero
import turtle

#EJERCICIO NO RESUELTO, NO PUDE RESOLVERLO A TIEMPO DE LA ENTREGA...
def copo_koch(longitud, nivel):

    t = turtle.Turtle()
    t.speed(100)

    for _ in range(3):
        koch(200, 3)
        t.right(120)

if __name__ == "__main__":

    copo_koch(200,2)

    turtle.mainloop()