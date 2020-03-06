from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tkinter import *
import time
from Course import Course

SUBMIT_BUTTON_TEXT = 'Submit'
EXIT_BUTTON_TEXT = 'Exit'
BACK_BUTTON_TEXT = 'Back'
SUBJECT_LABEL = 'Select a subject'


class CourseReader:
    def __init__(self, browser):
        self.browser = browser

    def lookup_class(self):

        def prompt_subject():
            menu_elements = self.browser.find_elements(By.XPATH, '//*[@id="subj_id"]/option')
            subject_text = []
            for element in menu_elements:
                subject_text.append(element.text)

            subject_str = self.prompt_list(SUBJECT_LABEL, subject_text)
            print("line 27 reached")
            if subject_str == 'Back' or subject_str == 'Exit':
                return
            subject_menu = Select(
                self.browser.find_element_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr/td[2]/select'))
            subject_menu.select_by_visible_text(subject_str)
            self.browser.find_element_by_xpath('/html/body/div[3]/form/input[17]').click()
            prompt_course()

        def prompt_course():
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
            if course_str == 'Back':
                self.browser.back()
                Select(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr/td[2]/select')).\
                    deselect_all()
                prompt_subject()
                return
            if course_str == 'Exit':
                self.browser.back()
                return
            course_data[course_strings.index(course_str)][2].click()

            prompt_section()

        def prompt_section():

            def back():
                nonlocal window
                self.browser.back()
                window.destroy()
                prompt_course()

            def exit_menu():
                self.browser.back()
                self.browser.back()
                window.destroy()

            subject = self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[3]').text
            number = self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[4]').text
            name = self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[8]').text
            course = Course(subject, number, name)

            element_arr = self.browser.find_elements(By.XPATH, '/html/body/div[3]/form/table/tbody/tr')
            for i in range(3, len(element_arr) + 1):
                arr = []
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[1]/abbr' % i)
                    .text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[2]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[5]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[6]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[9]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[10]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[11]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[13]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[17]' % i).text)
                arr.append(
                    self.browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[%i]/td[19]' % i).text)
                course.add_section(arr)

            window = Tk()
            Label(window, text="%s %s %s" % (course.subject, course.number, course.name)).grid(row=0, column=0,
                                                                                               sticky='W')
            i = 1
            for key in course.sections:
                section = course.sections[key]
                Button(window, text="Select Section", command=lambda s=section: self.select_section(s, window)). \
                    grid(row=i, column=0, sticky='W')
                Label(window, text=section.status).grid(row=i, column=1, sticky='W')
                Label(window, text=section.course_number).grid(row=i, column=2, sticky='W')
                Label(window, text=section.section_number).grid(row=i, column=3, sticky='W')
                Label(window, text=section.campus).grid(row=i, column=4, sticky='W')
                Label(window, text=section.days).grid(row=i, column=5, sticky='W')
                Label(window, text=section.times).grid(row=i, column=6, sticky='W')
                Label(window, text=section.capacity).grid(row=i, column=7, sticky='W')
                Label(window, text=section.remaining).grid(row=i, column=8, sticky='W')
                Label(window, text=section.instructor).grid(row=i, column=9, sticky='W')
                Label(window, text=section.location).grid(row=i, column=10, sticky='W')
                i = i + 1
            Button(window, text=BACK_BUTTON_TEXT, command=back).grid(row=i, column=0, sticky='W')
            Button(window, text=EXIT_BUTTON_TEXT, command=exit_menu).grid(row=i, column=1, sticky='W')
            window.mainloop()

        prompt_subject()

    def prompt_list(self, label, strings):
        ret_str = ''

        def submit(status):
            nonlocal ret_str
            if status == 1:
                ret_str = 'Back'
            elif status == 2:
                ret_str = 'Exit'
            else:
                ret_str = str_var.get()
            window.quit()
            window.destroy()
        window = Tk()
        str_var = StringVar(window, strings[0])
        Label(window, text=label).grid(row=0, column=0, sticky='W')
        OptionMenu(window, str_var, *strings).grid(row=1, column=0, sticky='W')
        Button(window, text=SUBMIT_BUTTON_TEXT, command=lambda: submit(0)).grid(row=2, column=0, sticky='W')
        Button(window, text=BACK_BUTTON_TEXT, command=lambda: submit(1)).grid(row=2, column=1, sticky='W')
        Button(window, text=EXIT_BUTTON_TEXT, command=lambda: submit(2)).grid(row=2, column=2, sticky='W')
        
        window.mainloop()
        print("Line 155 reached")
        return ret_str

    def select_section(self, section, window):
        window.destroy()
        section.course.display = False
        print("Selected section %s %s.%s" % (section.course.subject, section.course.number, section.section_number))
