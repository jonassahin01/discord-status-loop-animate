
import requests 
from time import sleep
from colorama import init,Fore
import json
init(autoreset=True)
intro = Fore.GREEN + """
 ___   ___   ___   ___   ___   ___   ___         ___   ___   ___   ___         ___  
  | |   |   |     |     |   | |   |   | |       |       |   |   |   |   |   | |     
  + |   +    -+-  |     |   | |-+-    + |        -+-    +   |-+-|   +   |   |  -+-  
  | |   |       | |     |   | |  \    | |           |   |   |   |   |   |   |     | 
 ---   ---   ---   ---   ---         ---         ---                     ---   ---  
                                                                                    
"""

file = open("config.json", "r", encoding='utf-8')
config = json.load(file)
    

        
print(intro)    

#menu
print(Fore.GREEN + "[1]Loop")
print(Fore.GREEN + "[2]Animation")
print(Fore.YELLOW + "[3]Config")
print(Fore.RED + "[4]Exit\n")

token = config["token"]
headers = {
    'accept':'*/*',
    'authorization': token,
    'content-type':'application/json',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.18 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
    'x-super-properties':'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkRpc2NvcmQgQ2xpZW50IiwicmVsZWFzZV9jaGFubmVsIjoicHRiIiwiY2xpZW50X3ZlcnNpb24iOiIwLjAuMTgiLCJvc192ZXJzaW9uIjoiNS41LjctMS1NQU5KQVJPIiwib3NfYXJjaCI6Ing2NCIsIndpbmRvd19tYW5hZ2VyIjoiS0RFLHVua25vd24iLCJkaXN0cm8iOiJcIk1hbmphcm8gTGludXhcIiIsImNsaWVudF9idWlsZF9udW1iZXIiOjU1NzEyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
}

#var
lst = list(config["list"])
status = config["status"]
emoji = config["emoji"]
time = int(config["time"])


menuvar = input("enter: ")

#menu func
class menu():  
    if menuvar == "1":       
        while True:                      
            for message in lst:
                data = {'custom_status': {'text': message,'emoji_name':emoji}} 
                requests.patch('https://ptb.discordapp.com/api/v8/users/@me/settings', headers=headers, json=data)
                sleep(time)
    elif menuvar == "2":
        while True:
            for x in range(0, len(status)+1):
                data = {'custom_status': {'text': status[:x],'emoji_name':emoji}}
                requests.patch('https://ptb.discordapp.com/api/v8/users/@me/settings', headers=headers, json=data)
                sleep(time)
    elif menuvar == "3":
        with open("config.json", "w", encoding='utf-8') as fw:
            fw.write('{\n"token":"')
            fw.write(str(input("token: ")))
            fw.write('",\n"status":"')
            fw.write(str(input("status: ")))
            fw.write('",\n"emoji":"')
            fw.write(str(input("emoji: ")))
            fw.write('",\n"list":["')
            print("Add commas to separate")
            var = str(input("list: "))
            fw.write(var.replace(',','","'))
            fw.write('"],\n"time":"')
            fw.write(str(input("time: ")))
            fw.write('"\n}')
            
    elif menuvar == "4":
        sys.exit()
    else:
        print("Please choose between (1-4)")


        






