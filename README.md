# University Course Registration System

The program is a basic system for the maintenance of students' academic records at a university. `registrar.py` contains program logic, and `registration.py` allows the user to run the program in the command line. If you would like data to persist beyond the current session, users must save the data to a .pickle file. 

**Course**  
A class representing a course offered (possibly repeatedly) at a university (e.g., MPCS 55001 at University of Chicago).  
  
Attributes
- department (e.g., MATH, MPCS, PHYSICS, STATS, ENGLISH)
- number (e.g., 55001)
- name (e.g., Algorithms)
- credits (An integer value. The number of credits awarded for passing the course.)

**CourseOffering**  
A class representing a specific offering of a course. This class combines the general idea of a course (e.g., Algorithms offered on a regular basis at the school) with a specific instance of it being offered (e.g., Fall 2017).    

Attributes  
- course (An instance of the Course class.)
- section_number (A section number for the offering (e.g. 1))
- instructor (e.g., Joe Smith)
- year (e.g., 2017)
- quarter (e.g., FALL)

Behavior  
- _register_students_ : Takes an arbitrary number of instances of the student class and adds the students to the course.
- _get_students_ : Returns a list of instances of the Student class representing those that have registered for the course.
- _submit_grade_ : Takes an instance of the student class OR a student username and a letter grade (e.g., A+, A, A-, B+, B, B-, …) and sets the student's letter grade for the course. If the grade has already been set, this operation overwrites the existing grade.  
- _get_grade_ : Takes an instance of the student class OR a student username and returns the student's letter grade.
Jason Goode
Institution
A class representing a university (e.g., University of Chicago).
Attributes
• name
• domain
Behavior
• list_students : Return a list of all students enrolled.
• enroll_student : Accept an instance of the Student class and adds it.
• list_instructors : Return a list of all instructors employed at the university.
• hire_instructor : Accept an instance of the instructor class and add it.
• list_course_catalog: Return a list of all courses available at the university.
• list_course_schedule : Given a year and quarter, return a list of course offerings in the specified time period.
Optionally accept a department name argument. If the department name argument is given, filter the results list to exclude course offerings from any other department.
• add_course : Adds an instance of the Course class to the university's course catalog.
• add_course_offering : Takes an instance of the Course class and adds it to the university's course schedule.
Person
A class representing the people involved with the university.
Attributes
• last_name
• first_name
• school (A reference to an instance of the Institution class.)
• date_of_birth (An instance of the datetime.datetime class.)
• username (Equivalent to UChicago CNetID. Used as a unique identifier across the system.)
• affiliation (e.g., student, faculty, staff, etc)
• email (A property. Should resolve to [self.username]@[self.school.domain])
Instructor
A class representing an instructor of a course at a university. Inherits from Person class.
Behavior
• list_courses : Return a list of courses taught by the instructor in reverse-chronological order (most recent first).
Jason Goode
Student
A class representing a student at a university. Inherits from Person class.
Behavior
• list_courses : Return a list of courses the student has taken (or is currently registered for) in reverse-chronological order (most recent first).
• credits : Returns the number of credits earned toward graduation. Assume all credits are earned toward a single degree.
• gpa : Returns the student's grade point average (GPA) calculated as the average of grade points earned for each course, weighted by credits earned for the corresponding course. Pluses and minuses are available
Registration.py
This script makes an interactive command prompt that allows users to use the registration system
Menu
1 Create a course
2 Schedule a course offering
3 List course catalog
4 List course schedule
5 Hire an instructor
6 Assign an instructor to a course
7 Enroll a student
8 Register a student for a course
9 List enrolled students
10 List students registered for a course
11 List faculty
12 Submit student grade
13 Get student records
14 Exit
Actions
• If the user enters 1, 2, 5, or 7, for instance, present the user with a series of prompts for the relevant information for creating a course, course offering, instructor, or student instance, respectively.
• If the user enters 3, display a list of the courses in the course catalog and their relevant information.
• If the user enters 4, prompt the user for a year and quarter. Then display a list of the courses offered in the given year and quarter and their relevant information.
• If the user enters 6, prompt the user for an instructor username and a course department , number , section_number , year , and quarter . These values should
Jason Goode
uniquely determine a single instance of the CourseOffering class. Then associate that instructor with the given course offering.
• If the user enters 8, prompt the user for a student username , course department , number , section_number , year , and quarter . These values should uniquely determine a single CourseOffering . Associate the given student with the given course offering.
• If the user enters 9, display a list of all students enrolled at the university, along with their relevant info.
• If the user enters 10, prompt the user for the course department , number , section_number , year , and quarter . Then display the list of students enrolled in the given course.
• If the user enters 12, prompt the user for a student username , the identifying information for a course offering, and a letter grade. Update the student's records accordingly.
• If the user enters 13, prompt the user for a student username . After the username is supplied, display the student records, including GPA, credits earned, and transcript
• If the user enters 14, the program should exit and ask the user if they would like to save their data (to a new or existing .pickle file)
• If the user enters anything besides 1-14, the program will re-prompt for a valid entry
