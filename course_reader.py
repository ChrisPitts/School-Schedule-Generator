from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tkinter import *
import time
from Course import Course

SUBMIT_BUTTON_TEXT = 'Submit'
SUBJECT_LABEL = 'Select a subject'


class CourseReader:
    def __init__(self, browser):
        self.browser = browser

    def lookup_class(self):
        menu_elements = self.browser.find_elements(By.XPATH, '//*[@id="subj_id"]/option')
        subject_text = []
        for element in menu_elements:
            subject_text.append(element.text)

        subjectstr = self.prompt_list(SUBJECT_LABEL, subject_text)
        subject_menu = Select(
            self.browser.find_element_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr/td[2]/select'))
        subject_menu.select_by_visible_text(subjectstr)
        self.browser.find_element_by_xpath('/html/body/div[3]/form/input[17]').click()

        course_data = []
        for i in range(3, len(self.browser.find_elements(By.XPATH, '/html/body/div[3]/table[2]/tbody/tr')) + 1):
            course_data.append([])
            course_data[i - 3].append(self.browser.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/'
                                                                         'tr[%i]/td[1]' % i))
            course_data[i - 3].append(self.browser.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/'
                                                                         'tr[%i]/td[2]' % i))
            course_data[i - 3].append(self.browser.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/'
                                                                         'tr[%i]/td[3]/form/input[30]' % i))
        course_strings = []
        for i in range(0, len(course_data)):
            course_strings.append('%s %s' % (course_data[i][0].text, course_data[i][1].text))

        course_str = self.prompt_list("Select course", course_strings)
        course_data[course_strings.index(course_str)][2].click()

        subject = self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[3]').text
        number = self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[4]').text
        course = Course(subject, number)

        for i in range(3, len(self.browser.find_elements(By.XPATH, '/html/body/div[3]/form/table/tbody/tr'))+1):
            arr = []
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[1]/abbr' % i)
                       .text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[2]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[5]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[6]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[9]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[10]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[11]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[13]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[17]' % i).text)
            arr.append(self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[19]' % i).text)
            course.add_section(arr)
        course.print()
        input("Press enter to continue")

        # window = Tk()
        # Label(window, text=SUBJECT_LABEL).grid(row=0, column=0, sticky='W')
        # selection = StringVar(window, subject_text[0])
        # OptionMenu(window, selection, *subject_text).grid(row=1, column=0, sticky='W')
        # Button(window, text=SUBMIT_BUTTON_TEXT, command=lambda:self.show_classes(window, selection)).grid(row=2, column=0, sticky='W')
        # window.mainloop()

    def prompt_list(self, label, strings):
        ret_str = ''

        def submit():
            nonlocal ret_str
            ret_str = str_var.get()
            window.destroy()
        window = Tk()
        str_var = StringVar(window, strings[0])
        Label(window, text=label).grid(row=0, column=0, sticky='W')
        OptionMenu(window, str_var, *strings).grid(row=1, column=0, sticky='W')
        Button(window, text=SUBMIT_BUTTON_TEXT, command=submit).grid(row=2, column=0, sticky='W')
        window.mainloop()
        return ret_str


