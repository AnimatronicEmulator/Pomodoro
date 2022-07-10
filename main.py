from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    pomodoro_checks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 2 == 0:
        time = int(WORK_MIN * 60)
        timer_label.config(text="Work time!", fg=GREEN)
    elif reps != 7:
        time = int(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        time = int(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)

    countdown(time)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    seconds = count % 60
    minutes = int((count - seconds) / 60)

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 0:
            pomodoro_checks.config(text=f"{int(reps / 2) * '✔'}")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 48))
timer_label.config(bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.config(font=("Arial", 14, "bold"), fg=RED, bg="white", borderwidth=1, relief="raised")
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.config(font=("Arial", 14, "bold"), fg=RED, bg="white", borderwidth=1, relief="raised")
reset_button.grid(row=2, column=2)

pomodoro_checks = Label(font=("Arial", 15), bg=YELLOW, fg=GREEN)
pomodoro_checks.grid(row=3, column=1)

window.mainloop()
