from tkinter import *
import tkinter
import time
from time import time
import random
import csv

# declaring window 1

start_screen = tkinter.Tk()
img = PhotoImage(file="Mini project background 1.png")
label = Label(start_screen, image=img)
label.place(x=0, y=0)
start_screen.geometry("800x500")
heading = Label(start_screen, text="TYPING TEST", bg="black", fg="white", font=("Times New Roman", 35, "bold"))
heading.pack(padx=25, pady=30, anchor=W)

name = tkinter.StringVar()


def submit():
    global name
    name = name_entry.get()
    start_screen.destroy()


name_label = tkinter.Label(start_screen, text="Please Enter Your Name", font=("Times New Roman", 20, "bold"))
name_label.pack(padx=30, pady=30, anchor=W)
name_entry = tkinter.Entry(start_screen, textvariable=name, font=('calibre', 20, 'normal'))
name_entry.pack(padx=25, pady=25, anchor=W)
submitbutton = tkinter.Button(start_screen, text="Submit", command=submit, width=6, height=2,
                              font=('calibre', 14, 'bold'))
submitbutton.pack(padx=135, pady=5, anchor=W)

start_screen.mainloop()

# declaring window 2

welcome_screen = tkinter.Tk()
welcome_screen.geometry("800x500")


def destroy():
    welcome_screen.destroy()


img = PhotoImage(file="Mini project background 1.png")
label = Label(welcome_screen, image=img)
label.place(x=0, y=0)
heading = Label(welcome_screen, text="TYPING TEST", bg="black", fg="white", font=("Times New Roman", 35, "bold"))
heading.pack(padx=25, pady=30, anchor=W)
display = "Welcome " + str(name)
message = Label(welcome_screen, text=display, bg="white", fg="black", font=("Times New Roman", 30, "bold"))
message.pack(padx=50, pady=30, anchor=W)
startgame = tkinter.Button(welcome_screen, text="Start Game", width=12, height=2, command=destroy,
                           font=('calibre', 14, 'bold'))
startgame.pack(padx=100, pady=25, anchor=W)

welcome_screen.mainloop()

# Declaring window 3

game_screen = tkinter.Tk()
img = PhotoImage(file="Mini project background 2.png")
label = Label(game_screen, image=img)
label.place(x=0, y=0)
game_screen.geometry("800x500")


# calculate the accuracy of the user input
def errors(userinput, og_sentence):
    og_sentence = og_sentence.split()
    userinput = userinput.split()
    error = 0
    if len(og_sentence) > len(userinput) or len(og_sentence) == len(userinput):
        shorter_len = len(userinput)
        error = len(og_sentence) - len(userinput)
    else:
        shorter_len = len(og_sentence)
        error = len(userinput) - len(og_sentence)
    for i in range(shorter_len):
        if len(og_sentence[i]) == len(userinput[i]):
            for j in range(len(og_sentence[i])):
                if og_sentence[i][j] != userinput[i][j]:
                    error += 1
        else:
            error += 1
    return error


# To calculate the speed in words per minute
def speed(userinput, start_time, end_time):
    userinput = userinput.split()
    totalwords = len(userinput)
    Input_speed = (totalwords / round((end_time - start_time), 2)) * 60

    return round(Input_speed, 2)


# calculate total time elapsed
def timetaken(start_time, end_time):
    time_taken = round((end_time - start_time), 2)

    return time_taken


def get_sentence():
    f = open('sentences.txt', 'r')
    sentences = f.readlines()
    sentence = random.choice(sentences)
    return sentence


def submit2():
    global etime
    global prompt

    prompt = typedsentence.get()
    etime = time()
    game_screen.destroy()


prompt = tkinter.StringVar()

# starting time after start is pressed
stime = time()
ogsentence = get_sentence()
message = Label(game_screen, text=ogsentence, bg="black", fg="white", font=("Times New Roman", 30, "bold"))
message.pack(padx=30, pady=30)
typedsentence = tkinter.Entry(game_screen, textvariable=prompt, font=('calibre', 25, 'normal'))
typedsentence.pack(padx=30, pady=30)
submitbutton = tkinter.Button(game_screen, text="Submit", width=6, height=2, command=submit2, font=('calibre', 14, 'bold'))
submitbutton.pack(padx=5, pady=5)

