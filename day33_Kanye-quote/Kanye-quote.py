from tkinter import *
from glob import glob
import os
import requests

def searchFile(fileName):
    # Create pathname variable to store the current folder of py file
    # If running from the command line, it is still give the current folder of py file
    pathname = os.path.dirname(sys.argv[0])      
    return glob(pathname + "/**/" + fileName, recursive=True)[0]

def get_quote():
    # Connect to kanye API
    response = requests.get(url="https://api.kanye.rest/", verify=False)
    response.raise_for_status()

    # Dump downloaded quote from the API to json, then extract the "quote" in the json library
    kanyeQuote = response.json()["quote"]

    # Update text in the canvas with the new 
    canvas.itemconfig(quote_text,text=kanyeQuote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=searchFile("background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=searchFile("kanye.png"))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()