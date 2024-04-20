from tkinter import *
from tkinter import messagebox
import words

root = Tk()
root.title("The Word")
word = words.get_word()
root.geometry('500x600')  # Window size
GREEN = "#019a01"
YELLOW = "#c8b653"
GRAY = "#787c7f"
WHITE = "#FFFFFF"
VIOLET = "#953f9a"
YELLOW2 = "#e6b322"
BLUE = "#60b5c2"

guessnum = 1

# starts the timer
def start_timer():
    update_timer()

# Switch frames
def show_frame(frame):
    frame.tkraise()

# time format
def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02}:{seconds:02}"

# Create menu frame
menu_frame = Frame(root)
menu_frame.grid(row=0, column=0, sticky="nsew")
menu_frame.configure(bg=VIOLET)

# Bind the function to window resize event
root.bind("<Configure>")

# The play button
play_button = Button(menu_frame, text="Play",bg=YELLOW2, font=("Comic Sans MS", 20,), width=10, command=lambda: [start_timer(),show_frame(game_frame)])
play_button.pack(padx=70, pady=(60,5))

# Tutorial button
def show_tutorial():
    tutorial_frame = Frame(root)
    tutorial_frame.grid(row=0, column=0, sticky="nsew")
    tutorial_frame.configure(bg=BLUE)

    tutorial_label = Label(tutorial_frame, text="This is the tutorial page.",bg=BLUE, font=("Comic Sans MS", 15))
    tutorial_label.pack(padx=20, pady=20)

    back_button = Button(tutorial_frame, text="Back to Menu", command=lambda: [tutorial_frame.destroy(), show_frame(menu_frame)])
    back_button.pack(padx=20, pady=10)

    show_frame(tutorial_frame)

tutorial_button = Button(menu_frame, text="Tutorial",bg=YELLOW2, font=("Comic Sans MS", 20),width=10, command=show_tutorial)
tutorial_button.pack(padx=20, pady=5)

text = Label(menu_frame, text="Welcome to\nThe Word", bg=VIOLET, font=("Comic Sans MS", 30, "bold"), wraplength=300, justify="center")
text.pack(padx=60, pady=(100, 1))  # Use a tuple for y-padding to set different padding for top and bottom

# the game frame
game_frame = Frame(root)
game_frame.grid(row=0, column=0, sticky="nsew")

# The input box so you can input the text
wordInput = Entry(game_frame, width=10, font=("Comic Sans MS", 31))
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

time_left = 301  # The set time

# Display the time
timer_label = Label(game_frame, text=format_time(time_left), font=("Comic Sans MS", 14))
timer_label.grid(row=0, column=4, padx=10, pady=10)

# Function to handle guessing a word in the game
def getGuess():
    global word, guessnum
    guess = wordInput.get().lower()  # Get the guessed word
    word = word.lower()
    guessnum += 1  # adds 1 to the guess count

    if guessnum <= 6:  # Checks if the number of guesses is more than 5
        if len(guess) == 5:  # Checks if the word is 5 letters
            for i, letter in enumerate(guess):
                label = Label(game_frame, text=letter.upper(), font=("Arial", 20, "bold"),width=2, height=1)
                label.grid(row=guessnum, column=i, pady=(10,1) , padx=(50,1))
                # Sets the color for the letters
                if letter == word[i]:
                    label.config(bg=GREEN, fg=WHITE)
                elif letter in word:
                    label.config(bg=YELLOW, fg=WHITE)
                else:
                    label.config(bg=GRAY, fg=WHITE)
            if word == guess:  # Checks if the guess is correct
                messagebox.showinfo("Correct!", f"The word is {word.title()}")
        else:
            messagebox.showerror("Error", "Please type a 5-letter word.")  # Displays if the guess letter is not 5 letters
    else:
        messagebox.showerror("You lost", f"The answer was {word.upper()}")  # Displays if you exceed 5 guesses



# The button for the guess
wordGuessButton = Button(game_frame, text="Guess", command=getGuess, font=("Comic Sans MS", 20))
wordGuessButton.grid(row=999, column=3, columnspan=2, padx=10, pady=10)

# starts the timer
def start_timer():
    update_timer()

# Updates the timer every second
def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=format_time(time_left))
        root.after(1000, update_timer)
    else:
        timeout()  # If the timer runs out

# Function to handle when time runs out
def timeout():
    messagebox.showinfo("Time's Up!", "You ran out of time.")  # SHow the timer has ran out
    root.destroy()  # Closses the window

print(word)  # show the answer in the terminal so I know the answer
show_frame(menu_frame)  # Show the menu frame

# Configure row and column weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()  # Loops tkinter
