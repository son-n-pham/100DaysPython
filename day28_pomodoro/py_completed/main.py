from tkinter import *
from playsound import playsound
from glob import glob
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2

def searchFile(fileName):
    return glob("./" + "/**/" + fileName, recursive=True)[0]

class Pomodoro:
    def __init__(self):
        self.reps = 1
        self.UI_setup()


# ---------------------------- TIMER RESET ------------------------------- # 





# ---------------------------- UI SETUP ------------------------------- #
    def UI_setup(self):
        # ---------------------------- TIMER MECHANISM ------------------------------- # 
        def StartTimer():
            #soundFile = searchFile("piano.mp3")
            #playsound(soundFile, False)
            # Set countDownTime for working time
            if self.reps % 2 != 0:
                countDownTime = WORK_MIN * 60

            # Set countDownTime for short break time
            elif self.reps % 8 != 0:
                countDownTime = LONG_BREAK_MIN * 60

            # Set countDownTime for long break time
            else:
                countDownTime = SHORT_BREAK_MIN * 60
                self.reps = 0

            # Call CountDown function with the set countDownTime
            CountDown(countDownTime)

        # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
        def CountDown(count):
            minute = count//60
            if minute < 10:
                minute = f"0{minute}"
            second = count%60
            if second < 10:
                second = f"0{second}"

            timeDisplay = f"{minute}:{second}"
            canvas.itemconfig(timerText, text=timeDisplay)

            if count>0:
                window.after(1000,CountDown, count-1)
            elif count == 0:
                self.reps += 1
                StartTimer()
        # -------------------------------------------------------------------------------- # 


        window = Tk()
        window.title("Pomodoro")
        window.config(padx=100, pady=50, bg=YELLOW)
        timerLabel = Label(text = "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50), justify=CENTER)
        timerLabel.grid(row=0, column=1)
        
        canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        tomato_img = PhotoImage(file=searchFile("tomato.png"))
        canvas.create_image(100,112,image=tomato_img)
        timerText = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
        canvas.grid(row=1, column=1)



        startBttn = Button(text="Start", command=StartTimer)
        startBttn.grid(row=2, column=0)

        resetBttn = Button(text="Reset")
        resetBttn.grid(row=2, column=2)

        checkerLabel = Label(text="🗹", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 40))
        checkerLabel.grid(row=3,column=1)

        window.mainloop()
        


        

pomodoro = Pomodoro()