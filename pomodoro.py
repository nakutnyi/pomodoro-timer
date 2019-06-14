#!/usr/bin/env python3

"""
Pomodoro.py
Created by Guido Minieri
Date - June 2017
My personal take on the most popular productivity tool out there.
"""

import datetime
import tkinter as tk
import statistics
from tkinter import messagebox#check why we need it


# class Counter():
#     def __init__(self):
#         self.is_break = False
#         self.is_wait = False
#         self.job = 

def count():
    """Countdown"""

    global TIMER
    global IS_BREAK
    global JOB
    global SESS_COUNTER

    ask = messagebox.askquestion

    if TIMER <= -1:

        #write statistics entry
        if not IS_BREAK:
            statistics.add_stat(str(datetime.datetime.now()))

        # toggle IS_BREAK
        IS_BREAK = not IS_BREAK

        # prompt and start new session
        if IS_BREAK and SESS_COUNTER % 4 != 0:
            prompt_answer = ask("Session Ended!", "\nAre you ready for a break?\n", icon='question')
        elif IS_BREAK and SESS_COUNTER % 4 == 0:
            prompt_answer = ask("4 POMODORI!", "Do you want a long break", icon='question')
        else:
            prompt_answer = ask("Time's up!", "\nReady for a new session?\n", icon='question')



        if prompt_answer == 'yes' and SESS_COUNTER % 4 != 0 and IS_BREAK:
            ROOT.after_cancel(JOB)
            TIMER = SHORT_BREAK #TODO: count(arg)
            count()
        elif prompt_answer == 'yes' and SESS_COUNTER % 4 == 0 and IS_BREAK:
            ROOT.after_cancel(JOB)
            TIMER = LONG_BREAK #TODO: count(arg)
            count()
        elif prompt_answer == 'no':
            stop()
        else:
            SESS_COUNTER += 1
            TIMER = SESSION #TODO: fix all global declarations
            count()
        return

    minutes, seconds = divmod(TIMER, 60)
    TIME_LABEL.configure(text='{:02d}:{:02d}'.format(minutes, seconds))
    if IS_BREAK:
        CNT_LABEL.configure(text='Break')
    elif IS_WAIT:
        CNT_LABEL.configure(text='Waiting...')
    else:
        CNT_LABEL.configure(text='Streak: {}'.format(SESS_COUNTER))
    if not IS_WAIT:
        TIMER -= 1 #TODO: count(arg)
        JOB = ROOT.after(1000, count)


def stop():
    """Stop the countdown and resets the counter"""
    global SESS_COUNTER
    global IS_BREAK

    ROOT.after_cancel(JOB)
    TIME_LABEL.configure(text='{:02d}:{:02d}'.format(0, 0))
    SESS_COUNTER = 0
    IS_BREAK = False
    CNT_LABEL.configure(text='Streak: {}'.format(0))
    START_BTN.configure(text="Start", command=start)


# pauses the counter
def pause():
    """Pause the counter"""
    global IS_WAIT
    IS_WAIT = not IS_WAIT
    START_BTN.configure(text="Resume", command=resume)

def resume():
    """Continue after pause"""
    global IS_WAIT
    IS_WAIT = not IS_WAIT
    count()
    START_BTN.configure(text="Start", command=start)
    #wait.destroy()

def start():
    """Start counting loop"""
    global SESS_COUNTER
    global TIMER
    global SESSION
    SESS_COUNTER += 1
    START_BTN.configure(command=tk.DISABLED)
    #TODO: find a way to put TIMER as count()'s parameter, not a global variable
    TIMER = SESSION 
    count()

# VARIABLE DECLARATIONS
# define sessions and breaks
SHORT_BREAK = 5 * 60  # 5 mins after every pomodoro
LONG_BREAK = 20 * 60  # 20 mins after 4 pomodori
SESSION = 25 * 60  # lenght of a pomodoro session

# session counter
SESS_COUNTER = 0

# tells the program if the next session is going to be a break or not
IS_BREAK = False
IS_WAIT = False


# TKINTER SETTINGS

# ROOT & title
ROOT = tk.Tk()
ROOT.wm_iconbitmap('@'+'icon.xbm')
ROOT.option_add("*Font", "courier")
ROOT.option_add("*Label.Font", "helvetica 12 bold")
ROOT.title('Pomodoro')
ROOT.geometry('600x250')


# labels
# main label area
MAIN_LABEL = tk.Frame(ROOT)
MAIN_LABEL.grid(row=2, column=3, sticky='nesw')

# column padding in window
ROOT.grid_columnconfigure(1, weight=1)
ROOT.grid_columnconfigure(2, weight=1)
ROOT.grid_columnconfigure(3, weight=1)
# TODO: the path to icon must not be hardcoded

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
START_BTN = tk.Button(MAIN_LABEL, text=" Start ", command=start)
START_BTN.grid(row=2, column=1)
PAUSE_BTN = tk.Button(MAIN_LABEL, text=" Pause ", command=pause)
PAUSE_BTN.grid(row=2, column=2)
STOP_BTN = tk.Button(MAIN_LABEL, text="  Stop  ", command=stop)
STOP_BTN.grid(row=2, column=3)


# MAINLOOP
ROOT.mainloop()
