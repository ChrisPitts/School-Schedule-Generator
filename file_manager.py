import data_manager
import os

FILE_DIR = "files"


def update_data(browser):
    pass


def save_data():
    if not os.path.exists("%s/%s" % (FILE_DIR, data_manager.file_name)):
        os.mkdir("%s/%s" % (FILE_DIR, data_manager.file_name))
    course_file = open('%s/%s/courses.txt' % (FILE_DIR, data_manager.file_name), 'w')
    section_file  = open('%s/%s/sections.txt' % (FILE_DIR, data_manager.file_name), 'w')
    for key in data_manager.courses:
        course_file.write(data_manager.courses[key].subject)
        course_file.write('\0')
        course_file.write(data_manager.courses[key].number)
        course_file.write('\0')
        course_file.write(data_manager.courses[key].display)
        course_file.write('\n')

    for key in data_manager.selected_sections:
        pass
