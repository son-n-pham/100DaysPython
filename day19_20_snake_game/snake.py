from turtle import Turtle
import time

class BodyPart(Turtle):
    def __init__(self, index):
        super().__init__()
        self.shape("square")
        self.penup()
        self.index = index

class Snake():
    def __init__(self):
        self.body = []
        self.Initiate()
        self.head = self.body[0]

    def Initiate(self):
        for i in range(3):
            self.body.append(BodyPart(i))
            self.body[i].setpos(x=-i*20,y=0)

    def HeadLeft(self):
        self.head.left(90)

    def HeadRight(self):
        self.head.right(90)

    def Moving(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].setpos(self.body[i-1].xcor(), self.body[i-1].ycor())
        self.head.forward(20)

    def Eating(self):
        self.body.append(BodyPart(len(self.body)))
        self.body[len(self.body)-1].setpos(self.body[len(self.body)-2].xcor(), self.body[len(self.body)-2].ycor())