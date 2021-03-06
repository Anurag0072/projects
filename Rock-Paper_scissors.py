from tkinter import *
import random

# Initialize window

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Rock,Paper,Scissors')
root.config(bg='seashell3')

#heading
Label(root, text='ROCK, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()


# for user choice
user_take = StringVar()  # user_take is a string type that store choice tht user enters:
Label(root, text='choose any one: rock, paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)  # entry() widget uses
# when we want to create an input text field


# for computer choice
comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    # Function to start game
Result = StringVar()


def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie u both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose ,computer choose paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you in computer choose scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('u loose computer choose scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('u win computer choose rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('u win computer choose paper')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('u loose computer choose rock')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
        # Function to reset


def Reset():
    Result.set(" ")
    user_take.set(" ")


 # Function to exit


def Exit():
    root.destroy()

    # Define Buttons
Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)
root.mainloop()
