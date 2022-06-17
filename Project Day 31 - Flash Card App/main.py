from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Courier", 30, "italic")
WORD_FONT = ("Courier", 40, "bold")

current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#function used to show the next card
def next_card():
    global current_card
    global timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(language, text="French", fill = "black")
    canvas.itemconfig(word, text=current_card["French"], fill= "black")
    canvas.itemconfig(card_image, image = front_img)
    timer = window.after(3000, func=flip_card)

#function that flips a card
def flip_card():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(language, text="English", fill = "white")
    canvas.itemconfig(word, text=current_card["English"], fill = "white")

#function that checks if the user know the word
#if they do, that word is removed from the "words-to-learn" file
def user_knows():
    if len(to_learn) == 0:
        messagebox.showinfo(title="Oops!", message="No More Words in the Database!")
    else:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()


#creating the program window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady = 50, bg = BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

#creating card images for later use
front_img = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

#creating the canvas
canvas = Canvas(width = 800, height = 526, background= BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image= front_img)
language = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word = canvas.create_text(400, 263, text="word", font = WORD_FONT)

canvas.grid(column=0, row=0,columnspan = 2)

#creating a button that the user clicks when they guess INCORRECTLY
incor_image = PhotoImage(file = "images/wrong.png")
incor_button = Button(image= incor_image, highlightthickness=0, command= next_card)
incor_button.grid(column=0,row=1)

#creating a button that the user clicks when they guess CORRECTLY
cor_image = PhotoImage(file="images/right.png")
cor_button = Button(image=cor_image, highlightthickness=0, command= user_knows)
cor_button.grid(column=1, row=1)

#this function call is made so that a starting card is shown
next_card()

window.mainloop()