game_screen.mainloop()

# declaring window 4

results_screen = tkinter.Tk()
results_screen.geometry("800x500")
img = PhotoImage(file="Mini project background 3.png")
label = Label(results_screen, image=img)
label.place(x=0, y=0)


def destroy2():
    results_screen.destroy()


# calling the functions

def typingSpeed(userinput, start_time, end_time):
    """
    Function to calculate typing speed in words per minute (WPM).
    
    Parameters:
    userinput (str): The user's typed input.
    start_time (float): The start time of typing.
    end_time (float): The end time of typing.
    
    Returns:
    float: The typing speed in words per minute (WPM).
    """
    words_typed = len(userinput.split())
    time_elapsed = end_time - start_time
    minutes_elapsed = time_elapsed / 60
    wpm = words_typed / minutes_elapsed
    return wpm


time = timetaken(stime, etime)
speed = typingSpeed(str(prompt), stime, etime)
errors = errors(str(prompt), ogsentence)

heading = Label(results_screen, text="YOUR RESULT", fg="white", bg="#293148", font=("Times New Roman", 30, "bold"))
heading.pack(padx=30, pady=30, anchor=W)
time_message = "Time taken: " + str(time) + "seconds"
timetaken = tkinter.Label(results_screen, text=time_message, fg="white", bg="#293148", font=("Times New Roman", 20, "bold"))
timetaken.pack(padx=30, pady=30, anchor=W)
wpm_message = "Your typing speed is: " + str(speed) + "wpm"
speedlabel = tkinter.Label(results_screen, text=wpm_message, fg="white", bg="#293148", font=("Times New Roman", 20, "bold"))
speedlabel.pack(padx=30, pady=30, anchor=W)
errors_message = "Number of errors: " + str(errors)
speedlabel = tkinter.Label(results_screen, text=errors_message, fg="white", bg="#293148", font=("Times New Roman", 20, "bold"))
speedlabel.pack(padx=30, pady=30, anchor=W)
viewleaderboard = tkinter.Button(results_screen, text="Show Leaderboard", command=destroy2, width=15, height=2,font=('calibre', 14, 'bold'))
viewleaderboard.pack(padx=60, pady=30, anchor=W)

results_screen.mainloop()

# declaring window 5

leaderboard = tkinter.Tk()
leaderboard.geometry("800x500")

img = PhotoImage(file="Mini project background 3.png")
label = Label(leaderboard, image=img)
label.place(x=0, y=0)

# player score
player_score = [0, str(name), float(speed)]

# opening file and reading
score_file = 'scores1.csv'
file = open(score_file, 'r')
reader = csv.reader(file)

# putting data in a list
data = []
for i in reader:
    data.append(i)
file.close()

# changed data
changed_data = data

# going through the data and checking
n = len(data)
x = n
for i in range(1, n):
    if float(data[i][2]) < player_score[2]:
        player_score[0] = i - 1
        changed_data.insert(i, player_score)
        x = i
        break

if x == n:
    player_score[0] = n
    changed_data.insert(n, player_score)
else:
    for a in range(x, n + 1):
        changed_data[a][0] = a + 1

# closing file
file.close()

# opening file to write
file = open(score_file, 'w', newline='')
writer = csv.writer(file)
writer.writerows(changed_data)
file.close()

# opening again to get edited data
file = open(score_file, 'r')
reader = csv.reader(file)
data = []
for i in reader:
    data.append(i)
file.close()

rows = []
try:
    table_top = 'Rank' + '\t' + 'Name' + '\t ' + 'WPM'
    table_label = tkinter.Label(leaderboard, text=table_top, fg="white", bg="#293148",
                                font=("Times New Roman", 25, "bold"))
    table_label.pack(padx=10, pady=10, anchor=W)
    for i in range(10):
        table_entry = str(data[i][0]) + '\t' + str(data[i][1]) + '\t   ' + str(data[i][2])
        table_entry_label1 = tkinter.Label(leaderboard, text=table_entry, fg="white", bg="#293148",
                                           font=("Times New Roman", 24, "normal"))
        table_entry_label1.pack(padx=10, pady=0, anchor=W)
except:
    pass

leaderboard.mainloop()

