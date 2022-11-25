'''
DIGITAL TELADOCS STATION IS A PLATFORM AIMED AT MAKING MEDICAL SERVICES MORE ACCESSIBLE 
TO ALL.IT SOLVES ISSUES LIKE HIGH TRANSPORT COSTS TO HOSPITALS, LONG QUEUES IN HOSPITALS BY USE
OF A DIGITAL MONITORING SYSTEM HENCE EASENING THE COMMUNICATION BETWEEN THE DOCTOR AND THE PATIENT
IF THE CONDITIONS OF THE PATIENT WORSENS IN RELATION TO THE ENVIRONMENT E.G BECAUSE OF HIGH ENVIRONMENTAL TEMPERATURE
~Contains a login system for both the doctor and the patient
~The patient is able to book an appointment with the doctor
~The doctor is also able to view the appointments and hence attend to them.
'''

import pyfiglet # a module which converts text to large ASCII texts
from termcolor import colored # alters colour of text
import sqlite3 # module that enhances connection to sqlite database
#import uuid # make a UUID based on the host ID and current time
# universally unique indentifiers(Immutable \uuid)
import time 
import datetime #converts time to hours and minutes from string
import random #generates random numbers


# seed a random number to generate a unique appointment ID
# appointmentID = random.randint(1000, 999)



result = pyfiglet.figlet_format(" Station Teladocs", width=180)
welcome_message = """
****************************************************

Welcome to Digital Teladocs Station,the best Telemedicine Monitoring System. 
Let us connect you to the best medical practitioners!

****************************************************
"""
#alters the colour of text
print(colored(result, "blue"))
print(colored(welcome_message, "blue"))
# function 
def display_opening_menu():
    menu = """
    Are you a new user? Register here! If not, login to your account.
    1. Login
    2. Register
    3. Exit
    """
    print(colored(menu, "blue"))
#when a user logins as a doctor
def display_doctor_menu():
    menu = """
    What would you like to do?
    1. View patient appointments and attend to patient through video call
    2. Exit
     
    """
    print(colored(menu, "blue"))
#when a user logins as a patient   
def display_patient_menu():
    menu = """
    What would you like to do?
    1. Book an appointment. If already booked, check your email for meeting link.
    2. Exit
    """
    print(colored(menu, "blue"))
  # registration function  
def display_registration_menu():
    menu = """
    Please select the type of registration you would like to do:
    1. Register as a doctor
    2. Register as a patient
    3. Exit
    """
    print(colored(menu, "blue"))
#a login function either a s a doctor or patient
def display_login_menu():
    menu = """
    Please select the type of login you would like to do:
    1. Login as a doctor
    2. Login as a patient
    3. Exit
    """
    print(colored(menu, "blue"))
   #login as a doctor 
def login_as_doctor():
    guesses = 0
    limit = 3
    loggedIn = False
    while guesses < limit and not loggedIn: #hasn't surpassed the limit of guesses and the login details match with the original details
        print("Please enter your credentials to login as a doctor")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        conn = sqlite3.connect("teladocs.db") #connect to the SQlite database file (teladocs.db)
        cursor = conn.cursor()#Shows result from a query on the SQLiteDatabase 
        cursor.execute("SELECT * FROM doctor WHERE username = ? AND password_ = ?", (username, password))
        user = cursor.fetchone()# retrieves only  first row from the Doctor table
        conn.close()#closes the connection to the database file
        if user:#authentication 
            loggedIn = True
            return user
        else:
            guesses += 1
            print("Wrong credentials. Try again.")
#login as a patient into your account
def login_as_patient():
    guesses = 0
    limit = 3
    loggedIn = False
    while guesses < limit and not loggedIn:#hasn't surpassed the limit of guesses and the login details match with the original details
        print("Please enter your credentials to login as a patient")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        conn = sqlite3.connect("teladocs.db")
        cursor = conn.cursor()#a cursor is a class that allows python code to execute SQLite command in a database
        cursor.execute("SELECT * FROM patient WHERE username = ? AND password_ = ?", (username, password))
        user = cursor.fetchone()#fetches only the first row from the Patient table
        conn.close()
        if user:
            loggedIn = True
            return user
        else:
            guesses += 1
            print("Wrong credentials. Try again.")
        

