# University Course Registration System

The program is a basic system for the maintenance of students' academic records at a university. `registrar.py` contains program logic, and `registration.py` allows the user to run the program in the command line. If you would like data to persist beyond the current session, users must save the data to a .pickle file. 

## Getting Started 

- Call `python3 registration.py` to start the interactive command prompt
- Type `14` or `Ctrl-C` to quit

**Menu**  
1. Create a course  
2. Schedule a course offering
3. List course catalog 
4. List course schedule
5. Hire an instructor
6. Assign an instructor to a course
7. Enroll a student
8. Register a student for a course
9. List enrolled students
10. List students registered for a course
11. List faculty
12. Submit student grade
13. Get student records
14. Exit

## Features & Functionality  

#### Course  
A class representing a course offered (possibly repeatedly) at a university (e.g., MPCS 55001 at University of Chicago).  
  
Attributes
- department (e.g., MATH, MPCS, PHYSICS, STATS, ENGLISH)
- number (e.g., 55001)
- name (e.g., Algorithms)
- credits (An integer value. The number of credits awarded for passing the course.)

#### CourseOffering 
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

#### Institution  
A class representing a university (e.g., University of Chicago).  

Attributes
- name (e.g. University of Chicago)
- domain (e.g. `@uchicago.edu`)

Behavior  
- _list_students_ : Return a list of all students enrolled.
- _enroll_student_ : Accept an instance of the Student class and adds it.
- _list_instructors_ : Return a list of all instructors employed at the university.
- _hire_instructor_ : Accept an instance of the instructor class and add it.
- _list_course_catalog_: Return a list of all courses available at the university.
- _list_course_schedule_ : Given a year and quarter, return a list of course offerings in the specified time period.  Optionally accept a department name argument. If the department name argument is given, filter the results list to exclude course offerings from any other department.
- _add_course_ : Adds an instance of the Course class to the university's course catalog.
- _add_course_offering_ : Takes an instance of the Course class and adds it to the university's course schedule.

#### Person  
A class representing the people involved with the university.    
  
Attributes
- last_name
- first_name
- school (A reference to an instance of the Institution class.)
- date_of_birth (An instance of the datetime.datetime class.)
- username (Equivalent to UChicago CNetID. Used as a unique identifier across the system.)
- affiliation (e.g., student, faculty, staff, etc)
- email (A property. Should resolve to [self.username]@[self.school.domain])

#### Instructor
A class representing an instructor of a course at a university. Inherits from Person class.  

Behavior  
- _list_courses_ : Return a list of courses taught by the instructor in reverse-chronological order (most recent first).

#### Student  
A class representing a student at a university. Inherits from Person class.

Behavior  
- _list_courses_ : Return a list of courses the student has taken (or is currently registered for) in reverse-chronological order (most recent first).
- _credits_ : Returns the number of credits earned toward graduation. Assume all credits are earned toward a single degree.
- _gpa_ : Returns the student's grade point average (GPA) calculated as the average of grade points earned for each course, weighted by credits earned for the corresponding course. Pluses and minuses are available  
