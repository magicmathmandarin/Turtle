import turtle

v=turtle.Pen()
v.shape("turtle")

v.speed(0)

#1. a loop for drawing a series of circles that are seashell-like

for i in range(50):
	v.circle(i*3)
	v.left(10)

#2. a loop for drawing a red rose
v.reset()
v.color("red")
v.width(4)

for i in range(40):
	v.circle(i*3,180) ##radius=i*3 and draw 1/2 of circle because 1/2=180/360
	v.right(45)

v.reset()

v.color("green")

v.width(5)

for i in range(100):
	v.forward(i*2)
	v.circle(i*2,90)
	v.right(20)
#4. defining a function to draw squares so that we don't have to type the loop again and again

def square(size): ##to define the function
	for i in range(4):
		v.forward(size)
		v.left(90)

square(100)
##to call the function and make it work

#5. use the square function we have defined and draw lots of "random" squares

import turtle
v=turtle.Pen()
import random
def square(size):
	for i in range(4):
		v.forward(size)
		v.left(90)
square(100)
colorList=["red","purple","yellow","green","orange","blue","brown","grey"]
v.speed(0)
v.width(5)
for i in range(100):
	col=random.choice(colorList)
	v.color(col)
	x=random.randrange(-200,200)
	y=random.randrange(-200,200)
	v.up()
	v.goto(x,y)
	v.down()
	size=random.randrange(10,200)
square(size)