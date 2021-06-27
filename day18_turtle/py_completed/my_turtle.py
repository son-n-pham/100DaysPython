from turtle import Turtle, Screen
import turtle
import random
import colorgram
import os
import glob

# Practice not only turtle but class and class inheritance
class MyTurtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")

    def DrawSquare(self, side=100, angle=90):
        for i in range(4):
            self.forward(side)
            self.right(angle)

    def DrawDashLine(self, dashLineLength=500, lineLength=5, spaceLength=2):
        distance = 0
        while distance < dashLineLength:
            self.forward(lineLength)
            self.penup()
            self.forward(spaceLength)
            self.pendown()
            distance += lineLength + spaceLength

    def DrawRandomShape(self, side=100, initNumberOfSide=3):
        turtleColor = ["red", "orange", "blue", "purple", "yellow", "black", "green"]
        numberOfSide = initNumberOfSide
        while True:
            self.pencolor(random.choice(turtleColor))
            for i in range (numberOfSide):
                self.forward(side)
                self.right(360/numberOfSide)
            numberOfSide += 1

    def RandomColor(self):
        turtle.colormode(255)
        self.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    def RandomWalk(self, length=20):
        #Comment out this list of color as the colormode is more advance.
        #turtleColor = ["red", "orange", "blue", "purple", "yellow", "black", "green"]

        #To use the color randomly, we use colormode of turtle class to set it to 255,
        #then we can use the random.randint in the while loop
        #turtle.colormode(255)

        direction = [0, 90, 180, 270]
        self.pensize(10)
        self.speed("fast")
        self.hideturtle()
        while True:
            #self.pencolor(random.choice(turtleColor))
            #self.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

            self.RandomColor()
            turtleHeadingAngle = self.setheading(random.choice(direction))
            self.forward(length)

    def spiroGraph(self, rotatingAngle=10, circleRadius=100, turtleSpeed="fastest"):
        currentAngle=0
        while True:
            self.speed(turtleSpeed)
            self.setheading(currentAngle)
            self.RandomColor()
            self.circle(circleRadius)
            currentAngle += rotatingAngle
            if currentAngle%360<=3:
                break

    def HirstPainting(self, dotSize=10, dotSpace=20,size=300, colorNumber=6, fileName = 'hirst_picture.jpg'):
        currentFolder = os.getcwd()
        filePath = glob.glob(currentFolder + "/**/" + fileName, recursive=True)
        imagePath = filePath[0]
        #Extract colorNumber colors from a picture by cologram package
        colorExtracted = colorgram.extract(imagePath, colorNumber)
        
        turtle.colormode(255)

        self.speed("fastest")
        def localRotate(i):
            if i%2==0:
                self.right(90)
            else:
                self.left(90)

        def dotLine():
            self.pendown()
            self.dot(dotSize,random.choice(colorExtracted).rgb)
            self.penup()
            self.forward(dotSpace)

        self.penup()
        self.setpos(-size/2, size/2)
        self.pendown()

        for i in range(size//dotSpace+1):
            for j in range(size//dotSpace):
                dotLine()
            localRotate(i)
            dotLine()
            localRotate(i)

    def keyDraw(self):
        def TurtleForward():
            self.forward(10)
        def TurtleBackward():
            self.backward(10)
        def TurtleGoRight():
            self.right(10)
            TurtleForward()
        def TurtleGoLeft():
            self.left(10)
            TurtleForward()
        turtle.listen()
        turtle.onkey(TurtleForward,"d")
        turtle.onkey(TurtleBackward,"a")
        turtle.onkey(TurtleGoRight,"s")
        turtle.onkey(TurtleGoLeft,"w")
            
tim = MyTurtle()

#Challenge 1: Draw Square
#tim.DrawSquare()

#Challenge 2: Draw Dash Line
#tim.DrawDashLine()

#Challenge 3: Draw different shapes with increasing numbers of sides and random colors
#tim.DrawRandomShape()

#Challenge 4: Random walk
#tim.RandomWalk()

#Challenge 5: Draw a Spirograph
#tim.spiroGraph(13)

#Challenge 6: Hirst painting
#tim.HirstPainting(size=500)

#Challnge 1 of Day 18: Turtle reacts to key press
tim.keyDraw()

screen = Screen()
screen.exitonclick()