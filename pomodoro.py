#!/usr/bin/env python3

"""
Pomodoro.py
Created by Guido Minieri
Date - June 2017
My personal take on the most popular productivity tool out there.
"""


import tkinter as tk
from tkinter import messagebox

def count(timer):
    """Countdown"""
    global IS_BREAK
    global JOB
    global SESS_COUNTER

    ask = messagebox.askquestion

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
            ROOT.after_cancel(JOB)
            count(SHORT_BREAK)
        elif prompt_answer == 'yes' and SESS_COUNTER % 4 == 0 and IS_BREAK:
            ROOT.after_cancel(JOB)
            count(LONG_BREAK)
        elif prompt_answer == 'no':
            stop_count()
        else:
            SESS_COUNTER += 1
            count(SESSION)
        return

    minutes, seconds = divmod(timer, 60)
    TIME_LABEL.configure(text='{:02d}:{:02d}'.format(minutes, seconds))
    if IS_BREAK:
        CNT_LABEL.configure(text='BREAK!')
    else:
        CNT_LABEL.configure(text='Streak: {}'.format(SESS_COUNTER))
    JOB = ROOT.after(1000, count, timer - 1)


def stop_count():
    """Stop the countdown and resets the counter"""
    global SESS_COUNTER
    global IS_BREAK

    ROOT.after_cancel(JOB)
    TIME_LABEL.configure(text='{:02d}:{:02d}'.format(0, 0))
    SESS_COUNTER = 0
    IS_BREAK = False
    CNT_LABEL.configure(text='Streak: {}'.format(0))
    START_BTN.configure(text="Start", command=start())


# pauses the counter
def pause_count():
    """Pause the counter"""
    START_BTN.configure(text="Cont.", command=continue_count)
    ROOT.wait_window(TIME_LABEL)


def continue_count():
    """Continue after pause"""
    wait.destroy()

def start():
    """Start counting loop"""
    global SESS_COUNTER

    SESS_COUNTER += 1
    START_BTN.configure(command=tk.DISABLED)
    count(SESSION)

# VARIABLE DECLARATIONS
# define sessions and breaks
SHORT_BREAK = 5 * 60  # 5 mins after every pomodoro
LONG_BREAK = 20 * 60  # 20 mins after 4 pomodori
SESSION = 25 * 60  # lenght of a pomodoro session

# session counter
SESS_COUNTER = 0

# tells the program if the next session is going to be a break or not
IS_BREAK = False


# TKINTER SETTINGS

# ROOT & title
ROOT = tk.Tk()
ROOT.title('Pomodoro')
ROOT.geometry('200x60')


# labels
# main label area
MAIN_LABEL = tk.Frame(ROOT)
MAIN_LABEL.grid(row=2, column=3, sticky='nesw')

# column padding in window
ROOT.grid_columnconfigure(1, weight=1)
ROOT.grid_columnconfigure(2, weight=1)
ROOT.grid_columnconfigure(3, weight=1)

# row padding in window
ROOT.grid_rowconfigure(1, weight=1)
ROOT.grid_rowconfigure(2, weight=1)


# time label
TIME_LABEL = tk.Label(MAIN_LABEL, text='00:00')
TIME_LABEL.grid(row=1, column=1, columnspan=1)

# placehodler label
PLACEHOLDER_LABEL = tk.Label(MAIN_LABEL, text=' ~ ')
PLACEHOLDER_LABEL.grid(row=1, column=2)

# counter label
CNT_LABEL = tk.Label(MAIN_LABEL, text='Streak: 0')
CNT_LABEL.grid(row=1, column=3, columnspan=1)


# buttons
START_BTN = tk.Button(MAIN_LABEL, text="Start", command=start)
START_BTN.grid(row=2, column=1)
PAUSE_BTN = tk.Button(MAIN_LABEL, text="Pause", command=pause_count)
PAUSE_BTN.grid(row=2, column=2)
STOP_BTN = tk.Button(MAIN_LABEL, text="Stop", command=stop_count)
STOP_BTN.grid(row=2, column=3)


# MAINLOOP
ROOT.mainloop()
