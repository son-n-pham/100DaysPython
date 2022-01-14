import pandas as pd
from random import randint
import os, sys
from glob import glob
from tkinter import *
import tkinter.font as tkFont

BACKGROUND_COLOR = "#B1DDC6"

# Helper function to search file
def searchFile(fileName):
    # Create pathname variable to store the current folder of py file
    # If running from the command line, it is still give the current folder of py file
    pathname = os.path.dirname(sys.argv[0])      
    return glob(pathname + "/**/" + fileName, recursive=True)[0]

class Words:
    def __init__(self, wordListFile):
        self.wordListFile = searchFile(wordListFile)
        self.wordList = pd.read_csv(self.wordListFile)
        self.firstLangName = self.wordList.columns[0]
        self.secondLangName = self.wordList.columns[1]
        self.firstLangOrigin = self.wordList[self.wordList.columns[0]].tolist()
        self.secondLangOrigin = self.wordList[self.wordList.columns[1]].tolist()
        self.firstLang = self.firstLangOrigin.copy()
        self.secondLang = self.secondLangOrigin.copy()
     
    def RandomWord(self):
        wordsLen = len(self.firstLang)
        if wordsLen>0:
            randomNum = randint(0, len(self.firstLang)-1)
            return (self.firstLang[randomNum], self.secondLang[randomNum])
        else:
            return None

class GUI:
    def __init__(self, Words):
        self.Words = Words
        #self.knownFirstLang = []
        #self.knownSecondLang = []
        #self.unknownFirstLang = []
        #self.unknownSecondLang = []
        self.Design()
        self.randomWord = None

    def Design(self):
        def LangsOnCard(cardSideImg, langName,langWord):
            cardImg = canvas.create_image(0, 0, anchor="nw", image=cardSideImg)
            cardTitleText = canvas.create_text(400,150,text=langName,font=("Ariel",40,"italic"))
            cardWordText = canvas.create_text(400,263,text=langWord,font=("Ariel",60,"bold"))
        def FlipToSecondLang(isKnown):
            cardSideImg = backImg
            langName = self.Words.secondLangName
            langWord = self.randomWord[1]
            LangsOnCard(cardSideImg, langName,langWord)
            if isKnown:
                self.Words.firstLang.remove(self.randomWord[0])
                self.Words.secondLang.remove(self.randomWord[1])
                pd.DataFrame(list(zip(self.Words.firstLang, self.Words.secondLang))).to_csv(os.path.dirname(sys.argv[0])+ '/data/' + 'words_to_learn.csv')
                timer = 1000
            else:
                timer = 3000
            knownBttn["state"] = "disable"
            unknownBttn["state"] = "disable"
            window.after(timer,FlipToFirstLang)
        def FlipToFirstLang():
            self.randomWord = self.Words.RandomWord()            
            if self.randomWord!=None:
                cardSideImg = frontImg
                langName = self.Words.firstLangName
                langWord = self.randomWord[0]
                LangsOnCard(cardSideImg, langName,langWord)
                knownBttn["state"] = "normal"
                unknownBttn["state"] = "normal"
            else:
                cardSideImg = frontImg
                langName = "No more word"
                langWord = "No more word"
                LangsOnCard(cardSideImg, langName,langWord)
                knownBttn["state"] = "disable"
                unknownBttn["state"] = "disable"
        def KnownClick():
            FlipToSecondLang(True)

        def UnknownClick():
            FlipToSecondLang(False)


        window = Tk()
        window.title("Flash Card")
        window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.randomWord = self.Words.RandomWord()

        frontImgFile = searchFile("card_front.png")
        frontImg = PhotoImage(file=frontImgFile)
        backImgFile = searchFile("card_back.png")
        backImg = PhotoImage(file=backImgFile)
        canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        cardImg = canvas.create_image(0, 0, anchor="nw", image=frontImg)
        cardTitleText = canvas.create_text(400,150,text=self.Words.firstLangName,font=("Ariel",40,"italic"))
        cardWordText = canvas.create_text(400,263,text=self.randomWord[0],font=("Ariel",60,"bold"))
        canvas.grid(row=0, column=0, columnspan=2)

        knownImgFile = searchFile("right.png")
        knownImg = PhotoImage(file=knownImgFile)
        knownBttn = Button(image=knownImg, highlightthickness=0, command=KnownClick)
        knownBttn.grid(row=1,column=0)

        unknownImgFile = searchFile("wrong.png")
        unknownImg = PhotoImage(file=unknownImgFile)
        unknownBttn = Button(image=unknownImg, highlightthickness=0, command=UnknownClick)
        unknownBttn.grid(row=1,column=1)

        window.mainloop()

try:
    myWordList = searchFile("words_to_learn.csv")
    myWordList = Words("words_to_learn.csv")
    print("Loading from words_to_learn")
except IndexError:
    myWordList = Words("french_words.csv")
    print("Loading from french_words")
myGUI = GUI(myWordList)