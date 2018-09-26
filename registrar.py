import datetime

class Course:
    def __init__(self, department, number, name, credits):
        self.department = department
        self.number = number
        self.name = name
        self.credits = credits

    def __str__(self): #EX: Algorithms, MPCS 55001, 3 credits
        return (self.name + ', ' + self.department + ' ' + str(self.number) + ' ('+ str(self.credits)+' credits)')

class CourseOffering:
    def __init__(self, course, section_number, year, quarter):
        self.course = course
        self.section_number = section_number
        self.instructor = None #instructor saved for later #6
        self.year = year
        self.quarter = quarter
        self.registered_students = [] #keep a list of registered students
        self.grades = {} #keep a dictionary of grades keyed by username

    def register_students(self, *args):
        for arg in args:
            self.registered_students.append(arg)
            arg.course_list.append(self) #add courseoffering to list of this student's course

    def get_students(self):
        return self.registered_students

    def submit_grade(self, student, grade):
        valid_grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
        if isinstance(student, Student) and grade in valid_grades: # if arg is instance of student and is a valid grade
            self.grades[student.username] = grade #add student grade to course offering
            key = self.__str__()
            student.transcript[key] = grade #add grade to student's transcript
        #elif not(isinstance(student, Student)) and grade in valid_grades:
        #    self.grades[student] = grade
        else:
            return 'Please enter a valid grade'

    def get_grade(self, student):
        if isinstance(student, Student): #if student for an arg
            return self.grades[student.username]
        else:
            return self.grades[student] #it will raise a key-val errot if arg is incorrect

    def __str__(self): #EX: Algorithms, MPCS 55001-1, Gerry Brady, (Fall 2017)
        if self.instructor: #if an instructor has been assigned
            return (self.course.name + ', ' + self.course.department +
                ' ' + str(self.course.number)+'-'+str(self.section_number) +
                ', ' + self.instructor.first_name + ' ' + self.instructor.last_name +
                ' (' + self.quarter + ' ' + str(self.year) + ')')
        else: #else just list course with no instructore name
            return (self.course.name + ', ' + self.course.department +
                ' ' + str(self.course.number)+'-'+str(self.section_number) +
                ' ' + ' (' + self.quarter + ' ' + str(self.year) + ')')

class Institution:
    def __init__(self, name, domain): #adding a domain to constructor, since there is no standard method you can build for it
        self.name = name
        self.domain = domain
        self.student_list = {} #key = student username, value = student object
        self.course_catalog = {} #key = course name; value = courses; #institution.coursecatalog[course].append(courseoffering)
        self.course_schedule = {} #key = course name; value = list course offerings
        self.faculty_list = {} #key = username #value = instructor

    def list_students(self):
        print('\n' + 'Enrolled Students (' + self.name + ') \n' + '-------------------------------------------')
        slist = [x.last_name + ', ' + x.first_name for x in self.student_list.values()]
        student_list = sorted(slist) #alphabetize
        for x in student_list:
            print(x)
        print('\n')

    def enroll_student(self, student):
        if isinstance(student,Student):
            if student.username in self.student_list.keys():
                print(student.first_name + ' ' + student.last_name + ' is already enrolled!')
            else:
                self.student_list[student.username] = student
        else:
            raise TypeError('Only accepts student object')

    def register_student_for_course(self,this_student,course_name, dept, number,section_number,year,quarter):
        for offering in self.course_schedule[course_name]:
            if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section_number == offering.section_number:
                if this_student in self.student_list.values(): #if student is enrolled in school
                    if this_student in offering.registered_students: #if student is already enrolled in this offering
                        print('\n' + this_student.first_name + ' ' + this_student.last_name + ' is already enrolled in this course' +'\n')
                    else:
                        offering.register_students(this_student)
                        print('\n' + this_student.first_name + ' ' + this_student.last_name + ' has been enrolled ' + offering.__str__() +'\n')

    def list_instructors(self):
        print('\n' + 'Instructor List (' + self.name + ') \n' + '-------------------------------------------')
        flist = [x.last_name + ', ' + x.first_name for x in self.faculty_list.values()]
        faculty_list = sorted(flist)
        for x in faculty_list:
            print(x)
        print('\n')

    def hire_instructor(self, instructor):
        if isinstance(instructor, Instructor):
            if instructor.username in self.faculty_list.keys():
                print(instructor.first_name + ' ' + instructor.last_name + ' already works at this institution!')
            else:
                self.faculty_list[instructor.username] = instructor
        else:
            raise TypeError('Only accepts instructor object')

    def assign_instructor(self,this_instructor,course_name, dept, number,section_number,year,quarter):
        for offering in self.course_schedule[course_name]:
            if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section_number == offering.section_number:
                if offering.instructor == this_instructor:
                    print('\n' + this_instructor.first_name + ' ' + this_instructor.last_name + ' is already teaching this course' +'\n')
                else:
                    offering.instructor = this_instructor
                    this_instructor.course_list.append(offering)
                    print('\n' + this_instructor.first_name + ' ' + this_instructor.last_name + ' has been assigned to teach ' + offering.__str__() +'\n')
            else:
                print('Course not found. Please create a course and course offering')

    def list_course_catalog(self):
        print('\n' + 'Course Catalog (' + self.name + ') \n' + '----------------------------------------')
        for item in self.course_catalog.values():
            print(item.__str__())
        print('\n')

    def list_course_schedule(self, year, quarter, dept=None):
        if dept: #filter by year, quarter, and department
            schedule = []
            print('\n' + 'Course Schedule (' + dept + ', '+ quarter + ' '+ str(year) + ') \n' + '----------------------------------------')
            for offerings in self.course_schedule.values(): #each item in list is a list of offerings for a given course
                filtered = list(filter(lambda x: x.year == year and x.quarter == quarter and x.course.department == dept, offerings)) #filters
                for item in filtered:
                    schedule.append(item.__str__())
            if schedule:
                for x in schedule:
                    print(x)
            else:
                print('No offerings during this semester')
            #return schedule
        else: #filter only by dept
            schedule = []
            print('\n' + 'Course Schedule (' + quarter + ' '+ str(year) + ') \n' + '----------------------------------------')
            if self.course_schedule: #if the course schedule is not empty
                for offerings in self.course_schedule.values():
                    filtered = list(filter(lambda x: x.year == year and x.quarter == quarter, offerings)) #filters
                    for item in filtered:
                        schedule.append(item.__str__())
                if schedule:
                    for x in schedule:
                        print(x)
                else:
                    print('No offerings scheduled during this semester')
            else:
                print('No offerings currently scheduled')
            #return schedule

    def list_registered_students(self,course_name, dept, number,section_number,year,quarter):
        for offering in self.course_schedule[course_name]:
            if dept == offering.course.department and number == offering.course.number and year == offering.year and quarter == offering.quarter and section_number == offering.section_number:
                print('Registered Students List (' + offering.__str__() + ') \n' + '------------------------------------------------------------')
                for student in offering.registered_students:
                    print(student.last_name + ', ' + student.first_name) #list of students in offering

    def add_course(self, course): #this adds courses, NOT course offerings
        if isinstance(course, Course):
            if course.name in self.course_catalog.keys(): #if course object is already in dict
                return 'Course has already been added'     #we dont need it
            else:
                self.course_catalog[course.name] = course #otherwise create a new entry in our course catalog
        else:
            raise TypeError('Only accepts course object as argument')

    def add_course_offering(self, course_offering):
        if isinstance(course_offering, CourseOffering): #check for right instance
            if course_offering.course.name in self.course_catalog.keys(): #check to see if course in course catalog
                self.course_schedule.setdefault(course_offering.course.name, []) #sets default values to list
                self.course_schedule[course_offering.course.name].append(course_offering)
            else:
                return 'Please create a course before creating course offering'
        else:
            raise TypeError('Only accepts course offering as argument')

