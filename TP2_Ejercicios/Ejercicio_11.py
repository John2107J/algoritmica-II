import turtle

t = turtle.Turtle()
t.speed(10)

def flor(radio, cantidad):
    if cantidad == 0:
        return
    t.circle(radio)
    t.left(360 / 12)   # 12 pétalos
    flor(radio, cantidad - 1)

def mandala(radio, repeticiones):
    if repeticiones == 0:
        return
    
    flor(radio, 12)   
    t.left(360 / 6)   # rota para siguiente flor
    mandala(radio, repeticiones - 1)


flor(50, 12)
mandala(100, 6)
turtle.mainloop()