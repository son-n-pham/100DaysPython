from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

SCREEN_WIDTH = SCREEN_HEIGHT = 500

if __name__ == "__main__":
    screen = Screen()
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    #screen.tracer(0) to turn off the automatic screen update.
    #screen is only one at a time with screen.update()
    screen.tracer(0)

    snake = Snake()

    #This is to call even-driven functions of snake by key presses
    screen.listen()
    screen.onkey(snake.HeadLeft,"a")
    screen.onkey(snake.HeadRight,"d")

    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)

    gameIsOn = True

    while gameIsOn:
        screen.update()
        time.sleep(0.1)


        snake.Moving()

        if (abs(snake.head.xcor()-food.xcor()) <= 20) & (abs(snake.head.ycor()-food.ycor()) <= 20):
            snake.Eating()
            food.Appear()

        if (abs(snake.head.xcor())>=(SCREEN_WIDTH)) | (abs(snake.head.ycor())>=(SCREEN_HEIGHT)):
            gameIsOn = False
    
    screen.exitonclick()
