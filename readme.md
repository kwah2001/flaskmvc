# COMP 3613 A1 - Student Conduct Tracker

# Project Requirements 

a commandline application needs to be developed so that users can track the conduct of students, the requirements for an application such as this are as follows:

 Create Student
 Search Student
 Add Student Review
  View Student Reviews


# Commands 
 add_student - allows the user to add a student to the database so that they can review or see reviews on them, each student would be given a unique ID number to allow them to be identified.

 search_student - once a student is in the database, the search student function would allow the user to find a specific student by entering their student ID number which is unique to them.

add_review - Once a student is in the database, the user is able to give them a review.

view_reviews - The user would be able to view the student’s reviews by entering their unique student ID into the system.

# How it's entered 
 flask user add_student{student_id} {student name}   
example =  flask user add_student 01 "Fake Name"

 flask user search_student{student_id}    
 example = flask user search_student 01

flask user add_review {student_id} {staff_id} {review_text}          
example = flask user add_review 01 1 "good job" 

 flask user view_reviews{student_id}                                          
example = flask user view_reviews 01

these show what parameters must be entered along with the command inside of the console


