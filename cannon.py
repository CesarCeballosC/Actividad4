"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
speed_target = vector(0, 0)
targets = []

# Se añade la función tap para responder al toque de la pantalla
def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball): 
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# Se añade la función para verificar que todo se encuentre dentro de la pantalla
def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Se añade la función draw para dibujar los objetivos y el proyectil
def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Se añade la función move para el movimiento de los objetivos
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Movimiento de los objetivos
    for target in targets:
        target.x -= 0.5
        speed_target.x = -1 # Se ajusta la velocidad de los objetivos
        target.move(speed_target)

    # Movimiento del misil
    if inside(ball):
        speed.y -= 0.35 # Se ajusta la gravedad
        speed.x += 0.50 # Se ajusta la velocidad del proyectil
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    # Se eliminan los objetivos que no han sido alcanzados
    for target in dupe:
        if abs(target - ball) > 13: # Se ajusta el radio de impacto
            targets.append(target) # Se añade el objetivo a la lista de objetivos

    draw()

    
    for target in targets:
            if not inside(target):
                return
            

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
