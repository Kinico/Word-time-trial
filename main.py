from tkinter import *
from tkinter import messagebox
import words

root = Tk()
word = words.get_word()

GREEN = "#019a01"
YELLOW = "#c8b653"
GRAY = "#787c7f"
WHITE = "#FFFFFF"

guessnum = 1

wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

time_left = 300  # 300 seconds = 5 minutes

def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02}:{seconds:02}"

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=format_time(time_left))
        root.after(1000, update_timer)
    else:
        timeout()

timer_label = Label(root, text=format_time(time_left), font=("Arial", 14))
timer_label.grid(row=0, column=4, padx=10, pady=10)

def getGuess():
    global word, guessnum
    guess = wordInput.get()
    guessnum += 1
    
    if guessnum <= 5:
        if len(guess) == 5:
            if word == guess:
                messagebox.showinfo("Correct!", f"The word is {word.title()}")
            else:
                for i, letter in enumerate(guess):
                    label = Label(root, text=letter.upper())
                    label.grid(row=guessnum, column=i, pady=10, padx=10)

                    if letter == word[i]:
                        label.config(bg=GREEN, fg=GRAY)
                    elif letter in word:
                        label.config(bg=YELLOW, fg=GRAY)
                    else:
                        label.config(bg=GRAY, fg=WHITE)
        else:
            messagebox.showerror("Error", "Please type a 5-letter word.")
    else:
        messagebox.showerror("You lost", f"The answer was {word.upper()}")
 
    update_timer()

wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2, padx=10, pady=10)


def start_timer():
    messagebox.showinfo("Timer Started", "You have 5 minutes to guess the word.")
    update_timer()

def timeout():
    messagebox.showinfo("Time's Up!", "You ran out of time.")
    root.destroy()

start_timer()

root.mainloop()
