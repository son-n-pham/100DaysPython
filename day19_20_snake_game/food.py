from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, screenWidth, screenHeight):
        super().__init__()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.Appear()

    def Appear(self):
        self.setpos(random.randint(-self.screenWidth//2, self.screenWidth//2), random.randint(-self.screenHeight//2, self.screenHeight//2))
