import turtle

t = turtle.Turtle()
t.speed(0)

def koch(longitud, nivel):
            

    if nivel == 0: # Si el nivel es 0 se dibuja una recta
        t.forward(longitud)
    else:
        koch(longitud / 3, nivel - 1)
        t.left(60)

        koch(longitud / 3, nivel - 1)
        t.right(120)

        koch(longitud / 3, nivel - 1)
        t.left(60)

        koch(longitud / 3, nivel - 1)


if __name__ == "__main__":


    koch(200, 3) 
    turtle.mainloop()
