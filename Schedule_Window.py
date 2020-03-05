from tkinter import *
from Course import Course
from Section import Section
# import data_manager


class WindowSchedule:

    def __init__(self, reader):
        self.reader = reader
        reader.lookup_class()
        #self.window = Tk()

        # Set up course list frame
        #self.course_list_frame = Frame(self.window)
        #self.course_list_frame.grid(row=0, column=0, sticky='W')
        #i = 0
        #for course_key in data_manager.courses:
        #    course = data_manager.courses[course_key]
        #    Label(self.course_list_frame, text="%s %s" % (course.subject, course.number)).grid(
        #        row=i, column=0, sticky='W')
        #    i = i + 1

        # Set up schedule frame
        #self.schedule_frame = Frame(self.window)
        #self.schedule_frame.grid(row=0, column=1, sticky='W')
        #self.window.mainloop()


#data_manager.add_course(Course('CS', '2336'))
#data_manager.add_course(Course('MATH', '2413'))
#schedule = WindowSchedule()
