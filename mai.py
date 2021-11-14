#a python program to increase personal efficiency by allowing work for 25 minutes then giving a 5 minute break. After 4 cycles a long break of 20 minutes is awarded 
from tkinter import *

#constants
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
marks = ""

#timer reset
def reset_timer():
    global marks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text = "TIMER")
    check_marks.config(text=marks)





#timer mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_min)
        title_label.config(text = "LONG BREAK",fg =RED)

    elif reps % 2 == 0:
        count_down(short_break_min)
        title_label.config(text = "SHORT BREAK",fg = PINK)

    else:
        count_down(work_sec)
        title_label.config(text = "WORK TIME",fg = GREEN)






#countdown mechanism
def count_down(count):

    global timer
    global marks
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        for _ in range(reps//2):
            marks += "c"
        check_marks.config(text = marks)


#UI setup
window = Tk()
window.title("POMODORO")
window.config(padx = 100,pady = 50,bg = YELLOW)


title_label = Label(text = "Timer",fg = GREEN,bg = YELLOW ,font = (FONT_NAME,40))
title_label.grid(column = 1,row = 0)



#creat canvas

canvas = Canvas(width = 200, height = 224,bg=YELLOW, highlightthickness = 0)
tomato_pic = PhotoImage(file= "tomato.png")
canvas.create_image(100,112, image = tomato_pic)
canvas.grid(column = 1,row = 1)
timer_text = canvas.create_text(103,112,text = "00:00",fill = "red",font = (FONT_NAME,35,"bold"))


start_button = Button(text = "Start",highlightthickness = 0,command = start_timer)
start_button.grid(column = 0,row = 2)

reset_button = Button(text = "Reset",highlightthickness = 0,command = reset_timer)
reset_button.grid(column = 2,row = 2)

check_marks = Label(fg = RED,bg = YELLOW, highlightthickness = 0)
check_marks.grid(column = 1, row = 3)


window.mainloop()