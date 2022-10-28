from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganizationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.

studentOrganizationDetails = {  
                                "Noah": "Running club",
                                "Charlie": "Soccer club",
                                "Jose": "Computer club",
                                "Adam": "Swimming club",
                                "Jesse":"Chess club"
                            }

#
# /: index.html
#
@app.route('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    date = datetime.datetime.now()
    currentDate = date.strftime( "%d-%m-%Y %H:%M:%S" )
    return render_template( 'index.html', currentDate=currentDate )

#
# /calculate: form.html + result.html
#
@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template("form.html")

@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']

    if not number:
        result = "No number given"
    elif number.isdigit() == False:
        result = "Number given was not a positive number"
    else:
        number = int(number)
        if number%2==0:
            result = "Given number is even"
        else:
            result = "Given number is odd"

    return render_template('result.html', result=result)

#
# /addStudentOrganization: studentForm.html + studentDetails.html
#

@app.get('/addStudentOrganization')
def displayStudentForm():
    return render_template('studentForm.html')

@app.route('/addStudentOrganization', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organization from form.
    studentName = request.form['name']
    studentOrg = request.form['organization']

    if studentName=="" or studentOrg=="":
        pass
    else:
        # Append this value to studentOrganizationDetails
        studentOrganizationDetails[studentName] = studentOrg

    # Display studentDetails.html with all students and organizations
    return render_template('studentDetails.html', studentOrganizationDetails=studentOrganizationDetails)
