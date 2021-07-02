import tkinter

class Distance_Converter:
    def __init__(self):
        self.labelMiles = "Miles"
        self.labelKm = "Km"
        self.labelEqual = "is equal to"
        self.labelCalculate = "Calculate"
        self.labelResult = ""
        self.Execute()
    def Execute(self):
        window = tkinter.Tk()
        window.title("Converter from Miles to Km")
        window.minsize(width=200, height=200)

        entry = tkinter.Entry(width = 10)
        entry.config(justify='center')
        entry.grid(column=1, row=0)

        labelMiles = tkinter.Label(text=self.labelMiles)
        labelMiles.grid(column=2, row=0)

        labelEqual = tkinter.Label(text=self.labelEqual)
        labelEqual.grid(column=0, row=1)

        labelResult = tkinter.Label(text=self.labelResult)
        labelResult.grid(column=1, row=1)

        labelKm = tkinter.Label(text=self.labelKm)
        labelKm.grid(column=2, row=1)

        #button
        #config is used to update the text of the label
        def UnitConverter():
            labelResult.config(text=f"{round(float(entry.get())*1.6,2)}")

        buttonConvert = tkinter.Button(text="Convert", command=UnitConverter)
        buttonConvert.grid(column=1, row=2)

        window.mainloop()

if __name__ == "__main__":
    converter = Distance_Converter()