from tkinter import *

WEEKDAYS = {'M':0, 'T':1, 'W':2, 'H':3, 'F':4}
FRAME_HEIGHT = 50
TIME_WIDTH = 50
CANVAS_HEIGHT = 400


class FrameSchedule:
    def __init__(self, frame):
        self.frame = frame
        frame.config(height=FRAME_HEIGHT)
        frame.config(width=50, height=1000)
        self.height_per_block = 0
        self.start_time = -1
        self.end_time = -1
        self.canvases = []
        self.sections = []
        self.drawn_sections = []
        self.canvas_widths = []

        for i in WEEKDAYS:
            Label(frame, text=i, padx=0).grid(row=0, column=WEEKDAYS[i], sticky='W')
            canvas = Canvas(frame, width=TIME_WIDTH, height=CANVAS_HEIGHT, bd=1,relief=RIDGE)
            canvas.grid(row=1, column=WEEKDAYS[i], sticky='W')
            self.canvases.append(canvas)
            self.drawn_sections.append([])

    def add_section(self, section):
        self.sections.append(section)
        hours = section.get_times_in_minutes()
        print(self.start_time)
        if self.start_time == -1:
            self.start_time = hours[0]
            self.end_time = hours[1]
            self.redraw()
        elif self.start_time > hours[0]:
            self.start_time = hours[0]
            self.redraw()
        elif self.end_time < hours[1]:
            self.end_time = hours[1]
            self.redraw()
        self.draw(section)

    def draw(self,section):
        times = section.get_times_in_minutes()
        section.print()
        print(times)

        for day in section.days:
            index = WEEKDAYS[day]
            canvas = self.canvases[index]
            x_start = 0
            for sec in self.drawn_sections[index]:
                if sec.conflicts(section):
                    x_start += TIME_WIDTH
            x_end = x_start + TIME_WIDTH
            y_start = ((times[0] - self.start_time)//30) * self.height_per_block
            y_end = (( times[1] + (30 - times[1]%30) - self.start_time) // 30) * self.height_per_block
            #print(self.start_time)
            print('%s X1:%s X2:%s Y1:%s Y2:%s' % (section.section_number, x_start, x_end, y_start, y_end))
            #print('Times\t%s:%s - %s:%s' % (times[0]//60, times[0]%60, times[1]//60, times[1]%60))
            #print("Minutes\t%s - %s" % (times[0], times[1]))
            canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="red")
            self.drawn_sections[index].append(section)

    def redraw(self):
        self.height_per_block = CANVAS_HEIGHT / ((self.end_time - self.start_time) / 30)
        for canvas in self.canvases:
            canvas.delete(ALL)
        for section in self.sections:
            self.draw(section)
