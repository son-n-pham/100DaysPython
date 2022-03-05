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
- render_template is used to call html file. The render_template looks for html file in templates folder. The below renders index.html and pass the template variable grocery_list to that index.html. That grocery_list is set to variable items in python file.

```python
return render_template("index.html", grocery_list=items)
```


- {{ }} is usually to insert Python code in html file
- To run Python codes requiring imported libraries, it is better to run those codes in the python file, then send the results to html.
  - In the python file, after the template file, we can add keyword and its value
  
    ![image](https://user-images.githubusercontent.com/79841341/149652077-397466df-d83c-48ee-b013-4bdda1b0603d.png)
  
  - Then the html can use {{ }} with the keyword to access the value of that keyword.

    ![image](https://user-images.githubusercontent.com/79841341/149652010-f037ab03-79ae-460b-a9a7-b70d915acb9c.png)

  - And here is the result:

    ![image](https://user-images.githubusercontent.com/79841341/149652033-7c1d460e-67cc-4bbd-a03d-b85382e2970d.png)

### Variable Rules

<variable_name> can be used to bind the address's component into the view as function

The below can pass user_name and order_id into view function orders. Enforcement of types of variables is optional, which order_id is forced to be integer type

```python
@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'
```

### Variable Filters
- Filters are used by the template engine to act on template variables
- Syntax {{ variable | filter_name }}
- Filter option:
  - title: Capitalizes the first letter of each word in a string, known as titlecase
  - capitalize: Capitalizes the first character of a string, such as in a sentence
  - lower/uppercase: Makes all the characters in a string lowercase/uppercase
  - int/float: Changes any number variable to an integer/float
  - default: Defines a default string if the variable is not defined
  - length: Calculates the length of a string, list or dictionary variable
  - dictsort: Sorts a dictionary by its keys

### Loop
- To run for loop or if condition in html file, below is an example to render even integers from 0 to 9

  ```Python
  {% for i in range(0,10): %}
    {%if i%2==0: %}
        <h1>{{ i }} </h1>
    {% endif %}
  {% endfor %}
  ```

### Route Selection
{{ url_for("python_function", \*\*kwargs) }} is used to redirect with paramaters from kwargs. Below is an example.

![image](https://user-images.githubusercontent.com/79841341/149656765-22b838f3-ee51-45cf-94bc-456b18c71af7.png)

### Inheritance
- We can create a html file as the template, then create other html file using that template.
- The template html file has the template layout/data/info. Inside it, there is a block of {%block content%}  {% endblock %}

```html
// This is the content of the template html file base.html
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
  {% block content %}{% endblock %}
  </body>
</html>
```

- The other html files, which use that template, need to have 

```html
{% extends "base.html"  %} // Inherit the above html file named base.html
 
{% block content %}
    <p>This is my paragraph for this page.</p> // Its own contents is here
{% endblock %}
```

The inherited html file would have the content as below because it is inheriting from the base.html.
```html
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
    <p>This is my paragraph for this page.</p>
  </body>
</html>
```

### Flask Forms by Flask request object
- The object **request** is used to retrieve the input data of the form.
- By the default, flask route only supports GET requests. To get data from the form, the flast route must have method=[\"GET\",\"POST\"]

This is from the app.py which render index.html. In which, flask.request is imported. request.form is used to retrieve data from a specific form based on the input's name of the form.

```python
from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  new_id = len(recipes) + 1
  if len(request.form) > 0:
    #### Add the recipe name to recipes[new_id] 
    recipes[new_id] = request.form["recipe"]
    #### Add the recipe description to descriptions[new_id]
    descriptions[new_id] = request.form["description"]
    #### Add the values to new_ingredients and new_instructions
    new_ingredients = request.form["ingredients"]
    new_instructions = request.form["instructions"]
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
  return render_template("index.html", template_recipes=recipes)
```

Here is the index, which inherits base.html

```html
{% extends "base.html" %}
{% block content %}
  <h1>Cooking By Myself</h1>
  <p>Welcome to my cookbook. These are recipes I like.</p>
  {% for id, name in template_recipes.items() %}
    <p><a href="/recipe/{{ id }}">{{ name }}</a></p>
  {% endfor %}

  <form action="/" method="POST">
    <h3>Add Recipe</h3>
    <p>
      <label for="recipe">Name:</label>
      <input type="text" name="recipe"/>
    </p>
    <p>
      <label for="description">Description:</label>
      <textarea name="description"></textarea>
    </p>
    <p>
      <label for="ingredients">Ingredients:</label>
      <textarea name="ingredients"></textarea>
    </p>
    <p>
      <label for="instructions">Instructions:</label>
      <textarea name="instructions"></textarea>
    </p>
    <p><input type="submit" name="submit_recipe"/></p>
  </form>
{% endblock %}
```

### Flask Forms by FlaskForm class

We need to create our own Flask form inherit from FlaskForm

```python
from flask import Flask, render_template

# This is for Flask forms by FlaskForm class
from flask_wtf imoprt FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# This is for protecting from CSRF (Cross Site Request Forgery)
app.config["SECRET_KEY"] = "my_secret"

class MyForm(FlaskForm):

    # This is equal to <input type=text...
    my_textfield = StringField("TextLabel")
    
    # This is equal to <input type=submit...
    my_submit = SubmitField("SubmitName")

# Then Flask route can use MyForm by creating its instance, and assign it in render_template

@app.route("/", method=["GET", "POST"])
def my_route():
    flask_form = MyForm()
    return render_template("mytemplate", template_form=flask_form)
```

In the template, the form can be written as below

```html
<form action="/" method="post">
    
    # This is for CSRF
    {{ template_form.hidden_tag() }}
    
    # Render the label of my_textfield, which is "TextLabel"
    {{ template_form.my_textfield.label }}
    
    # This is for inputting text
    {{ template_form.my_textfield() }}
    
    # This is for clicking to submit
    {{ template_form..my_submit() }}
    
</form>
```

Once the form is submitted, the input data is sent back to server. Python file can be rewritten as below to receive the input data.

```python
from flask import Flask, render_template

# This is for Flask forms by FlaskForm class
from flask_wtf imoprt FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# This is for protecting from CSRF (Cross Site Request Forgery)
app.config["SECRET_KEY"] = "my_secret"

class MyForm(FlaskForm):

    # This is equal to <input type=text...
    my_textfield = StringField("TextLabel")
    
    # This is equal to <input type=submit...
    my_submit = SubmitField("SubmitName")

# Then Flask route can use MyForm by creating its instance, and assign it in render_template

@app.route("/", method=["GET", "POST"])
def my_route():
    # Initiate the instance flask_form of MyForm class
    flask_form = MyForm()
    
    # Input text from my_textfield is assigned to new_textfield variable
    new_textfield = flask_form.my_textfield.data
    
    # Render mytemplate from templates folder with a flask variable template_form
    return render_template("mytemplate", template_form=flask_form)
```

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
  
  
