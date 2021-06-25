from turtle import Turtle, Screen
import turtle
import random
import colorgram



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

    def HirstPainting(self, size=300, colorNumber=6, imagePath = 'C:\Development\python\\100Days_Python\day18_turtle\hirst_picture.jpg'):     
        colorExtracted = colorgram.extract(imagePath, colorNumber)
        for i in colorExtracted:
            print(i.rgb)
        
            

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
tim.HirstPainting()

screen = Screen()
screen.exitonclick()