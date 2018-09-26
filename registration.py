import registrar as reg
import datetime
import pickle
from pathlib import Path

print('\n' + 'Welcome to the Registration System \n')

#Data Persistence
load_existing = input('Would you like to load existing data? Enter Yes or No: ')
load_existing = load_existing.lower()

if load_existing == 'yes':
    file_path = input('Please enter the filepath: ') #must be a .pickle file
    pickle_file = open(file_path, 'rb')
    institution = pickle.load(pickle_file) #load existing regsitration

else: #create a new institution class
    name = input('Please enter an institution name: ')
    domain = input('Please enter a domain name (format = <institution>.edu): ')
    institution = reg.Institution(name,domain)

menu_string = '\n' + 'Please select an option from the following:' + '\n\n' + \
                'MENU' + '\n' + \
                '----------------------------------------' + '\n' + \
                '1 Create a course' + '\n' + \
                '2 Schedule a course offering' + '\n' + \
                '3 List course catalog' + '\n' + \
                '4 List course schedule' + '\n' + \
                '5 Hire an instructor' + '\n' + \
                '6 Assign an instructor to a course' + '\n' + \
                '7 Enroll a student' + '\n' + \
                '8 Register a student for a course' + '\n' + \
                '9 List enrolled students' + '\n' + \
                '10 List students registered for a course' + '\n' + \
                '11 List faculty' + '\n' + \
                '12 Submit student grade' + '\n' + \
                '13 Get student records' + '\n' + \
                '14 EXIT' + '\n'

valid_options = ['1','2','3','4','5','6','7','8','9','10','11','12', '13']
valid_quarters = ['Fall','Winter','Spring','Summer']
valid_grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']

