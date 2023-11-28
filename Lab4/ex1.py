import turtle
from draw.tonkey import user_draw
from alphabet.twrite import draw,sterge_2
from aesthetic.menu import menu, menu_2

t = turtle.Turtle()


def run():
    while True:
        print(menu())
        opt = int(input("Geben Sie Ihre Option ein: "))
        if opt == 0:
            break
        if opt == 1:
            draw()
        if opt == 2:
            sterge_2()
            print(menu_2())
            user_draw()

run()



