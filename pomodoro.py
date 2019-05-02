#!/usr/bin/env python3

"""
Pomodoro.py
Created by Guido Minieri
Date - June 2017
My personal take on the most popular productivity tool out there.
"""


import tkinter as tk


def count(timer):
    """
    Countdown
    """
    global IS_BREAK
    global job
    global SESS_COUNTER

    ask = tkinter.messagebox.askquestion

    if timer <= -1:

        # toggle IS_BREAK
        IS_BREAK = not IS_BREAK

        # prompt and start new session
        if IS_BREAK and SESS_COUNTER % 4 != 0:
            prompt_answer = ask("Session Ended!", "Are you ready for a break?", icon='question')
        elif IS_BREAK and SESS_COUNTER % 4 == 0:
            prompt_answer = ask("4 POMODORI!", "Do you want a long break", icon='question')
        else:
            prompt_answer = ask("Time's up!", "Ready for a new session?", icon='question')



        if prompt_answer == 'yes' and SESS_COUNTER % 4 != 0 and IS_BREAK:
            root.after_cancel(job)
            count(SHORT_BREAK)
        elif prompt_answer == 'yes' and SESS_COUNTER % 4 == 0 and IS_BREAK:
            root.after_cancel(job)
            count(LONG_BREAK)
        elif prompt_answer == 'no':
            stop_count()
        else:
            SESS_COUNTER += 1
            count(SESSION)
        return

    m, s = divmod(timer, 60)
    time_label.configure(text='{:02d}:{:02d}'.format(m, s))
    if IS_BREAK:
        cnt_label.configure(text='BREAK!')
    else:
        cnt_label.configure(text='Streak: {}'.format(SESS_COUNTER))
    job = root.after(1000, count, timer - 1)


def stop_count():
    """
    Stops the countdown and resets the counter
    """
    global SESS_COUNTER
    global IS_BREAK

    root.after_cancel(job)
    time_label.configure(text='{:02d}:{:02d}'.format(0, 0))
    SESS_COUNTER = 0
    IS_BREAK = False
    cnt_label.configure(text='Streak: {}'.format(0))
    start_btn.configure(text="Start", command=lambda: start())


# pauses the counter
def pause_count():
    global time_label

    start_btn.configure(text="Cont.", command=continue_count)
    root.wait_window(time_label)


# continue after pause
def continue_count():
    global wait

    wait.destroy()

# starts counting loop
def start():
    global SESSION
    global SESS_COUNTER

    SESS_COUNTER += 1
    start_btn.configure(command=tk.DISABLED)
    count(SESSION)

# VARIABLE DECLARATIONS
# define sessions and breaks
SHORT_BREAK = 5# * 60  # 5 mins after every pomodoro
LONG_BREAK = 20# * 60  # 20 mins after 4 pomodori
SESSION = 25# * 60  # lenght of a pomodoro session

# session counter
SESS_COUNTER = 0

# tells the program if the next session is going to be a break or not
IS_BREAK = False


# TKINTER SETTINGS

# root & title
root = tk.Tk()
root.title('Pomodoro')
root.geometry('200x60')


# labels
# main label area
main_label = tk.Frame(root)
main_label.grid(row=2, column=3, sticky='nesw')

# column padding in window
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# row padding in window
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)


# time label
time_label = tk.Label(main_label, text='00:00')
time_label.grid(row=1, column=1, columnspan=1)

# placehodler label
placeholder_label = tk.Label(main_label, text=' ~ ')
placeholder_label.grid(row=1, column=2)

# counter label
cnt_label = tk.Label(main_label, text='Streak: 0')
cnt_label.grid(row=1, column=3, columnspan=1)


# buttons
start_btn = tk.Button(main_label, text="Start", command=start)
start_btn.grid(row=2, column=1)
pause_btn = tk.Button(main_label, text="Pause", command=pause_count)
pause_btn.grid(row=2, column=2)
stop_btn = tk.Button(main_label, text="Stop", command=stop_count)
stop_btn.grid(row=2, column=3)


# MAINLOOP
root.mainloop()
