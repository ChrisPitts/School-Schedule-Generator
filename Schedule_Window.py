from tkinter import *
from Course import Course
from Section import Section
import data_manager
from schedule_frame import FrameSchedule


class WindowSchedule:

    def __init__(self):
        #self.reader = reader
        #reader.lookup_class()
        self.window = Tk()

        # Set up course list frame
        self.course_list_frame = Frame(self.window)
        self.course_list_frame.grid(row=0, column=0, sticky='W')

        # Course Frame
        self.course_frame = Frame(self.course_list_frame, bd=1, relief=RIDGE)
        self.course_frame.grid(row=0, column=0, sticky='W')

        i = 0
        for course_key in data_manager.courses:
            course = data_manager.courses[course_key]
            Label(self.course_frame, text="%s %s" % (course.subject, course.number)).grid(
                row=i, column=0, sticky='W')
            i = i + 1

        # Sections Frame
        self.sections_frame = Frame(self.course_list_frame, bd=1, relief=RIDGE)
        self.sections_frame.grid(row=1, column=0, sticky='W')

        # Section Data Frame
        self.section_data_frame = Frame(self.course_list_frame, bd=1, relief=RIDGE)
        self.section_data_frame.grid(row=2, column=0, sticky='W')

        self.section_data_name_label = Label(self.section_data_frame, text='Course Name: ')
        self.section_data_name_label.grid(row=0, column=0, sticky='W')


        # Set up schedule frame
        self.schedule_frame = FrameSchedule(Frame(self.window, bd=1, relief=RIDGE))
        self.schedule_frame.frame.grid(row=0, column=1, sticky='W')


        # Set up buttons frame

        for course in data_manager.courses:
            for section in data_manager.courses[course].sections:
                self.schedule_frame.draw(data_manager.courses[course].sections[section])

        self.window.mainloop()


course_1_array = [
    'O',
    '23135',
    '003',
    'M',
    'MWF',
    '08:00 am-10:50 am',
    '30',
    '25',
    'Jack Harris (P)',
    'DERR 242'
]

course_2_array = [
    'O',
    '23465',
    '252',
    'M',
    'TH',
    '12:00 pm-1:50 pm',
    '200',
    '150',
    'James Erikson (P)',
    'INGM 320'
]

course_3_array = [
    'O',
    '23465',
    '252',
    'M',
    'TH',
    '6:00 pm-7:20 pm',
    '200',
    '150',
    'James Erikson (P)',
    'INGM 320'
]

course = Course('CS', '2336', "Computer Science 1")
course.add_section(course_1_array)
data_manager.add_course(course)
course = Course('MATH', '2413', "Calculus 1")
course.add_section(course_2_array)
course.add_section(course_3_array)
data_manager.add_course(course)


schedule = WindowSchedule()
