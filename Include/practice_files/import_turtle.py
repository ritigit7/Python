from turtle import *
import turtle
color("blue")           #created line in blue color
print(position())
title("All codes")
speed(2)
forward(100)            # 100  is a distance
print(position())
backward(100)
right(90)               # here 90 is angle
forward(100)
left(90)
stamp()                 #it put stamp of pointer at the point
forward(100)
goto(x=0,y=0)           # the pointer goto the givin cordinate
setx(200)
sety(200)
print(position())
setheading(90)          #to change pointer direction
home()                  #bring pointer to 0,0 cordinate
fillcolor("yellow")        #if fill color in the shape
begin_fill()
circle(radius=100,extent=360,steps=6)#radius 100 means length is 100,
                                     #extent means is angle 360 degree 
                                     #steps means how much step to complete the circle
end_fill()
dot(50,"red")           # it create dot with size 50 and red color
print(xcor())
clearstamps()
print(round(xcor(),5))  #round is use to ruond up number round(a,b)-->a is float number,
                        #b is digit of number 
undo()                  #it will undo last step
penup()                 #no drawing when pen is up
forward(50)
penup()                 #no drawing when pen is up
pendown()               #drawing when pen is down
pencolor("red")
forward(100)
pencolor("#33cc8c")
pensize(5)
print(isdown())         #it return True or false if pen is down
left(150)
forward(100)
forward(100)
color("red","blue")     #in bracket first one is indicate the pencolor and second one is 
                        #indicate fillcolor
hideturtle()            #hide the turtle 
pensize(0)            
pencolor("black")
right(90)
forward(200)
showturtle()
shape("arrow")          #to change the shape of turtle
shapesize(0.5,1,0.5)    #in this function first one is indicate width,
                        #second indicate lingth,thrid is indicate corner round
right(90)
# shape("classic")
forward(100)
def turn(x,y):
    right(90)
    forward(100)
onclick(turn)           #onclick is used to do some function on clicking
                        #it has 3 atributes first function 
                        # second btn=botten third add
                        #clicking on turtle pointer

class fun(Turtle):
    def f1(self,x,y):
        self.forward(100)
    def f2(self,x,y):
        self.left(90)
t=fun()
onclick(t.f1)
onrelease(t.f2)
forward(100)
# exitonclick()           #exit the turtle popop box by clicking
# heading(1)            # i think it is use to end the screen after it complitation
done()