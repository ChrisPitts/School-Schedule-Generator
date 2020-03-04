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

        subject_str = self.prompt_list(SUBJECT_LABEL, subject_text)
        subject_menu = Select(
            self.browser.find_element_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr/td[2]/select'))
        subject_menu.select_by_visible_text(subject_str)
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
        name = self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[8]').text
        course = Course(subject, number, name)

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

        window = Tk()
        Label(window, text="%s %s %s" % (course.subject, course.number, course.name)).grid(row=0, column=0, sticky='W')
        i = 0
        for key in course.sections:
            section = course.sections[key]
            Label(window, text=section.status).grid(row=i+1, column=0, sticky='W')
            Label(window, text=section.course_number).grid(row=i + 1, column=1, sticky='W')
            Label(window, text=section.section_number).grid(row=i + 1, column=2, sticky='W')
            Label(window, text=section.campus).grid(row=i + 1, column=3, sticky='W')
            Label(window, text=section.days).grid(row=i + 1, column=4, sticky='W')
            Label(window, text=section.times).grid(row=i + 1, column=5, sticky='W')
            Label(window, text=section.capacity).grid(row=i + 1, column=6, sticky='W')
            Label(window, text=section.remaining).grid(row=i + 1, column=7, sticky='W')
            Label(window, text=section.instructor).grid(row=i + 1, column=8, sticky='W')
            Label(window, text=section.location).grid(row=i + 1, column=9, sticky='W')
            i = i + 1
        window.mainloop()

        input("Press enter to continue")

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
