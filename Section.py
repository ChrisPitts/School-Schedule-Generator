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