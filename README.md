## Introduction
This repo is for practice Python projects from 100 Days of Python Code by Angela Yu. The importance of learning coding is to practice, take note, and practice again. Even though I have been through most of the projects in this course; however, I still cannot remember them after a while. Therefore, I decide to go through them again, also put them up into this GitHub repo with more notes about the importances of each projects and what I learn / like / or believe they are important.

The repo will have sub-folder for each project. In each folder, there will be a folder for the starting files for the project, the completed-code folder and also the folder with exe file from the python code.

### Day 54

Hello world website can be created quickly from Flask website:
https://flask.palletsprojects.com/en/2.0.x/quickstart/

#### Function decorator

```Python
import time

# Syntax of delay_decorator
def delay_decorator(function):
    def wrapper_function():
        # Do something before the function
        print("This is the execution before the function(s)")

        # Execute the function as many times as we want. Here we run 2 times
        function()
        function()

        # Do something after the function
        print("This is execution after the function")
        print("--------------------------------")
    return wrapper_function


#Add this @delay_decorator on top of the function to use the decorator with this function
@delay_decorator
def say_hello():
    print("hello")


#Add this @delay_decorator on top of the function to use the decorator with this function
@delay_decorator
def say_goodbye():
    print("goodbye")


def say_greeting():
    print("how are you")


say_hello()

say_goodbye()

#Only this do not have the decorator applied.
say_greeting()
```
  
