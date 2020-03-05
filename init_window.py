from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from tkinter import *
import time
from course_reader import CourseReader
from Schedule_Window import WindowSchedule

LOG_IN_TEXT = "Log into self service"
LOGGED_IN_BUTTON_TEXT = "Log in"
SELECT_TERM_LABEL = "Select Term"

class WindowInit:

    def __init__(self):
        # Open self service
        browser_options = Options()
        #browser_options.add_argument("--headless")
        self.browser = webdriver.Chrome('C:/Users/cp253/OneDrive/Documents/chromedriver', options=browser_options)
        self.browser.get("https://ssb.txstate.edu/prod/twbkwbis.P_WWWLogin")

        username = ''
        password = ''

        def login_clicked():
            nonlocal username
            nonlocal password
            nonlocal username_entry
            nonlocal password_entry
            username = username_entry.get()
            password = password_entry.get()
            self.window.destroy()

        # Log in
        self.window = Tk()
        Label(self.window, text=LOG_IN_TEXT).grid(row=0, column=0, sticky='W')
        Label(self.window, text="Username").grid(row=1, column=0, sticky='W')
        username_entry = Entry(self.window)
        username_entry.grid(row=1, column=1, sticky='W')
        Label(self.window, text="Password").grid(row=2, column=0, sticky='W')
        password_entry = Entry(self.window, show='*')
        password_entry.grid(row=2, column=1, sticky='W')
        Button(self.window, text=LOGGED_IN_BUTTON_TEXT, command=login_clicked).grid(row=3, column=0, sticky='W')
        self.window.mainloop()

        self.browser.find_element_by_xpath('//*[@id="UserID"]').send_keys(username)
        self.browser.find_element_by_xpath('//*[@id="PIN"]').send_keys(password)
        self.browser.find_element_by_xpath('/html/body/div[3]/form/p/input').click()

        # Click Student
        self.browser.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[2]/td[2]/a').click()
        #time.sleep(1)

        # Click Registration
        self.browser.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a').click()
        #time.sleep(1)

        # Click Look Up Courses
        self.browser.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td[2]/a').click()
        #time.sleep(1)

        dropdown_list = self.browser.find_elements(By.XPATH,
                                                   '/ html / body / div[3] / form / table / tbody / tr / td / '
                                                   'select / option')

        # create text for dropdown menu
        dropdown_list_text = []
        for item in dropdown_list:
            dropdown_list_text.append(item.text)

        self.window = Tk()
        selection = StringVar(self.window)
        selection.set(dropdown_list_text[0])
        Label(self.window, text=SELECT_TERM_LABEL).grid(row=0, column=0, sticky='W')
        OptionMenu(self.window, selection, *dropdown_list_text).grid(row=1, column=0, sticky='W')
        Button(self.window, text="Confirm", command=lambda: self.finish_init(selection)).grid(row=2, column=0, sticky='W')
        self.window.mainloop()

    def finish_init(self, term):
        dropdown = Select(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr/td/select'))
        termstr = term.get()
        dropdown.select_by_visible_text(termstr)
        self.browser.find_element_by_xpath('/html/body/div[3]/form/input[2]').click()
        self.window.destroy()
        reader = CourseReader(self.browser)
        WindowSchedule(reader)

WindowInit()
