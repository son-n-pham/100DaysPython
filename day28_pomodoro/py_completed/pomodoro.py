from tkinter import *
import tkinter.font as tkFont
from pygame import mixer
from glob import glob
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Helper function to search file
def searchFile(fileName):
    # Create pathname variable to store the current folder of py file
    # If running from the command line, it is still give the current folder of py file
    pathname = os.path.dirname(sys.argv[0])      
    return glob(pathname + "/**/" + fileName, recursive=True)[0]

def playMusic(fileName):
    try:
        mixer.music.load(searchFile(fileName))
        mixer.music.play()
    except:
        pass

class Pomodoro:
    def __init__(self):
        self.reps = 1
        self.checkNum = ""
        self.timer = None
        self.UI()
        
# ---------------------------- UI SETUP ------------------------------- #
    def UI(self):
        # This needs to be run first for other tkinter to run properly.
        window = Tk()

        # Local variable
        buttonFont = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)

        # Enable pygame mixer for playing music
        mixer.init()

        # ---------------------------- TIMER RESET ------------------------------- # 
        def ResetTimer():
            # Turn off music if it is playing
            mixer.music.stop()

            # Stop window after
            window.after_cancel(self.timer)

            # Reset all texts
            timerLabel.configure(text="Timer", fg=GREEN)
            canvas.itemconfig(timerText, text="00:00")
            self.checkNum = ""
            checkerLabel.configure(text=self.checkNum)

            # Reset self.reps
            self.reps = 1

            # Set states of buttons and entry boxes to appropriate states
            startBttn["state"] = "normal"
            resetBttn["state"] = "disable"
            workPeriodEntry["state"] = "normal"
            shortBreakPeriodEntry["state"] = "normal"
            longBreakPeriodEntry["state"] = "normal"

        # ---------------------------- TIMER MECHANISM ------------------------------- # 
        def StartTimer():
            # Helper function to handle input box of work & break periods
            def inputTime(myInput):
                myInputValue = int(float(myInput.get()))
                if myInputValue < 1:
                    myInputValue = 1
                myInput.delete(0,END)
                myInput.insert(0,str(myInputValue))
                return myInputValue

            # Turn off music if it is playing
            mixer.music.stop()

            # Set countDownTime for working time
            startBttn["state"] = "disable"
            resetBttn["state"] = "normal"

            # Set countDownTime for work time
            if self.reps % 2 != 0:
                countDownTime = inputTime(workPeriodEntry) * 60
                timerLabel.configure(text="Work", fg=GREEN)

            # Set countDownTime for long break time
            elif self.reps % 8 == 0:
                playMusic("Comptine d'un autre été l'après.mp3")
                countDownTime = inputTime(longBreakPeriodEntry) * 60
                timerLabel.configure(text="Long Break", fg=RED)

            # Set countDownTime for short break time
            else:
                playMusic("Comptine d'un autre été l'après.mp3")
                countDownTime = inputTime(shortBreakPeriodEntry) * 60
                timerLabel.configure(text="Short Break", fg=PINK)
            
            # Disable all entry box for periods of work and break
            workPeriodEntry["state"] = "disable"
            shortBreakPeriodEntry["state"] = "disable"
            longBreakPeriodEntry["state"] = "disable"

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
                self.timer = window.after(1000,CountDown, count-1)
            elif count == 0:
                self.reps += 1
                if self.reps%2==0:
                    self.checkNum += "🗹"
                checkerLabel.configure(text=self.checkNum)
                StartTimer()
        # -------------------------------------------------------------------------------- # 
        window.title("Pomodoro")
        window.config(padx=100, pady=50, bg=YELLOW)
        timerLabel = Label(text = "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50), justify=CENTER)
        timerLabel.grid(row=0, column=1)
        
        canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        tomato_img = PhotoImage(file=searchFile("tomato.png"))
        canvas.create_image(100,112,image=tomato_img)
        timerText = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
        canvas.grid(row=1, column=1)

        startBttn = Button(text="Start", font=buttonFont, command=StartTimer)
        startBttn.grid(row=2, column=0)

        resetBttn = Button(text="Reset", font=buttonFont, command=ResetTimer)
        resetBttn.grid(row=2, column=2)
        resetBttn["state"] = "disable"

        checkerLabel = Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 40))
        checkerLabel.grid(row=3, column=1)

        workPeriodLabel = Label(text="Work in (mins)", bg=YELLOW)
        workPeriodLabel.grid(row=4, column=0)

        workPeriodEntry = Entry(width=10, justify="center")
        workPeriodEntry.insert(0, WORK_MIN)
        workPeriodEntry.grid(row=5, column=0)

        shortBreakPeriodLabel = Label(text="Short Break in (mins)", bg=YELLOW)
        shortBreakPeriodLabel.grid(row=4, column=1)
        
        shortBreakPeriodEntry = Entry(width=10, justify="center")
        shortBreakPeriodEntry.insert(0, SHORT_BREAK_MIN)
        shortBreakPeriodEntry.grid(row=5, column=1)

        longBreakPeriodLabel = Label(text="Long Break in (mins)", bg=YELLOW)
        longBreakPeriodLabel.grid(row=4, column=2)

        longBreakPeriodEntry = Entry(width=10, justify="center")
        longBreakPeriodEntry.insert(0, LONG_BREAK_MIN)
        longBreakPeriodEntry.grid(row=5, column=2)

        warningLabel = Label(text="To avoid virus, please avoid downloading exe files from unknown sources.", font=("Arial", 9, "italic"), bg=YELLOW)
        warningLabel.grid(row=6, column=0, columnspan=3, pady=20)

        window.mainloop()
        
if __name__ == "__main__":
    pomodoro = Pomodoro()