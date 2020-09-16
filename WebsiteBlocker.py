from datetime import datetime
# This is only for WINDOW USERS
host_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

website_list = []

websites = input('Enter you website name')
website_list.append(websites)

# Time frame during which we want to block our website
start_date = datetime(2020,2,3)
end_date = datetime(2021,2,2)
today_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

while True:
    if start_date<=today_date<=end_date:
        with open(host_path,'r') as file:
            content = file.read()
            for site in content:
                if site in website_list:
                    pass
                else:
                    file.write(redirect+' '+site+"\n")
        print('Your site is blocked')
        break
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)

            file.truncate()
        print('Your site is unblocked')
        break
