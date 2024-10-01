# COMP 3613 A1 - Student Conduct Tracker

# Project Requirements 

a commandline application needs to be developed so that users can track the conduct of students, the requirements for an application such as this are as follows:

1) Create Student
2)Search Student
3)Add Student Review
4) View Student Reviews


# Commands 
1) add_student - allows the user to add a student to the database so that they can review or see reviews on them, each student would be given a unique ID number to allow them to be identified.
2) search_student - once a student is in the database, the search student function would allow the user to find a specific student by entering their student ID number which is unique to them.
3)add_review - Once a student is in the database, the user is able to give them a review and give them a rating that would be out of 5
4)view_reviews - The user would be able to view the student’s reviews by entering their unique student ID into the system.

# How it's entered 
1) flask user add_student{student_id} {student name}                            example =  flask user add_student 01 "Fake Name"
2) flask user search_student{student_id}                                        example = flask user search_student 01
3) flask user add_review {student_id} {staff_id} {review_text} {rating}         example = flask user add_review 01 1 "good job" 5
4) flask user view_reviews{student_id}                                          example = flask user view_reviews 01

these show what parameters must be entered along with the command inside of the console


