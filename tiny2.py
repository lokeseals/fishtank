import math
import turtle
import random
import time
import os

turtle.tracer(False)
turtle.setundobuffer(None)
turtle.pu()

s = turtle
s.begin_poly()
s.goto(0,0)
s.goto(10,20)
s.goto(10,-20)
s.goto(0,0)
s.end_poly()
m1 = s.get_poly()

s.begin_poly()
s.circle(6)
s.end_poly()
m2 = s.get_poly()

s.goto(0,8)
s.begin_poly()
s.circle(2)
m3 = s.get_poly()

s.goto(0,8)
s.begin_poly()
s.circle(1)
m4 = s.get_poly()

petshape = turtle.Shape("compound")
petshape.addcomponent(m1,"orange")
petshape.addcomponent(m2,"blue")
petshape.addcomponent(m3,"white")
petshape.addcomponent(m4,"black")
s.getscreen().register_shape("pet", petshape)

petshape2 = turtle.Shape("compound")
petshape2.addcomponent(m1,"orange")
petshape2.addcomponent(m2,"red")
petshape2.addcomponent(m3,"white")
petshape2.addcomponent(m4,"black")
s.getscreen().register_shape("pet2", petshape2)

food = turtle.clone()
food.shape("circle")
food.shapesize(0.4)
food.goto(0,400)

turtle.shape("circle")
turtle.pu()
turtle.shapesize(0.5)

count = 0

players = []

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="pet")
        self.pu()
        self.color("red")
        self.speed = random.randint(70,130)/100.0
        self.move = True
        self.shapesize(random.random() + 0.5)

for i in range(50):

    t = Player()
    players.append(t)

def left():

    turtle.goto(turtle.xcor()-10,turtle.ycor())

def right():

    turtle.goto(turtle.xcor()+10,turtle.ycor())

def up():

    turtle.goto(turtle.xcor(),turtle.ycor()+10)

def down():
    
    turtle.goto(turtle.xcor(),turtle.ycor()-10)

def space():

    #food.goto(random.randint(-200,200),280)
    food.goto(turtle.xcor(), turtle.ycor() + 20)

turtle.onkey(space,"space")
turtle.onkey(left, "Left")
turtle.onkey(right,"Right")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")

turtle.listen()

fish_phrases = ["Thank you","Aquaman save the Queen",
                "We are fish","Red fish angry blue fish happy"]

go = True

fish_board = turtle.clone()
fish_board.hideturtle()
fish_board.goto(-290,300)
fish_board.color("red")
fish_board.write("Angry Fish", font=("Arial", 16, "bold"), align="center")

while(go):

    if count % 1000 == 0:

        food.goto(turtle.xcor(), turtle.ycor() + 20)

    red_fish = 0

    for t in players:

        if (t.shape() == "pet2"):

            red_fish += 1

        if t.shapesize()[0] > 0.01:
            t.shapesize(t.shapesize()[0] - 0.00001)

        if t.shapesize()[0] < 0.90 and t.shape() != "pet2":

            t.shape("pet2")

        if t.shapesize()[0] > 1.0 and t.shape() != "pet":

            t.shape("pet")

        if food.ycor() < 300 and t.ycor() > 0:
            
            t.setheading(t.towards(food.pos()))

        t.right(math.sin(count)*5)
        t.right(random.randint(-1,1))

        if abs(food.xcor() - t.xcor()) < 5 and abs(food.ycor() - t.ycor()) < 5:
            
            random.shuffle(fish_phrases)
            os.popen("say " + fish_phrases[0])
            
            t.shapesize(t.shapesize()[0] + 0.5)
            t.speed += 0.2
            food.goto(0,400)
            
        t.forward(t.speed)
            
        if abs(t.xcor()) > 300:
            t.right(45)

        if abs(t.ycor()) > 300:
            t.right(45)

        if abs(t.xcor()) > 400 or abs(t.ycor()) > 400:
            t.goto(0,0)
            
        #turtle.setheading(turtle.towards(t.pos()))
        #turtle.forward(0.4)

        if turtle.xcor() > 300:
            turtle.goto(-300, turtle.ycor())

        if turtle.xcor() < -300:
            turtle.goto(300, turtle.ycor())

        if turtle.ycor() > 300:
            turtle.goto(turtle.xcor(), -300)

        if turtle.ycor() < -300:
            turtle.goto(turtle.xcor(), 300)

    count+= 1

    fish_board.clear()
    fish_board.write("Angry Fish: " + str(red_fish), font=("Arial", 14, "bold"), align="center")
       
    turtle.update()

turtle.mainloop()
