from turtle import *
from random import randrange
from freegames import square, vector
import time
import colored

red=colored.fg('red')
yellow=colored.fg('yellow')
purple=colored.fg('magenta')
reset=colored.attr('reset')
print('')
time.sleep(0)
print(red+'This Game was Created By :')
print(yellow+'                           Script Kiddie Tamil')
print(purple+'                           https://www.youtube.com/c/ScriptKiddieTamil'+reset)
print('')
print('Game starts in 3Sec be ready :) ')
print('')
time.sleep(3)
print('')

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -290 < head.x < 320 and -290 < head.y < 320

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        point=len(snake)-1
        print('Point:', point)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
