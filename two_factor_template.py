#!/usr/bin/python3

import getpass
import smtplib
import random

from email.mime.text import MIMEText

# Some test users
users_passwords = {
    "user01" : "user01",
    "demo" : "demo",
    "user02" : 12345678,
}

users_database = {
    
}

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    print("TODO TODO TODO")
        
    
def send_verification_email(login_user_name: str, verification_code: int):
    subject = "ACME Account Verification"
    body = "Hello {},\n\n" \
    "We are delighted you have joined our web site. Before start using our \n" \
    "wonderful products and services we must verify your account.\n" \
    "Please, enter the following verificaction code in the login screen:\n" \
    "\n       {}\n\n" \
    "and follow any further instruction on the screen.\n" \
    "\n" \
    "If you have any questions or need help, please, do not hesitate to contact us.\n" \
    "Many thanks,\n" \
    "The ACME team\n".format(login_user_name, verification_code)

    # GMX
    sender = "world_of_work@gmx.com"
    recipients = ["YOUR@EMAIL.COM"]
    password = "GmxSecret0"

    send_email(subject, body, sender, recipients, password)
    
def do_login():    
    # Read login; username and password
    print(" ")
    print("ACME. Welcome to the Coyote e-commerce site")
    print(" ")

    # Read the user name
    while True:
        user_name = input("Username [%s]: " % getpass.getuser())
        if not user_name:
            user_name = getpass.getuser()        

        if user_name not in users_passwords:
            print("Incorrect user name. Please, enter a valid user name")
        else:
            break
        
        
    # Read the password
    while True:
        user_password = getpass.getpass() 
        while not user_password:
            print("Please, enter a password")
            user_password = getpass.getpass()
        
        if user_password != users_passwords[user_name]:
            print("Incorrect password. Please, try again")
        else:
            break
          
    # TODO: Clear screen
    
    if user_name not in users_database:
        users_database[user_name] = []
    
    list_user_codes = users_database[user_name]
    
    # Generate a random number
    print("TODO")

    # Check if the code is repeated
    print("TODO")
            
    # Save the code
    print("TODO")
    
    # Send email with the code
    print("TODO")
    
    # Read code
    while True:
        read_verification_code = input("Verification code: ")
        try:
            read_verification_code = int(read_verification_code)
        except:
            read_verification_code = 0
    
        # While code is not correct, keep reading
        if verification_code != read_verification_code:
            print("Incorrect verification code. Please try again")
        else:
            break
            
    print(" ")
    print("Verification code is correct. Access granted")
    print(" ")
    
    
if __name__ == "__main__":
    for i in range(3):
        do_login()
    
    
