import os
import sys
from dotenv import load_dotenv
from helpers import only_att, periods, enter_to_exit, check_if_int

load_dotenv()
sessionid = os.getenv("sessionid")
if sessionid is None:
    print("Setup SessionID in env file before use.")
    input()
    sys.exit()

choice = input("1.Check Attendance\n2.Check Attendance by class\n3.Exit\n")

if not check_if_int(choice):
    enter_to_exit()
    sys.exit()

choice = int(choice)


if choice == 1:
    only_att(sessionid)
elif choice == 2:
    subject = input("1.Counselling.\n2.Operating Systems.\n3.Software Construction.\n4.User Interface Design.\n5.Softskills.\n6.Library.\n7.Probability Statistics and Simulation.\n8.NPTEL.\n")

    if not check_if_int(subject):
        enter_to_exit()
        sys.exit()

    subject = int(subject)

    if subject not in range(1, 9):
        enter_to_exit()
        sys.exit()

    
    periods(int(subject), sessionid)
elif choice == 3:
    sys.exit()
else:
    enter_to_exit()
    sys.exit()


a = input("Press Enter to exit.")
if a:
    sys.exit()




