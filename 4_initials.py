import turtle

t = turtle.Turtle()

## begin W

t.right(90)
t.forward(100)
t.left(135)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(100)

# move over for next letter

t.penup()
t.back(100)
t.right(90)
t.forward(25)
t.left(90)
t.pendown()

## begin K

t.forward(100)
t.back(50)
t.right(45)
t.forward(70)
t.back(70)
t.right(90)
t.forward(70)

turtle.mainloop()