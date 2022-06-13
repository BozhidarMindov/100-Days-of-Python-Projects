import math
from tkinter import *
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
def timer_reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig.config(timer_text, text="00:00")
    check_mark_label.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8==0:
        timer_label.config(text="Long break!", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 ==0:
        timer_label.config(text="Short break!", fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work!", fg= GREEN)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark = ""
            work_sessions = math.floor(reps/2) 
            for _ in range(work_sessions):
                check_mark += "✔️"
            check_mark_label.config(text=check_mark)
# ---------------------------- UI SETUP ------------------------------- #

#creating the window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


#creating the actual canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row = 1)

#creating a timer label that will be on the top, center part of the screen
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg= YELLOW, highlightthickness=0)
timer_label.grid(column = 1, row = 0)

#creating a start button
start_button = Button(text="Start", width=12,command=start_timer)
start_button.grid(column=0, row=2)

#creating a reset button
reset_button = Button(text="Reset", width=12, command=timer_reset)
reset_button.grid(column = 2, row=2)

#creating a check mark label
check_mark_label = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark_label.grid(column=1, row=3)


window.mainloop()