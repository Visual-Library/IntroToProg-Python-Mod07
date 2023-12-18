# ------------------------------------------------------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Ronald Mursewick, 11/27/2023, Create script to accept student name and print result)
#
#   <Ronald Mursewick>,<11/27/2023>, Created Script
# ------------------------------------------------------------------------------------------------- #
#
#   Define the method libraries we will use
#
import os
import os.path

# import the CSV libraries for easier manipulation of our csv file
import csv
# import pandas to help use 2 dimensional arrays easily
import pandas as pd
import sys
import json

# We will define our initial constants for the program
# specifically defining the datatype to be used for each variable
# we will capitalize the constant names as a programming best practice as a
# visual indication that these declarations will remain constant throughout the program operation
#

COURSE_NAME         : str = "Python 100"
COURSE_PRICE        : float = 999.98
STATE_TAX           : float = .09
TOTAL_PRICE         : float = (COURSE_PRICE
                      + (COURSE_PRICE * STATE_TAX))
FILE_NAME           : str = "Enrollments.json"
FILE_HEADER         : str = "FirstName,LastName,CourseName,CoursePrice,CourseCost\n"
MENU                : str = \
"---- Course Registration Program ----\n" +\
"  Select from the following menu:\n" +\
"    1. Register a Student for a Course\n" +\
"    2. Show current data\n" +\
"    3. Save data to a file\n" +\
"    4. Exit the program\n" +\
"    -----------------------------------------"

# Now we will define the variables and set their initial values that we will use in our program
# We set the initial values to "" which is an ASCII Null, which differs form setting the value to " "
# which is an ASCII value 32 (Space)

student_first_name  : str = ""
student_last_name   : str = ""
course_name         : str = ""
menu_choice         : str = ""

# this is a list in dictionary format
student_list        : list[dict[str]] = []

student_count       : int = 0
total_student_count : int = 0
student_data        : str = ""
file_check          : bool = False
student_registered  : bool = False
file_obj                     = None

#
# Create our class definition of person
# Then create the constructors to for the data structure

class Person:

    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Student(Person):  # Add a class name to indicate explicit inheritance.

    def __init__(self, first_name: str = '', last_name: str = '', class_name: str = ''):
        super().__init__(first_name=first_name, last_name=last_name)

        self.course_name = course_name
        self.course_price = COURSE_PRICE
        self.course_cost = TOTAL_PRICE

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course_name},{self.course_price},{self.course_cost}"

#
# Set up our setters and getters for student first Name and student last name
@property
def first_name(self):
        return self.__first_name.title()

@first_name.setter
def first_name(self, value: str):
        #
        # Verify that the first name is alphabetic

        if value.isalpha() or value == "":
            self.__first_name = value.capitalize()
        else:
            raise ValueError("The first name should not contain numbers.")

@property
def last_name(self):
        return self.__last_name.title()  # formatting code

@last_name.setter
def last_name(self, value: str):
        #
        # verify that the last name if alphabetic

        if value.isalpha() or value == "":
            self.__last_name = value.capitalize()
        else:
            raise ValueError("The last name should not contain numbers.")





# Import the os libraries
# specifically the .path method
# we will use this method to determine if the enrollments.csv file already exists.
# if the file exists we will add new students to the existing file
# if the file does not already exist, we will create it an add students to the file


#
# Create the dataframe with the header row

students_pd = pd.DataFrame(columns=("FirstName", "LastName", "CourseName", "CoursePrice", "CourseCost"))

#
# Create a function to print out the menu
# this menu directs the function we are providing for the operator
# output ment is an example of a function that we call.
# we pass a variable and expect nothing to be returned from the function

@staticmethod
def  output_menu (menu: str):
    print("\n", MENU, "\n")
    return

#
# this function is our request to the operator for what operation they wish to perform
# we dont need to pass any value or parameter but expect the value of number of the operation
# they want to perform in return.

def input_menu_choice (ps: str):
    menu_choice = input(ps)
    return menu_choice

#
# define a function to print out the students that the operator
# has enrolled in the current session

def print_student_data():
    print("\nThis is the data from the list: \n")
    print (student_list)
    return

# Print some blank spaces to separate the script execution for the operator input request
# Lets ask the operator for the students first name, print what we are asking the operator for
print("\n", "\n")