while True:
    while True:
        var = input('\n ...press enter to continue...')
        if not(var):
            print(menu_string)
            menu_input = input('Enter Menu Choice: ')
            break
        else:
            print('Press enter to continue')
    if menu_input == '14':
        print('\n' + 'EXITING...Thank you!' + '\n')
        break
    elif menu_input in valid_options:
        #OPTION 1 - CREATE COURSE
        if menu_input == '1':
            #course args
            while True:
                dept = input('Please enter department code: ')
                if isinstance(dept, str) and len(dept) <= 4:
                    break
                else:
                    print('Invalid entry. Please enter 4 letter dept')

            while True:
                num = int(input('Please enter a course number: '))
                if isinstance(num,int):
                    break
                else:
                    print('Invalid entry. Please enter a number')

            name = input('Please enter name: ')
            while True:
                credits = int(input('Please enter number of credits: '))
                if isinstance(credits,int) and credits <= 4:
                    break
                else:
                    print('Invalid entry. Credit must be integer <= 4')

            course = reg.Course(dept,num,name,credits) #create a course object
            institution.add_course(course) #add course
            print('\n' + course.name + ' added to course list!' + '\n')

        #OPTION 2 - SCHEDULE COURSE OFFERING
        elif menu_input == '2':
            while True:
                key = input('Course Name: ')
                if key in institution.course_catalog.keys():
                    course = institution.course_catalog[key]
                    break
                else:
                    print('This course is not currently offered. Please add new course or select from the following offerings: ' + '\n' + institution.course_catalog.keys())

            section = int(input('Please enter a section number: '))
            while True:
                quarter = input('Please enter quarter (Fall,Winter,Spring,Summer): ')
                if quarter in valid_quarters:
                    break
                else:
                    print('Please enter a valid quarter')

            while True:
                year = int(input('Please enter year (YYYY): '))
                if year >= 1900 and year <= 2100:
                    break
                else:
                    print('Please enter a year between 1900 and 2100')

            course_offering = reg.CourseOffering(course,section,year,quarter)
            institution.add_course_offering(course_offering)
            print('\n' + course_offering.__str__() + ' has been scheduled!' + '\n')

        #OPTION 3 - LIST COURSE CATALOG
        elif menu_input == '3':
            institution.list_course_catalog()

        #OPTION 4 - LIST COURSE SCHEDULE
        elif menu_input == '4':
            while True:
                quarter = input('Please enter quarter (Fall,Winter,Spring,Summer): ')
                if quarter in valid_quarters:
                    break
                else:
                    print('Please enter quarter (Fall,Winter,Spring,Summer):')

            while True:
                year = int(input('Please enter year (YYYY): '))
                if year >= 1900 and year <= 2100:
                    break
                else:
                    print('Please enter a year between 1900 and 2100')

            institution.list_course_schedule(year,quarter)

        #OPTION 5 - HIRE INSTRUCTOR
        elif menu_input == '5':
            last_name = input('Please enter instructor last name: ')
            first_name = input('Please enter instructor first name: ')
            while True:
                year = int(input('Please enter year (YYYY): '))
                if year >= 1900 and year <= 2100:
                    break
                else:
                    print('Please enter a year between 1900 and 2100')

            month = int(input('Please enter birth month(MM): '))
            day = int(input('Please enter birth day (DD): '))
            dob = datetime.date(year,month,day)
            username = input('Please give instructor a unique username: ')
            instructor = reg.Instructor(last_name,first_name,institution,dob,username)
            institution.hire_instructor(instructor)
            print('\n' + 'You have hired ' + instructor.first_name + ' ' + instructor.last_name + '\n')

        #OPTION 6 - ASSIGN INSTRUCTOR
        elif menu_input == '6':
            while True:
                username = input('Instructor username: ')
                if username in institution.faculty_list.keys():
                    this_instructor = institution.faculty_list[username]
                    break
                else:
                    print('Invalid username, please try again')

            while True:
                course_name = input('Course name: ')
                if course_name in institution.course_catalog.keys():
                    break
                else:
                    print('Invalid coursename, please ensure course has been created first')

            dept = input('Department: ')
            number = int(input('Course Number: '))

            while True:
                quarter = input('Please enter quarter (Fall,Winter,Spring,Summer): ')
                if quarter in valid_quarters:
                    break
                else:
                    print('Please enter quarter (Fall,Winter,Spring,Summer):')

            while True:
                year = int(input('Please enter year (YYYY): '))
                if year >= 1900 and year <= 2100:
                    break
                else:
                    print('Please enter a year between 1900 and 2100')

            section = int(input('Section Number: '))

            institution.assign_instructor(this_instructor,course_name, dept, number, section, year, quarter)

        #OPTION 7 - ENROLL A STUDENT
        elif menu_input == '7':
            last_name = input('Last name: ')
            first_name = input('First name: ')
            year = int(input('Birth year (YYYY): '))
            month = int(input('Birth month(MM): '))
            day = int(input('Birth day (DD): '))
            dob = datetime.date(year,month,day)
            username = input('Assign unique username: ')
            student = reg.Student(last_name, first_name, institution, dob, username)
            institution.enroll_student(student)
            print('\n' + student.first_name + ' ' + student.last_name + ' has been enrolled!'+'\n')

        #OPTION 8 - REGISTER A STUDENT FOR A COURSE
        elif menu_input == '8':
            while True:
                username = input('Student username: ')
                if username in institution.student_list.keys():
                    student = institution.student_list[username]
                    break
                else:
                    print('Student username not found, please enroll student or try again')
            while True:
                course_name = input('Course name: ')
                if course_name in institution.course_catalog.keys():
                    break
                else:
                    print('Course name not found, please enter valid coursename')

            dept = input('Department: ')
            number = int(input('Course Number: '))
            year = int(input('Please enter year offered (YYYY): '))
            quarter = input('Please enter quarter offered (Fall,Winter,Spring,Summer): ')
            section_number = int(input('Section Number: '))
            institution.register_student_for_course(student,course_name,dept,number,section_number,year,quarter)

        #OPTION 9 - LIST ENROLLED STUDENTS
        elif menu_input == '9':
            institution.list_students()

        #OPTION 10 - LIST STUDENTS REGISTERED FOR A COURSE
        elif menu_input == '10':
            while True:
                course_name = input('Course name: ')
                if course_name in institution.course_catalog.keys():
                    break
                else:
                    print('Course name not found, please enter valid coursename')
            dept = input('Department: ')
            number = int(input('Course Number: '))
            year = int(input('Please enter year offered (YYYY): '))
            quarter = input('Please enter quarter offered (Fall,Winter,Spring,Summer): ')
            section = int(input('Section Number: '))
            institution.list_registered_students(course_name,dept,number, section,year,quarter)

        #OPTION 11 - LIST FACULTY
        elif menu_input == '11':
            institution.list_instructors()

        #OPTION 12 - SUBMIT STUDENT GRADE
        elif menu_input == '12':
            while True:
                username = input('Student username: ')
                if username in institution.student_list.keys():
                    student = institution.student_list[username]
                    break
                else:
                    print('Student username not found, please enroll student or try again')
            while True:
                course_name = input('Course name: ')
                if course_name in institution.course_catalog.keys():
                    break
                else:
                    print('Course name not found, please enter valid coursename')
            dept = input('Department: ')
            number = int(input('Course Number: '))
            while True:
                quarter = input('Please enter quarter (Fall,Winter,Spring,Summer): ')
                if quarter in valid_quarters:
                    break
                else:
                    print('Please enter quarter (Fall,Winter,Spring,Summer):')

            while True:
                year = int(input('Please enter year (YYYY): '))
                if year >= 1900 and year <= 2100:
                    break
                else:
                    print('Please enter a year between 1900 and 2100')
            section = int(input('Section Number: '))
            while True:
                grade = input('Enter a grade (A to F): ')
                if grade in valid_grades:
                    break
                else:
                    print('Please enter a valid grade')

            for offering in institution.course_schedule[course_name]:
                if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section == offering.section_number:
                    offering.submit_grade(student,grade)

        #OPTION 13 - GET STUDENT RECORDS
        elif menu_input == '13':
            username = input('Enter student username: ')
            student = institution.student_list[username]
            print(student.__str__())
            print('Transcript' + '\n' + '----------'  + '\n')
            for k,v in student.transcript.items():
                print(v + ', ' + k)
    else:
        print('\n' + 'INVALID MENU OPTION: Please try again' + '\n')

save_session = input('Would you like to the contents of this session? Enter Yes or No: ')
save_session = save_session.lower()

if save_session == 'yes':
    file_name = input('Please enter a filename for saving your data (this is a .pickle file): ')
    pickle_file = open(file_name, 'wb')
    pickle.dump(institution, pickle_file)
    pickle_file.close
    print('Session contents saved, goodbye!')
else:
    print('Goodbye!')
