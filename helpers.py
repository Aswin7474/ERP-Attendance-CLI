import json
import requests
import pandas as pd
from tabulate import tabulate

def only_att(sessionid):
    url = "https://erp.rajalakshmi.org/StudeHome.aspx/ShowAttendance"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://erp.rajalakshmi.org",
        "Referer": "https://erp.rajalakshmi.org/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }

    my_cookies = {
        "ASP.NET_SessionId": sessionid
    }

    try:
        # POST request using the cookies parameter
        response = requests.post(url, headers=headers, cookies=my_cookies, json={})  # No payload needed
        response.raise_for_status()
        json_data = response.json()
        attendance_list = json_data["d"]["AttendList"]
        df = pd.DataFrame(attendance_list)

        # Renaming columns for better readability
        df.columns = ["Course Name", "Attendance", "Attendance Percentage", "Course Code", "Section Name"]

        # Displaying the table in terminal format
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def periods(sub_num, sessionid):
    from bs4 import BeautifulSoup
    subjects = ['counselling', 'os', 'sc', 'uid', 'softskills', 'dt', 'library', 'pss', 'nptel']

    with open('options.json', 'r') as file:
        options = json.load(file)

    url = "https://erp.rajalakshmi.org/Academic/iitmsPFkXjz+EbtRodaXHXaPVt3dlW3oTGB+3i1YZ7alodHeRzGm9eTr2C53AU6tMBXuOXVbvNfePRUcHp4rLz3edhg==?pageno=76"
    headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://erp.rajalakshmi.org",
            "Referer": "https://erp.rajalakshmi.org/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "X-MicrosoftAjax": "Delta=true",
            "X-Requested-With": "XMLHttpRequest",
        }

    my_cookies = {
        "ASP.NET_SessionId": sessionid
        }
    
    session = requests.Session()
    session.cookies.update(my_cookies)
    response = requests.post(url, headers=headers, data=options.get(subjects[sub_num - 1]), cookies=my_cookies)

    soup = BeautifulSoup(response.text, "html.parser")

    class_elements = soup.select('.table-responsive')
    if class_elements:
        table = class_elements[-1]
        rows = table.find_all('tr')
        parsed_data = []
        for row in rows[1:]:
            columns = row.find_all('td')
            column_texts = [col.get_text(strip=True) for col in columns]
            parsed_data.append(column_texts)

    df_html = pd.DataFrame(parsed_data, columns=["Period No", "Date", "Slot Time", "Present/Absent"])

    print(tabulate(df_html, headers='keys', tablefmt='grid', showindex=False))


def enter_to_exit():
    print("Invalid option.")
    a = input("Press Enter to exit.")


def check_if_int(choice):
    try:
        int(choice)
        return True
    except ValueError:
        return False
