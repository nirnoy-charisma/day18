import colorgram
import turtle as t
from turtle import  Screen
import random
rgb_colors = [(247, 227, 212), (183, 16, 40), (239, 73, 46), (232, 62, 81), (239, 114, 88), (171, 40, 50), (187, 62, 43), (240, 170, 157), (219, 124, 129), (251, 195, 199)]
random_color= random.choice(rgb_colors)
scaled_color = (random_color[0] / 255, random_color[1] / 255, random_color[2] / 255)
tim = t.Turtle()
tim.speed(10)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
number_of_dots=101
for dots in range(number_of_dots):

   tim.dot(20,scaled_color)
   tim.forward(50)

   if dots %10==0:
      tim.setheading(90)
      tim.forward(50)
      tim.setheading(180)
      tim.forward(500)
      tim.setheading(0)








my_screen=Screen()
my_screen.exitonclick()