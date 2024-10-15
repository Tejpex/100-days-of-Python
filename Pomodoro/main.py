import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def handle_start():
    global reps
    if reps == 0:
        start_timer()


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if len(str(seconds)) < 2:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        marks = ""
        for _ in range(math.ceil(reps / 2)):
            marks += "✔ "
        checkmarks.config(text=marks)
        if reps == 8:
            window.after_cancel(timer)
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=410, height=334)
window.config(padx=100, pady=50, bg=YELLOW)

title = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title.grid(row=0, column=1)

canvas = tk.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = tk.Button(text="Start", font=("Arial", 14), cursor="hand2", command=handle_start)
start_btn.grid(row=2, column=0)

reset_btn = tk.Button(text="Reset", font=("Arial", 14), cursor="hand2", command=reset_timer)
reset_btn.grid(row=2, column=2)

checkmarks = tk.Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

window.mainloop()
