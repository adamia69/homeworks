from turtle import *
#drawing a square
speed(40)
width(7)
color("green")
fillcolor("pink")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#drawing a door


forward(70)
color("blue")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()

goto(200, 200)
pendown()

#roof 
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

penup()

goto(0, 140)
pendown()
color("yellow")
begin_fill()
left(120)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()

penup()
goto(200, 140)
pendown()
color("yellow")
begin_fill()
right(360)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()

exitonclick()