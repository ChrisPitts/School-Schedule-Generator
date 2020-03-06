from Section import Section


class Course:
    courses = dict()

    def __init__(self, subject, number, name):
        self.name = name
        self.subject = subject
        self.number = number
        self.sections = dict()
        self.display = True

    # def __init__(self, subject, number, array):
    #     self(subject, number)
    #     for arr in array:
    #         self.sections.append(Section(self, arr))

    def add_section(self, arr):
        section = Section(self, arr)
        self.sections[section.course_number] = section

    def print(self):
        for s in self.sections:
            print("%s %s.%s\tStatus: %s\tCRN: %s\tCampus: %s\tDays: %s\tTimes: %s\tCapacity: %s\t"
                  "Remaining: %s\tInstructor: %s\tLocation: %s" %
                  (self.subject, self.number, self.sections[s].section_number, self.sections[s].status,
                   self.sections[s].course_number, self.sections[s].campus, self.sections[s].days, self.sections[s].times,
                   self.sections[s].capacity, self.sections[s].remaining, self.sections[s].instructor,
                   self.sections[s].location))
