from flask import Flask

app = Flask(__name__)

#Practice decorator by creating the make_bold decorator
def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}<b>"
    return wrapper_function

#This is to use the decorator to redirect the user to the design webpage, here is root webpage
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#This is to use the decorator to redirect the user to the design webpage, here is root/bye webpage.,
@app.route("/bye")
@make_bold
def bye():
    return "<p>Goodbye, see you later.</p>"

#This is the extension, which we can cast the variable in the function into the URL by using the <>
@app.route("/username/<name>")
def greeting(name):
    return f"Hello {name+12}"

#We can add string before and/or after the <variable>
@app.route("/username/<name>/1")
def greeting_1(name):
    return f"Hello {name}"


# Variable rules: Optionally, we can use converter to specify the type of the argument <converter:variable_name>
# string is the default, others are int, float, path and uuid
# path like string but also accepts slashes
# We can use path to include everything from that point as the variable.
# When running 127.0.0.1:5000/Son/3, we get the result Additional Path: Hello Son/3
@app.route("/<path:name>")
def path_greeting(name):
    return f"Additional path: Hello {name}"

#This return "Hello Son with ID of 3" when running URL "127.0.0.1:5000/Son/3
@app.route("/username/<name>/<int:number>")
def two_variable_greeting(name, number):
    return f"Hello {name} with ID of {number}"


if __name__ == "__main__":
    #If running app.run(), debug mode is off as default. To turn the debug mode on, just do the syntax app.run(debug=True)
    app.run(debug=True)