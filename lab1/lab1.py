print('jack'*3)
number1 = 29
print(number1)
number2 = number1/2
print(number2)
lst=[24,11,2002]
print(lst[0]),print(lst[0]*2)
print(lst[1]),print(lst[1]*2)
print(lst[2]),print(lst[2]*2)
import turtle
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.circle(150)

turtle.penup()
turtle.begin_fill()
turtle.goto(100,100)
turtle.pendown()
turtle.circle(50)
turtle.mainloop()