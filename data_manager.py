courses = dict()
selected_sections = dict()


def add_course(course):
    if courses.get('%s %s' % (course.subject, course.number)) is None:
        courses['%s %s' % (course.subject, course.number)] = course


def remove_course(course):
    del courses['%s %s' % (course.subject, course.number)]


def select_section(section):
    section.course.display = True
    del selected_sections[section.course_number]
