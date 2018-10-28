import time
from datetime import datetime as dt
hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

#change directory to whenever websites text doc is saved to
with open("C:\\Users\\Pete\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\app3\\websites.txt") as w:
    global website_list
    website_list= w.readlines()
website_list = [x.strip() for x in website_list]

#should block sites between 9am and 5pm
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < (dt(dt.now().year,dt.now().month,dt.now().day,17)):
        print("Working Hard or hardly working...?")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Break time...")
    time.sleep(5)