class Person:
    def __init__(self, last_name, first_name, school, date_of_birth, username, affiliation):
        self.last_name = last_name
        self.first_name = first_name
        self.school = school
        self.date_of_birth = date_of_birth
        self.username = username
        self.affiliation = affiliation

    @property
    def email(self):
        return self.username + '@' + self.school.domain


class Instructor(Person):
    def __init__(self, last_name, first_name, school, date_of_birth, username):
        Person.__init__(self, last_name, first_name, school, date_of_birth, username, 'instructor')
        self.course_list = [] # key = self.course.name

    def list_courses(self,year=None,quarter=None):
        if year and quarter: #filter by year and quarter
            filtered = list(filter(lambda x: x.year == year and x.quarter == quarter, self.course_list)) #filters
            final = sorted(filtered, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]
        elif year: #only year arg given
            filtered = list(filter(lambda x: x.year == year, self.course_list)) #filters
            final = sorted(filtered, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]

        elif quarter: #only quarter arg given
            filtered = list(filter(lambda x: x.quarter == quarter, self.course_list)) #filters
            final = sorted(filtered, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]

        else: #no filters given, default to None
            final = sorted(self.course_list, key = lambda x: (x.year, x.quarter), reverse=True) #sorts
            return [x.__str__() for x in final]

    def __str__(self):
        return ('\n' + 'Instructor Name: ' + self.first_name + ' ' + self.last_name + '\n' +
            'School: ' + self.school.name + '\n' +
            'DOB: ' + self.date_of_birth.strftime('%b %d, %Y') + '\n' +
            'Username: ' + self.username + '\n')

class Student(Person):
    def __init__(self, last_name, first_name, school, date_of_birth, username):
        Person.__init__(self, last_name, first_name, school, date_of_birth, username, 'student')
        self.course_list = [] #list of offering objects
        self.transcript = {} #course:grade

    def list_courses(self):
        ordered = sorted(self.transcript.keys(), key = lambda x: (x.year, x.quarter), reverse=True)
        return ordered

    @property
    def credits(self):
        total = 0
        for x in self.course_list:
            total += x.course.credits
        return total

    @property
    def gpa(self):
        earned = 0
        available = 0

        grade_scale = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33,'B':3.0,'B-':2.67, 'C+':2.33,'C':2.0,'C-':1.67, 'D+':1.33, 'D':1.0, 'D-': 0.67,'F':0}

        for x in self.course_list:
            if self.username in x.grades.keys(): #check to see if a grade has already been submitted
                earned += (grade_scale[x.get_grade(self)] * x.course.credits)
                available += x.course.credits

        if available == 0:
            GPA = 0
        else:
            GPA = earned / available

        return GPA

    def __str__(self):
        return ('\n' + 'Student Name: ' + self.first_name + ' ' + self.last_name + '\n' +
            'School: ' + self.school.name + '\n' +
            'DOB: ' + self.date_of_birth.strftime('%b %d, %Y') + '\n' +
            'Username: ' + self.username + '\n' +
            'Email: ' + self.email + '\n' +
            'GPA: ' + str(self.gpa) + '\n' +
            'Credits: ' + str(self.credits) + '\n')
