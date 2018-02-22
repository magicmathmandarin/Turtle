import turtle

v=turtle.Pen()
v.shape("turtle")

v.speed(0)

#1. a loop for drawing a series of circles that are seashell-like

for i in range(50):
	v.circle(i*3)
	v.left(10)

#2. a loop for drawing a red rose
#v.reset()
#v.color("red")
#v.width(2)

for i in range(40):
	v.circle(i*3,180) ##radius=i*3 and draw 1/2 of circle because 1/2=180/360
	v.right(45)

#v.reset()
v.up()
v.forward(40)
v.down()
from turtle import *
v.speed(0)
color('pink', 'green')
begin_fill()
while True:
	    #forward(200)
    forward(250)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
