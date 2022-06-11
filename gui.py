import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from bs4 import BeautifulSoup
import requests

win = tk.Tk()
win.title("Boston Jobs")


text = tk.StringVar()

scrol_w = 20
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)

scrol_w = 20
scrol_h = 3
scr_des = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)


def information(html_code):
    html_code = html_code.split('>')
    html_code = ' '.join(html_code)
    html_code = html_code.split('<')
    list_atr = []
    list_atr_info = []

    for i in html_code:
        i = i.split(' ')
        if i[0] == 'span':
            list_atr.append(' '.join(i[1:]))

        if i[0] == 'b':
            list_atr_info.append(' '.join(i[1:]))
    list_string_format_to_show = []
    for title, info in zip(list_atr, list_atr_info):
        title=title.replace('{', '')
        title=title.replace('}', '')

        list_string_format_to_show.append(f'{title.strip()} {info.strip()}\n  ')
        scr_des.insert(tk.INSERT, f'{title.strip():<10} {info.strip():>10}\n  ')


    print(list_atr)
    print(list_atr_info)





def search_detal(url_detail):
    page = requests.get(url_detail)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_job = soup.find_all(class_ = 'attrgroup')
    ttk.Button(win, text=f"{url_detail}").grid(row=4, column=3,pady=1)
    ttk.Button(win, text="For more details press button",command=lambda : information(str(title_job))).grid(row=5, column=3)

    print(title_job)


def request_to_site(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_job = soup.find_all(class_="result-title hdrlnk")
    list_job =[]
    count = 0
    for i in title_job:
        count += 1
        list_job.append([i.text, i["href"]])
        scr.insert(tk.INSERT, f'{count}- {i.text}\n')




    for i in range(10):
        ttk.Button(win, text=f"{list_job[i][0]}", command=lambda : search_detal(list_job[i][1])).grid(row=i+4, column=0,pady=1)

    print(list_job)


def search():
    url = 'https://boston.craigslist.org/search/jjj?query='
    job = text.get()
    '''action.configure(text="I have been clicked!")
    a_lable.configure(foreground='red')
    a_lable.configure(text='A red Label')'''
    search_for = job
    search_for = search_for.split(' ')
    search_for = '+'.join(search_for)
    url = url + search_for


    request_to_site(url)



a_lable = ttk.Label(win, text="A Lable")
a_lable.grid(column=0, row=0)

action = ttk.Button(win, text="Click to search", command=search)
action.grid(column=0, row=2,ipadx=30, ipady=10)

'''action1 = ttk.Button(win, text="Clear Results", command=search)
action1.grid(column=1, row=2)'''

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=text)
name_entered.insert(0, "Some Menu for Job title Selection(for exapmle: A Drop Menu")
name_entered.grid(column = 0, row = 1,padx=10, pady=10, ipadx=200, ipady=10,columnspan=2)

ttk.Label(win, text = "Enter your job").grid(column=1, row=0)

chVarDis = tk.IntVar()

color = ["Blue", "Gold", "Red"]

radVar = tk.IntVar()

scr.grid(column=0,row=3, columnspan=2,ipadx=140, ipady=60,pady=30)


scr_des.grid(column=2,row=3, columnspan=2,ipadx=140, ipady=70)

name_entered.focus()

win.mainloop()


