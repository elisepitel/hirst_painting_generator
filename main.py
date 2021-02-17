import turtle
import random
#import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)

franklin = Turtle()
screen = Screen()

screen.setup(width=800, height=800)

franklin.shape("turtle")
franklin.color("forest green")
franklin.speed(9)
franklin.penup()


### Uncomment following code to create list of colors, extracting colors from image.jpg:
#colors = colorgram.extract('image.jpg', 16)
#colors_list = []
#for color in colors:
#    color_rgb = color.rgb
#    color_tuple = (color_rgb.r, color_rgb.g, color_rgb.b)
#    colors_list.append(color_tuple)

### Once list is created within the console, you can save the output with a list of tuple ↓ and comment the code above ↑ 
colors_list = [(234, 62, 100), (233, 149, 88), (248, 218, 97), (2, 180, 212), (162, 53, 97), (236, 121, 146), (1, 132, 167), (236, 79, 66), (111, 190, 153), (2, 155, 100), (86, 191, 211)]
### You might white color's tuples within your list, do not hesitate to test your colors with a Colors RGB calculator 
### (exmpl : https://www.w3schools.com/colors/colors_rgb.asp)


y_position = -200

### Regular point with random color from colors_list: ↓ 
for _ in range(10):
    franklin.setx(-300)
    franklin.sety(y_position)
    for _ in range(10):
        franklin.forward(50)
        franklin.dot(20, random.choice(colors_list))
        y_position += 5

franklin.hideturtle()

screen.exitonclick()
