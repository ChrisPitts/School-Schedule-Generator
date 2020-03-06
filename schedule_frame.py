from tkinter import *

WEEKDAYS = {'M':0, 'T':1, 'W':2, 'H':3, 'F':4}
FRAME_HEIGHT = 50
TIME_WIDTH = 120
CANVAS_HEIGHT = 600


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
            self.canvas_widths.append(TIME_WIDTH)

    def add_section(self, section):
        self.sections.append(section)
        hours = section.get_times_in_minutes()

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
        #section.print()
        #print(times)

        for day in section.days:
            index = WEEKDAYS[day]
            canvas = self.canvases[index]
            x_start = 0
            conflicts = self.get_num_conflicting_sections(section, day)
            print(conflicts)
            x_start += TIME_WIDTH * conflicts
            if canvas.winfo_width() < TIME_WIDTH * conflicts:
                canvas.config(width= TIME_WIDTH*(conflicts + 1))
            x_end = x_start + TIME_WIDTH
            y_start = ((times[0] - self.start_time)//30) * self.height_per_block
            y_end = (( times[1] + (30 - times[1]%30) - self.start_time) // 30) * self.height_per_block
            canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="red")
            course_str = "%s %s.%s\n%s\n%s" % (section.course.subject, section.course.number, section.section_number,
                                               section.instructor, section.times)
            canvas.create_text(x_start + 5, y_start + 10, anchor='nw', text=course_str)
            self.drawn_sections[index].append(section)

    def redraw(self):
        self.height_per_block = CANVAS_HEIGHT / ((self.end_time - self.start_time) / 30)
        for i in range(0, len(self.canvases)):
            self.canvases[i].delete(ALL)
            self.canvases[i].config(width=TIME_WIDTH)
            self.canvas_widths[i] = TIME_WIDTH
            self.drawn_sections[i] = []
        for section in self.sections:
            self.draw(section)

    def get_num_conflicting_sections(self, section, day):
        num_conflicts = 0
        for sec in self.drawn_sections[WEEKDAYS[day]]:
            if day in section.get_conflicting_days(sec):
                num_conflicts += 1
        return num_conflicts
