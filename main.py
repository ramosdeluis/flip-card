from tkinter import *
import pandas as pd


BG_COLOR = '#B1DDC6'

data = pd.read_csv('en_moust_common.csv')

# Screen configs
window = Tk()
window.title('English Words Flip Card')
window.config(padx=50, pady=50, bg=BG_COLOR)

# Label

label = Label(text='Hello')
label.grid(row=0)


# Canvas

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='images/card_front.png', width=800, height=526)
card_back_image = PhotoImage(file='images/card_back.png', width=800, height=526)
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons

green_button_image = PhotoImage(file='images/right.png', height=100, width=100)
red_button_image = PhotoImage(file='images/wrong.png', height=100, width=100)
green_button = Button(image=green_button_image)
red_button = Button(image=red_button_image)
green_button.grid(column=1, row=1)
red_button.grid(column=0, row=1)



window.mainloop()
