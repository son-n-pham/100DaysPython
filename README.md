## Introduction
This repo is for practice Python projects from 100 Days of Python Code by Angela Yu. The importance of learning coding is to practice, take note, and practice again. Even though I have been through most of the projects in this course; however, I still cannot remember them after a while. Therefore, I decide to go through them again, also put them up into this GitHub repo with more notes about the importances of each projects and what I learn / like / or believe they are important.

The repo will have sub-folder for each project. In each folder, there will be a folder for the starting files for the project, the completed-code folder and also the folder with exe file from the python code.

## Day 54

Hello world website can be created quickly from Flask website:
https://flask.palletsprojects.com/en/2.0.x/quickstart/

### Function decorator

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

### Flask basic syntax with app.route
<a href="https://github.com/son-n-pham/Python_100Days/blob/main/day54_first_website_with_flask/hello.py">Flask basic syntax</a>


## Day 55
### wrapper with paramaters

```Python
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    # Different from wrapper in the previous day, this wrapper has parameters of *args and **kwargs
    def wrapper(*args, **kwargs):
        # As we know that the function is create_blog_post with only one parameter user, the args[0] will be corresponding with that user input. The state of args[0].is_logged_in is checked to run the function with that user or not.
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


# We would like to check if the user logged before executing this function, which has parameter user. This is done by the decorator @is_authenticated_decorator
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}.")



# Create_blog_post() gives nothing with this new_user1 as its is_logged_in is False
new_user1 = User("Son")
create_blog_post(new_user1)


# Create_blog_post() print out the statement in the console with this new_user2 as its is_logged_in is set to True before calling that create_blog_post()
new_user2 = User("Hanh")
new_user2.is_logged_in = True
create_blog_post(new_user2)
```

## Day 56
Complete 2 projects which are my personal site and my name card


## Day 57
Jinja is used to render the html template:
- {{ }} is usually to insert Python code in html file
- To run Python codes requiring imported libraries, it is better to run those codes in the python file, then send the results to html.
  - In the python file, after the template file, we can add keyword and its value
  
    ![image](https://user-images.githubusercontent.com/79841341/149652077-397466df-d83c-48ee-b013-4bdda1b0603d.png)
  
  - Then the html can use {{ }} with the keyword to access the value of that keyword.

    ![image](https://user-images.githubusercontent.com/79841341/149652010-f037ab03-79ae-460b-a9a7-b70d915acb9c.png)

  - And here is the result:

    ![image](https://user-images.githubusercontent.com/79841341/149652033-7c1d460e-67cc-4bbd-a03d-b85382e2970d.png)

- To run for loop or if condition in html file, below is an example to render even integers from 0 to 9

  ```Python
  {% for i in range(0,10): %}
    {%if i%2==0: %}
        <h1>{{ i }} </h1>
    {% endif %}
  {% endfor %}
  ```
- {{ url_for("python_function", \*\*kwargs) }} is used to redirect with paramaters from kwargs. Below is an example.

![image](https://user-images.githubusercontent.com/79841341/149656765-22b838f3-ee51-45cf-94bc-456b18c71af7.png)

## Day 58: Review Bootstrap

Grid in Bootstrap:
- Screen width in bootstrap is equal to 12.
- Example of the grid syntax with bootstrap. In the large screensize (lg), each column size is 3, thus there are 4 columns in a row. When the screensize is smaller (md), each column has the size of 4, thus there are 3 columns in a row. When the screensize is small (sm), each column has the size of 6, thus there are 2 columns in a row.

```CSS
<div class="row">
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:yellow; border:1px solid;">col-lg-3 col-md-4 col-sm-6</div>
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:yellow; border:1px solid;">col-lg-3 col-md-4 col-sm-6</div>
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:yellow; border:1px solid;">col-lg-3 col-md-4 col-sm-6</div>
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:yellow; border:1px solid;">col-lg-3 col-md-4 col-sm-6</div>
</div>
```

Container:
- container vs container-fluid:
  - Both container and container-fluid make the block div responsive; container-fluid, however, make block to be full-width always.
  
  
