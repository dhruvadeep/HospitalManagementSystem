#Importing all the packages
import math
import json
import statistics
import time


# Asking user to select for modes
print("===Welcome to Hospital Management===")
print("Select your login option.")
print("★ Admin")
print("★ Doctor")
print("★ Patient")
print("====================================")

# Login Function
work = 0
while work==0:
    _login_choice = input("Enter your choice: ")
    print("")
    if _login_choice in ["admin", "ADMIN", "Admin", "Administrator", "Super"]:
        auth = "ADMIN"
        print("Login as Admin")
        password = input("Enter password: ")
        work = 1
        # print("Hello1") #Debugging Purpose
    elif _login_choice in ["doctor", "DOCTOR", "DC", "expert", "physician", "medic"]:
        auth = "DOCTOR"
        print("Login as Doctor.")
        password = input("Enter password: ")
        work = 1
        # print("Hello2") #Debugging Purpose
    elif _login_choice:
        auth = "PATIENTS"
        print("Login as Patient.")
        password = input("Enter password: ")
        work = 1
        # print("Hello3") #Debugging Purpose
    else:
        work = 0
        print("No input")

#adding a timer to counter dos
print("Trying to connect to server...")
time.sleep(3)
# Password check
with open('auth.system.json', 'r') as authDetails:
    json_data_auth = json.load(authDetails)
# print(json_data_auth) #Debugging
authentication = str(auth) #For Usage

#Testing
for auth_details in json_data_auth:
  val = auth_details.get('type')
  if val == authentication:
    user_pass = str(password)
    pass_ = str(auth_details.get('pass'))
    if user_pass == pass_:
      print('SuccessFul login.')
      isValid = 1 #for later part
      break
    else:
      print('Incorrect Password')
      isValid = 0 #for later part
      break
  else:
    continue


# Checking if login was successful
if isValid == 1:
	success = 1
elif isValid == 0:
	# print("Apple")
	exit()
else:
	print("Something went wrong...\nTerminating the connection...")
	exit()


# Main code and admin panel
# Admin panel first and usage
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

if (success==1) & (authentication=="ADMIN"):
	print("\n\n\n")
	print("====Welcome to ADMIN Dashboard====")
	print("Current Login: ADMIN")
	print("Current Time:", current_time, "\n")
	print("Select your prefered choice.")
	print("1. View Available Hospitals")
	print("2. View Available Doctors")
	print("3. View Patient Details")

if (success==1) & (authentication=="DOCTOR"):
	print("\n\n\n")
	print("====Welcome to DOCTOR Dashboard====")
	print("Current Login: DOCTOR")
	print("Current Time:", current_time, "\n")
	print("Select your prefered choice.")
	print("1. View Available Hospitals")
	print("2. View Patients List")
	print("3. View Appointment Details")

if (success==1) & (authentication=="PATIENTS"):
	print("\n\n\n")
	print("====Welcome to PATIENT Dashboard====")
	print("Current Login: PATIENT")
	print("Current Time:", current_time, "\n")
	print("Select your prefered choice.")
	print("1. View Available Hospitals")
	print("2. View Available Doctors")
	print("3. Book an appointment")
print("=====================================")
choice_assign = int(input("Enter your prefered choice: "))
if choice_assign in [1,2,3]:
	choice_assign = choice_assign
else:
	print("Invalid Choice.")
	print("Exiting the program.")
	time.sleep(2)
	exit()

# Available options
if (authentication == "ADMIN"):
	if choice_assign == 1:
		# Hospital DETAILS
		print(1)
		with open('hospitalDetails.json', 'r') as hospitalDetails:
    			json_data_hospital = json.load(hospitalDetails)
		for item in json_data_hospital:	
    	 		print(item["Hospital"])
	if choice_assign == 2:
		print(2)
		print("Coming soon...")
	if choice_assign == 3:
		print(3)
		with open('PatientDetails/Patients.json', 'r') as patientDetails:
    			json_data_patient = json.load(patientDetails)
		for item in json_data_patient:	
    	 		print(item["SLNo"], item["First_Name"], item["Last_Name"], " ",item["Age"], " ", item["PhoneNo"], " ", item["Email"])
# Debug
print("Thm")






# if (json_data_auth["type"]=="ADMIN") and (json_data_auth["pass"]==password):
#     print("Hello")
# else:
#     print("Failed to login")



# 12




# # with open('hospitalDetails.json', 'r') as f:
# #     json_data = json.load(f)

# for item in json_data_auth:
#     print(item["pass"])
