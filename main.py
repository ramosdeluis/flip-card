from tkinter import *
import pandas as pd


BG_COLOR = '#B1DDC6'
news_word = ''

try:
    data = pd.read_csv('en_most_common.csv')
except pd.errors.EmptyDataError:
    new_data = pd.read_csv('known_word.csv')
    new_data.to_csv('en_most_common.csv', index=False)
finally:
    data = pd.read_csv('en_most_common.csv')


# Functions

cont = 0


def next_card():
    try:
        global news_word, flip_timer
        window.after_cancel(flip_timer)
        canvas.itemconfig(title, text='English', fill='black')
        news_word = data.en_word.sample()
        canvas.itemconfig(word, text=f'{news_word.values[0]}', fill='black')
        canvas.itemconfig(image, image=card_front_image)
        flip_timer = window.after(3000, func=flip_card)
    except:
        with open('en_most_common.csv', mode='w+'):
            pass


def is_known():
    number = news_word.index[0]
    try:
        with open('known_word.csv', 'r') as file:
            pass
    except FileNotFoundError:
        with open('known_word.csv', 'w') as file:
            file.write('en_word,pt_word,frequence\n')
    finally:
        with open('known_word.csv', 'a') as file:
            file.writelines(f'{data.loc[number].en_word.strip()},{data.loc[number].pt_word.strip()},{data.loc[number].frequence}\n')
        data.drop(data.index[number], inplace=True)
        data.to_csv('en_most_common.csv', index=False)
        next_card()


def flip_card():
    canvas.itemconfig(title, text='Portuguese', fill='white')
    translate = data.loc[news_word.index[0]]['pt_word']
    canvas.itemconfig(word, text=f'{translate}', fill='white')
    canvas.itemconfig(image, image=card_back_image)


# Screen configs
window = Tk()
window.title('English Words Flip Card')
window.config(padx=50, pady=50, bg=BG_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Label

label = Label(text='Hello')
label.grid(row=0)


# Canvas

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='images/card_front.png', width=800, height=526)
card_back_image = PhotoImage(file='images/card_back.png', width=800, height=526)
image =canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons

green_button_image = PhotoImage(file='images/right.png', height=100, width=100)
red_button_image = PhotoImage(file='images/wrong.png', height=100, width=100)
green_button = Button(image=green_button_image, command=is_known, highlightthickness=0)
red_button = Button(image=red_button_image, command=next_card, highlightthickness=0)
green_button.grid(column=1, row=1)
red_button.grid(column=0, row=1)

next_card()




window.mainloop()
