import tkinter as tk
from tkinter import ttk

import requests
from bs4 import BeautifulSoup

from tkinter import *
from PIL import ImageTk, Image

win = tk.Tk()
win.title("image search")




def search(search_for):

    url_bing_img = 'https://www.bing.com/images/search?q='

    search_for = str(search_for).split(' ')
    search_for = '%20'.join(search_for)
    print('%',search_for)
    for i in search_for:
        url_bing_img += i
    page = requests.get(url_bing_img)

    soup = BeautifulSoup(page.text, "html.parser")

    x = 1
    for img in soup.find_all('img', class_='mimg'):
        if x ==6:
            break
        x += 1
        print(x)
        #if requests.get(img['src']).status_code == 200:

            #print(img['src'])

        response = requests.get(img['src'])
        file = open(f"sample_image{x}.png", "wb")
        file.write(response.content)
        file.close()

    print("finish")
    display()





name = tk.StringVar()
search_f = ttk.Entry(win, width=12, textvariable=name)
search_f.insert(0,'Search for...')
search_f.grid(column = 0, row = 0,padx=10, pady=10, ipadx=200, ipady=10,columnspan=2)

def clear():
    search_for.delete(0, 'end')

ttk.Button(win, text='Search to click',command=lambda : search(name.get())).grid(row=1, column=0 )
ttk.Button(win, text='Clear to Results', command=clear).grid(row=1, column=1)




win.mainloop()

