import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.models import Student
from App.models import Review
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, add_student, search_student, add_review, view_student_reviews )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())



#add student command
@user_cli.command("add_student", help="Adds a new student")
@click.argument("student_id", type=int)
@click.argument("student_name")
def add_student_command(student_id, student_name):
    result = add_student(student_id, student_name)
    print(result["message"])


#search student command
@user_cli.command("search_student", help="Search for a student by ID")
@click.argument("student_id")
def search_student_command(student_id):
    result = search_student(student_id)  
    print(result)

#add student review command
@user_cli.command("add_review", help="Add a review for a student")
@click.argument("student_id")
@click.argument("staff_id")
@click.argument("review_text")
@click.argument("rating", type=int)
def add_review_command(student_id, staff_id, review_text, rating):
    result = add_review(student_id, staff_id, review_text, rating)
    print(f"Review added: {result}")

#view student review command
@user_cli.command("view_reviews", help="View reviews for a specific student")
@click.argument("student_id")
def view_reviews_command(student_id):
    result = view_student_reviews(student_id)
    print(result)


app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)