# Lets see if our student enrollment file already exists
file_check = os.path.isfile(FILE_NAME)

# if the file doesn't exist, we will create a new file for our student enrollment
# once the file is open we will write the column header records
# open the file for appending

if file_check is False:
    file_obj = open(FILE_NAME, "a+")


while True:
    # Present the operator with a list of operations they can perform
    # Call the output_menu function to print out the menu of choices to the operator

    output_menu (MENU)

    #
    # remove any extra characters before or after the input value with the strip method
    # Call the input_menu_choice function to accept console input from the operator

    prompt_string = "Enter your menu Selection: "
    #
    # call our function to as the operator for the menu choice.

    menu_choice = input_menu_choice(prompt_string)
    menu_choice = menu_choice.strip()

    if menu_choice == "1":
        student_count = student_count + 1
        prompt_string = "Enter the students first name: : "
        #
        # call our function to prompt for data input
        student_first_name = input_menu_choice(prompt_string)

        #
        # confirm the student first name is alphabetic other wise go back and ask again

        try:
            if not student_first_name.isalpha():
                raise ValueError("The first name must be alphabetic. ")
        except ValueError as e:
                print("\n", e, "\n")
                continue

        student_first_name = student_first_name.capitalize()

        prompt_string = "Enter the students last name: : "
        student_last_name = input_menu_choice(prompt_string)

        #
        # confirm the student last name is alphabetic other wise go back and ask again

        try:
            if not student_last_name.isalpha():
                raise ValueError("The students last name must be alphabetic. ")
        except ValueError as e:
                print("\n", e, "\n")
                continue

        student_last_name = student_last_name.capitalize()
        student_data = ""
        #student_registered = students_pd.isin([student_last_name]).any().any()
        #if student_registered:
        #    print (("Student: ", student_first_name, student_last_name, "is already registered."))
        #    continue
        #
        # set up the data in the correct form for appending to the DataFrame

        student_data = {'FirstName': student_first_name,\
                        'LastName': student_last_name,\
                        'CourseName': COURSE_NAME,\
                        'CoursePrice': COURSE_PRICE,\
                        'CourseCost': round(TOTAL_PRICE, 2)}

        #
        # append the current student data to the list

        student_list.append(student_data)

        #
        # we will append the newly added student to the bottom of the dataframe
        # this DataFrame can extend indefinitely

        students_pd.loc[len(students_pd)] = student_data


    if menu_choice == "2":
        print ("\n")
        if student_count < 1:
            #
            # if the operator has not entered any data we will send them
            # back to the prompt so they can enter some data
            print ("No students have been registered yet", "\n")
            continue
            #
            # if they have entered data print it out for the operator to confirm the entries
        print (" This is the data in the dataframe ")
        print ("\n", "Total Students registered so far is: ", student_count, "\n")
        print (students_pd)
        print ("\n\n")

        #
        # print put the student that is in the list also

        #
        # use our function call to print out the data from the list
        px = print_student_data()

    if menu_choice == "3":
        print("\n")
        #
        # if the student count is 0, there is no data to write to the file.
        if student_count < 1:
            print("No students have been registered yet", "\n")
            continue
        #
        # if we have a student entered then we will write the entry to our .csv file
        # then we will print a list of every that is registered
        student_last_name = student_last_name.strip()
        COURSE_NAME = COURSE_NAME.strip()

        #
        # now we will append the newly added students to the .json file

        students_pd.to_json(FILE_NAME, mode="a", index=False, lines=True, orient="records")

        #
        # we will also write out the student list file we created as well

        file_obj = open("Enrollments2.json", "a+")
        json.dump(student_list, file_obj)
        file_obj.close()

        #
        # we will read thru the rows and show the operator all of the students that are registered.
        #
        # reassign $stdout to a text file and write our enrollment to a file for review

        print ("\n", "\n", "The student data has been written to Assignment07.txt for your review", "\n","\n")
        sys.stdout = open("Assignment07.txt", "w")

        with open('Enrollments.json') as f:
            for line in f:
                total_student_count = total_student_count + 1
                print ("Student: ", line)

        print ("Total students registered for the class is:", total_student_count, "\n")

        #
        # reassign $stdout to the console so we can interact on the console terminal again
        sys.stdout = sys.__stdout__

        #
        # reset the student count for another student
        student_count = 0

    if menu_choice == "4" or "":
        break

