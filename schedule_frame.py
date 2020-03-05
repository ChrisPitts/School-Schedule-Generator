from tkinter import *

WEEKDAYS = {'M':0, 'T':1, 'W':2, 'H':3, 'F':4}
FRAME_HEIGHT = 50
HEIGHT_PER_30 = 5
TIME_WIDTH = 50


class FrameSchedule:
    def __init__(self, frame):
        self.frame = frame
        frame.config(height=FRAME_HEIGHT)
        frame.config(width=50)
        self.height_per_block = 0
        self.start_time = -1
        self.end_time = -1
        self.canvases = []
        self.sections = []
        self.drawn_sections = []
        self.canvas_widths = []

        for i in WEEKDAYS:
            Label(frame, text=i, padx=0).grid(row=0, column=WEEKDAYS[i], sticky='W')
            canvas = Canvas(frame, width=TIME_WIDTH)
            canvas.grid(row=1, column=WEEKDAYS[i], sticky='W')
            self.canvases.append(canvas)
            self.drawn_sections.append([])

    def add_section(self, section):
        self.sections.append(section)
        hours = section.get_times_in_minutes()
        if self.start_time == -1:
            self.start_time = hours[0]
            self.end_time = hours[1]
            self.redraw()
        self.draw(section)

    def draw(self,section):
        times = section.get_times_in_minutes()
        for day in section.days:
            index = WEEKDAYS[day]
            canvas = self.canvases[index]
            x_start = 0
            for sec in self.drawn_sections[index]:
                if sec.conflicts(section):
                    x_start += TIME_WIDTH
            x_end = x_start + TIME_WIDTH
            y_start = times[0]/30
            y_end = (( times[1] + (30 - times[1]%30) ) / 30) * HEIGHT_PER_30
            print('%s X1:%s X2:%s Y1:%s Y2:%s' % (section.course.name, x_start, x_end, y_start, y_end))
            canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="red")
            self.drawn_sections[index].append(section)

    def redraw(self):
        for canvas in self.canvases:
            canvas.delete(ALL)
            canvas.config(height= HEIGHT_PER_30 * ((self.end_time - self.start_time)/30))
        for section in self.sections:
            self.draw(section)
