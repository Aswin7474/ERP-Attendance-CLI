import os
import sys
from dotenv import load_dotenv, set_key
from helpers import only_att, periods, enter_to_exit, check_if_int, cookie_dump

load_dotenv(override=True)

if not os.path.exists('.env'):
    open('.env', "w").close()  # Create empty .env file
    print(".env file created.")

user = os.getenv("user")
if user is None:
    newUsername = input('Enter username: ')
    set_key('.env', 'user', newUsername)
    user = newUsername

passw = os.getenv("pass")
if passw is None:
    newPassword = input("Enter password: ")
    set_key('.env', 'pass', newPassword)
    passw = newPassword

sessionid = os.getenv("sessionid")
if sessionid is None:
    sessionid = cookie_dump(user, passw)
    if sessionid is None:
        print("Cannot automate sessionid setup.")
        input("Press enter to exit.")
        sys.exit()

choice = input("1.Check Attendance\n2.Check Attendance by class\n3.Set Username and Password.\n4.Exit\n")

if not check_if_int(choice):
    enter_to_exit()
    sys.exit()

choice = int(choice)


if choice == 1:
    only_att(sessionid, user, passw)
elif choice == 2:
    subject = input("1.Counselling.\n2.Operating Systems.\n3.Software Construction.\n4.User Interface Design.\n5.Softskills.\n6.DT.\n7.Library.\n8.Probability Statistics and Simulation.\n9.NPTEL.\n")

    if not check_if_int(subject):
        enter_to_exit()
        sys.exit()

    subject = int(subject)

    if subject not in range(1, 10):
        enter_to_exit()
        sys.exit()

    periods(int(subject), sessionid, user, passw)
elif choice == 3:
    from dotenv import set_key
    set_key('.env', "user", input("Enter username: "))
    set_key('.env', "pass", input("Enter password: "))
elif choice == 4:
    sys.exit()
else:
    enter_to_exit()
    sys.exit()

if input("Press Enter to exit."):
    sys.exit()




