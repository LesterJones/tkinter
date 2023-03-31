from tkinter import *
from datetime import datetime
import time


# Constants
DEATH = datetime(2049, 11, 20) # Enter your time of death here.  You may need to take an online quiz.
RED = "#880033"

# Conversion factors
year = 60*60*24*365
month = 60*60*24*30
day = 60*60*24
hour = 60*60
minute = 60


def calculate_remaining_time():
    current_time = datetime.now()
    delta = DEATH - current_time
    total_seconds = delta.total_seconds()
    years = total_seconds // year
    total_seconds = total_seconds - years*year
    months = total_seconds // month
    total_seconds = total_seconds - months*month
    days = total_seconds // day
    total_seconds = total_seconds - days*day
    hours = total_seconds // hour
    total_seconds = total_seconds - hours*hour
    minutes = total_seconds // minute
    total_seconds = total_seconds - minutes*minute
    seconds = total_seconds

    return years, months, days, hours, minutes, seconds


def update_clock():
    years, months, days, hours, minutes, seconds = calculate_remaining_time()
    years = int(years)
    months = int(months)
    days = int(days)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    new_quote = f"Years: {years}\nMonths: {months}\nDays: {days}\nHours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}"
    countdown_clock.config(text=new_quote)


def start_clock():
    update_clock()
    window.after(1000, start_clock)


# Start a window
window = Tk()
window.config(padx=100, pady=100)
window.title("Super Metal Death Clock!")

# Labels
label = Label(text="Death Smiles at Us All", fg=RED, font=("Ariel", 35, "bold"))
label.grid(row=0, column=1)

# Create a label to show remaining time.
countdown_clock = Label(text='Time Remains')
countdown_clock.config(font=("Ariel", 30, 'bold'))
countdown_clock.grid(row=1, column=1)


# Create the canvas with an image of death.
canvas = Canvas(width=300, height=318, highlightthickness=0)
death_img = PhotoImage(file="Death.png")
canvas.create_image(150, 159, image=death_img)
canvas.grid(row=1, column=0)

start_clock()

window.mainloop()