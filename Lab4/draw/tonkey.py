import turtle

def move_forward():
    turtle.forward(50)


def turn_left():
    turtle.left(45)


def turn_right():
    turtle.right(45)


def turn_backward():
    turtle.backward(45)


def upwards():
    turtle.up()


def downwards():
    turtle.down()


def clear_screen():
    turtle.clear()


def user_draw():
    turtle.home()
    turtle.clear()
    turtle.onkey(exit, "x")
    turtle.onkey(clear_screen, "c")
    turtle.onkey(turn_backward, "s")
    turtle.onkey(turn_right, "d")
    turtle.onkey(turn_left, "a")
    turtle.onkey(move_forward, "w")
    turtle.onkey(upwards, "f")
    turtle.onkey(downwards, "g")
    turtle.listen()
    turtle.done()
