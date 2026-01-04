import turtle
import math


def draw_pythagoras_tree(t, branch_length, level, angle=45):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1, angle)

    t.right(angle * 2)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1, angle)

    t.left(angle)
    t.backward(branch_length)


def main():
    level = int(input("Введіть рівень рекурсії (рекомендовано 5-12): "))

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.title(f"Дерево Піфагора (рівень {level})")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("#8B2323")
    t.pensize(2)

    t.penup()
    t.goto(0, -250)
    t.left(90)
    t.pendown()

    draw_pythagoras_tree(t, 120, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
