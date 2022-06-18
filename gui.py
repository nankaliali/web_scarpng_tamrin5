import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
# Web driver is a part of selenium. Web driver is basically the core of selenium.

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import requests

class LogingPage:

    def __init__(self,browser):
        self.browser = browser

    def login(self, user_name, password):

        # access that Web driver using Web driver chrome
        username_input = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        password_input = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        username_input.send_keys(user_name)
        password_input.send_keys(password)

        # click to loging
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
        '''self.browser.f'''
        sleep(5)
        self.Logged_User_Information(user_name, password)

    def Logged_User_Information(self, user_name, password):

        self.user_name = user_name
        self.password = password
        self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()
        self.count_post = self.browser.find_element('xpath', '(//* [@class="_ac2a"])[1]').text
        self.prof_url = self.browser.find_element('xpath', "// * [@class = '_aadp']").get_attribute('src')
        self.image_data = requests.get(self.prof_url).content
        with open('prof.jpg', 'wb') as hand:
            hand.write(self.image_data)


    def information_post_prof(self):
        return self.count_post


class Home_page:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')
        #self.browser.fullscreen_window()

    def go_to_login_page(self):
        sleep(2)
        return LogingPage(self.browser)

    def go_to_meassage_box(self):
        sleep(2)
        return Messages_box(self.browser)



class Messages_box:
    def __init__(self,browser):
        self.browser = browser
        self.go_to_page_text_box_for_message_text()

    def go_to_page_text_box_for_message_text(self):
        self.browser.find_element('xpath', '//* [@class="_ab6-" and @aria-label ="Direct"]').click()
        self.browser.implicitly_wait(5)
        self.browser.find_element('xpath', '//*[@class = "_a9-- _a9_1"]').click()
        self.browser.implicitly_wait(5)

'''        self.id_search('m_b_alizade', 'Hello    PO___FI___UZ')


    def id_search(self, id_contact, Msg):
        print('1')
        self.browser.find_element('xpath', '//*[@aria-label = "New message"]').click()
        self.browser.find_element('xpath', '//*[@class = "_aaie  _aaid _aaiq"]').send_keys(id_contact)
        self.browser.find_element('xpath', '(//*[@cx= "12.008"])[1]').click()
        self.browser.find_element('xpath', '(//*[@class= "_aagz"])[1]').click()
        self.browser.find_element('xpath', '//*[@placeholder= "Message..."]').send_keys(Msg)
        self.browser.find_element('xpath', '//*[@class = "_acan _acao _acas" and text() = "Send"]').click()


class Stories:
    def __init__(self, browser):
        self.browser = browser
        pass

    def download_story(self):
        pass
'''







driver = webdriver.Chrome('chromedriver.exe')
driver.find_elements()
home_page = Home_page(driver)
login_page = home_page.go_to_login_page()
login_page.login('margatsni_80', 'alidada.1380baba')

'''msg = Messages_box(driver)'''






win = tk.Tk()
win.title("Instagram")

img1 = ImageTk.PhotoImage(Image.open("prof.jpg"))
label1 = Label(win, image=img1)
label1.grid(row=3, column=0)




win.mainloop


