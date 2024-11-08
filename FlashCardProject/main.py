import tkinter as tk
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
timer = None

# ---------------------------- READ DATA ------------------------------- #
try:
    french_data = pandas.read_csv("./data/french_to_learn.csv")
except FileNotFoundError:
    french_data = pandas.read_csv("./data/french_words.csv")
finally:
    french_words_to_learn = french_data.to_dict(orient="records")


def pick_new_word():
    global timer, current_card
    if timer:
        window.after_cancel(timer)
    current_card = random.choice(french_words_to_learn)

    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    timer = window.after(3000, flip_card, current_card)


def flip_card(card):
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")


def remove_card():
    french_words_to_learn.remove(current_card)
    csv_data = pandas.DataFrame(french_words_to_learn)
    csv_data.to_csv("data/french_to_learn.csv", index=False)
    pick_new_word()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.minsize(width=840, height=570)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="./images/card_front.png")
card_back = tk.PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = tk.PhotoImage(file="./images/wrong.png")
wrong_btn = tk.Button(command=pick_new_word, image=wrong_img, highlightthickness=0, cursor="hand2", borderwidth=0)
wrong_btn.grid(row=1, column=0)

right_img = tk.PhotoImage(file="./images/right.png")
right_btn = tk.Button(command=remove_card, image=right_img, highlightthickness=0, cursor="hand2", borderwidth=0)
right_btn.grid(row=1, column=1)

pick_new_word()
window.mainloop()