def register_as_patient():
    print("Please enter your details to register as a patient")
    PatientID = input("Enter your PatientID; The First 2 letters of your name: ")
    username = input("Enter your username: ")
    password_ = input("Enter your password: ")
    confirmpassword = input("Confirm your password: ")
    fullname = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    email = input("Enter your email: ")
    dob = input("Enter your date of birth: ")
    phone = input("Enter your phone number: ")
    residence = input("Enter your residence: ")
    bloodgroup = input("Enter your blood group: ")
    if password_ == confirmpassword:
        conn = sqlite3.connect("teladocs.db")
        cursor = conn.cursor()
        # patient_id = int(uuid.uuid4())
        cursor.execute("INSERT INTO Patient VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (PatientID, fullname, email, username, gender, dob, phone, residence, password_, age, bloodgroup))
        conn.commit()#saves all the modifications made since the first commit
        conn.close()
        print("Registration successful!")
    else:
        print("Passwords do not match!")
#doctor profile details which are saved in the doctor table in the database
def register_as_doctor():
    print("Please enter your details to register as a doctor")
    DoctorID = input("Enter your DoctorID; The First 2 letters of your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirmpassword = input("Confirm your password: ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    speciality = input("Enter your speciality: ")
    start_time = input("Enter your start time: ")
    end_time = input("Enter your end time: ")
    
    if password == confirmpassword:
        conn = sqlite3.connect("teladocs.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Doctor VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (DoctorID, name, username, password, speciality, start_time, age, gender, end_time, phone, email))   
        conn.commit()#saves all the modifications made since the first commit
        conn.close()
        print("Registration successful!")
    else:
        print("Passwords do not match!")
    
#function to book an appointment specifying the date and time
def book_appointment(user):
    AppointmentID = input("Enter your AppointmentID; The initials of your name : ")
    print("Please enter the time you would like to have your appointment")
    start_time = input("Enter your start time: ")
    end_time = input("Enter your end time: ")
    specialist = input("Enter the specialist you would like to see: ")
    conn = sqlite3.connect("teladocs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Doctor WHERE start_time = ? AND end_time = ?", (start_time, end_time))
    doctors = cursor.fetchall()#fetches all the rows from the Doctor table on start time and end time
    conn.close()
    print("Connecting you to a doctor...")
    #print(doctors)
    for doctor in doctors:
        if doctor[4] == specialist:#fetches the specialist from the Doctor table
            conn = sqlite3.connect("teladocs.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Appointment VALUES (?,?,?,?,?)", (AppointmentID, start_time, end_time, user[1] ,doctor[1]))#inserts all the details including the docotr assigned to patient into the Appointment table
            conn.close()
            print("Appointment booked successfully!")
            break
#function to view all the appointments booked by patients to a specific doctor
def view_appointments(doctor):
    conn = sqlite3.connect("teladocs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointment WHERE doctors_name = ?", (doctor[1],))
    appointments = cursor.fetchall()#fetches all the rows from the Appointment table so that the doctor can view them
    conn.close()
    return appointments

#function that enables the doctor access the emails of the patients to send them the links to the video call    
def attend_to_patient(appointment):
    patient_name = appointment[3]
    conn = sqlite3.connect("teladocs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM Patient WHERE fullname = ?", (patient_name,))
    email = cursor.fetchone()
    conn.close()
    print("Sending email to patient with address: ", email[0])
    
def mark_attended(appointment):
    conn = sqlite3.connect("teladocs.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Appointment WHERE patient = ?", (appointment[3],))
    conn.commit()
    conn.close()
    print("Appointment marked as attended!")
    
    
while True:
    try:
        display_opening_menu()
        option = int(input("Enter your option: "))
        if option == 1:
            while True:
                try:
                    display_login_menu()
                    option = int(input("Enter your option: "))
                    if option == 1:
                        user = login_as_doctor()
                        print(user)
                        if user:
                            print("Login successful!")
                            while True:
                                try:
                                    display_doctor_menu()
                                    option = int(input("Enter your option: "))
                                    if option == 1:
                                        appointments = view_appointments(user)
                                        print(appointments)
                                        for appointment in appointments:
                                            attend_to_patient(appointment)
                                            start = datetime.datetime.strptime(appointment[1], "%H:%M")
                                            end = datetime.datetime.strptime(appointment[2], "%H:%M")
                                            duration = end - start
                                            while duration > datetime.timedelta(0):
                                                print("You have ", duration, "left to attend to patient")
                                                time.sleep(1)
                                                duration = duration - datetime.timedelta(seconds=1)
                                            mark_attended(appointment)
                                    elif option == 2:
                                        print("Exiting")
                                        break
                                    else:
                                        print("Invalid option!")
                                except ValueError:
                                    print("Invalid option!")
                        else:
                            print("Invalid credentials!")
                    elif option == 2:
                        user = login_as_patient()
                        print(user)
                        if user:
                            print("Login successful!")
                            while True:
                                try:
                                    display_patient_menu()
                                    option = int(input("Enter your option: "))
                                    if option == 1:
                                        print("Booking appointment")
                                        book_appointment(user)
                                        print("Check your email for the link to the video call")
                                        print("Have a lovely Time.")
                                    elif option == 2:
                                        print("Exiting")
                                        break
                                    else:
                                        print("Invalid option!")
                                except ValueError:
                                    print("Invalid option!")
                    elif option == 3:
                        print("Exiting...")
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid option. Please try again.")
        elif option == 2:
            while True:
                try:
                    display_registration_menu()
                    option = int(input("Enter your option: "))
                    if option == 1:
                        register_as_doctor()
                        # set timer to 5 seconds
                        timer = 5
                        while timer > 0:
                            print(timer)
                            timer -= 1
                            time.sleep(1)
                        user = login_as_doctor()
                        print(user)
                        if user:
                            print("Login successful!")
                            while True:
                                try:
                                    display_doctor_menu()
                                    option = int(input("Enter your option: "))
                                    if option == 1:
                                        appointments = view_appointments(user)
                                        print(appointments)
                                        for appointment in appointments:
                                            attend_to_patient(appointment)
                                            start = datetime.datetime.strptime(appointment[1], "%H:%M")
                                            end = datetime.datetime.strptime(appointment[2], "%H:%M")
                                            duration = end - start
                                            while duration > datetime.timedelta(0):
                                                print("You have ", duration, "left to attend to patient")
                                                time.sleep(1)
                                                duration = duration - datetime.timedelta(seconds=1)
                                            mark_attended(appointment)
                                    elif option == 2:
                                        print("Exiting")
                                        break
                                    else:
                                        print("Invalid option!")
                                except ValueError:
                                    print("Invalid option!")
                        else:
                            print("Invalid credentials!")
                        
                    elif option == 2:
                        register_as_patient()
                        # set timer to 5 seconds
                        timer = 5
                        while timer > 0:
                            print(timer)
                            timer -= 1
                            time.sleep(1)
                            
                        user=login_as_patient()  
                        while True:
                            try:
                                display_patient_menu()
                                option = int(input("Enter your option: "))
                                if option == 1:
                                    print("Booking appointment")
                                    book_appointment(user)
                                    print("Check your email for the link to the video call")
                                    continue
                                elif option == 2:
                                    print("Exiting")
                                    break
                                else:
                                    print("Invalid option!")
                            except ValueError:
                                print("Invalid option!")
                        
                        #book_appointment(user)
                    elif option == 3:
                        print("Exiting...")
                        break
                        
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid option. Please try again.")
                    
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid option. Please try again.")