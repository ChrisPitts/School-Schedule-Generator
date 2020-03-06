class Section:
    def __init__(self, course, array):
        self.course = course
        self.status = array[0]
        self.course_number = array[1]
        self.section_number = array[2]
        self.campus = array[3]
        self.days = array[4]
        self.times = array[5]
        self.capacity = array[6]
        self.remaining = array[7]
        self.instructor = array[8][0:len(array[8])-4]
        self.location = array[9]

    def get_times_in_minutes(self):
        times = []
        time_str = self.times[: self.times.index('-')]
        hour = int(time_str[: self.times.index(':')])
        minutes = int(time_str[self.times.index(':') + 1: time_str.index(' ')])
        am_pm = time_str[time_str.index(' ') + 1:]
        if am_pm == 'pm' and hour != 12:
            hour += 12
        times.append(hour*60 + minutes)

        time_str = self.times[self.times.index('-') + 1:]
        print(time_str)
        hour = int(time_str[: self.times.index(':')])
        minutes = int(time_str[self.times.index(':') + 1: time_str.index(' ')])
        am_pm = time_str[time_str.index(' ') + 1:]
        if am_pm == 'pm' and hour != 12:
            hour += 12
        times.append(hour * 60 + minutes)
        return times

    def conflicts(self, section):
        self_times = self.get_times_in_minutes()
        other_times = section.get_times_in_minutes()
        if other_times[0] < self_times[0] < other_times[1]:
            return True
        if other_times[0] < self_times[1] < other_times[1]:
            return True
        if self_times[0] < other_times[0] < self_times[1]:
            return True
        if self_times[0] < other_times[1] < self_times[1]:
            return True
        return False

    def get_conflicting_days(self, section):
        days = []
        if not self.conflicts(section):
            return days
        for day in section.days:
            if day in self.days:
                days.append(day)
        return days

    def print(self):
        print("%s %s.%s" % (self.course.subject, self.course.number, self.section_number))