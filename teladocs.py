import pyfiglet
from termcolor import colored
import sqlite3
import uuid
import time
import datetime



result = pyfiglet.figlet_format("Teladocs", width=180)
welcome_message = """
****************************************************

Welcome to Teladocs Telemedicine Monitoring System. Let us connect you to the best medical practitioners!

****************************************************
"""

print(colored(result, "blue"))
print(colored(welcome_message, "blue"))

def display_opening_menu():
    menu = """
    Are you a new user? Register here! If not, login to your account.
    1. Login
    2. Register
    3. Exit
    """
    print(colored(menu, "blue"))

def display_doctor_menu():
    menu = """
    What would you like to do?
    1. View patient appointments and attend to patient through video call
    2. Exit
     
    """
    print(colored(menu, "blue"))
    
def display_patient_menu():
    menu = """
    What would you like to do?
    1. Book an appointment
    2. Exit
    """
    print(colored(menu, "blue"))
    
def display_registration_menu():
    menu = """
    Please select the type of registration you would like to do:
    1. Register as a doctor
    2. Register as a patient
    3. Exit
    """
    print(colored(menu, "blue"))

def display_login_menu():
    menu = """
    Please select the type of login you would like to do:
    1. Login as a doctor
    2. Login as a patient
    3. Exit
    """
    print(colored(menu, "blue"))
    
def login_as_doctor():
    guesses = 0
    limit = 3
    loggedIn = False
    while guesses < limit and not loggedIn:
        print("Please enter your credentials to login as a doctor")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        conn = sqlite3.connect("teladocs.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctor WHERE username = ? AND password_ = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            loggedIn = True
            return user
        else:
            guesses += 1
            print("Wrong credentials. Try again.")

def login_as_patient():
    guesses = 0
    limit = 3
    loggedIn = False
    while guesses < limit and not loggedIn:
        print("Please enter your credentials to login as a patient")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        conn = sqlite3.connect("teladocs.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patient WHERE username = ? AND password_ = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            loggedIn = True
            return user
        else:
            guesses += 1
            print("Wrong credentials. Try again.")
        

def register_as_patient():
    print("Please enter your details to register as a patient")
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
        cursor.execute("INSERT INTO Patient VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1, fullname, email, username, gender, dob, phone, residence, password_, age, bloodgroup))
        conn.commit()
        conn.close()
        print("Registration successful!")
    else:
        print("Passwords do not match!")

def register_as_doctor():
    print("Please enter your details to register as a doctor")
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
        cursor.execute("INSERT INTO Doctor VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1, name, username, password, speciality, start_time, age, gender, end_time, phone, email))   
        conn.commit()
        conn.close()
        print("Registration successful!")
    else:
        print("Passwords do not match!")
    

def book_appointment(user):
    print("Please enter the time you would like to have your appointment")
    start_time = input("Enter your start time: ")
    end_time = input("Enter your end time: ")
    specialist = input("Enter the specialist you would like to see: ")
    conn = sqlite3.connect("teladocs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctor WHERE start_time = ? AND end_time = ?", (start_time, end_time))
    doctors = cursor.fetchall()
    conn.close()
    for doctor in doctors:
        if doctor[4] == specialist:
            conn = sqlite3.connect("teladocs.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Appointment VALUES (?,?,?,?,?)", (1, start_time, end_time, user[1] ,doctor[1]))
            conn.close()
            print("Appointment booked successfully!")
            break
        
def view_appointments(doctor):
    conn = sqlite3.connect("teladocs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointment WHERE doctor = ?", (doctor[1],))
    appointments = cursor.fetchall()
    conn.close()
    return appointments
        
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
                                        book_appointment(user)
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
                        login_as_doctor()
                    elif option == 2:
                        register_as_patient()
                        # set timer to 5 seconds
                        timer = 5
                        while timer > 0:
                            print(timer)
                            timer -= 1
                            time.sleep(1)
                        login_as_patient()
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