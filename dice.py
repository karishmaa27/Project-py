import random
import tkinter as tk

def roll_dice(dice):
    # Get a random number between 1 and 6.
    number = random.randint(1, 6)
    # Set the image of the dice to the corresponding number.
    canvas.itemconfigure(dice, image=dice_images[number - 1])
    # Set the text of the label to the number.
    label.configure(text=str(number))

# Create the main window.
root = tk.Tk()

# Create the canvas.
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Create the dice images.
dice_images = [
    tk.PhotoImage(file="dice1.png"),
    tk.PhotoImage(file="dice2.png"),
    tk.PhotoImage(file="dice3.png"),
    tk.PhotoImage(file="dice4.png"),
    tk.PhotoImage(file="dice5.png"),
    tk.PhotoImage(file="dice6.png")
]

# Create the dice.
dice = canvas.create_image(100, 100, image=dice_images[0])

# Create the buttons.
roll_button = tk.Button(root, text="Roll", command=lambda: roll_dice(dice))
roll_button.pack()

# Create the label.
label = tk.Label(root, text="")
label.pack()

# Start the main loop.
root.mainloop()
