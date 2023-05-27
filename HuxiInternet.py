import requests
import os
import json
import time

print("===============================================================")
print("===============================================================")
print("------------This program will automatically check--------------")
print("---------your Internet accessibility and automatically---------")
print("------------login your network account in the given------------")
print("----------------------interval time.---------------------------")
print("-----Before use, please modify the \"account.json\" first!-----")
print("===============================================================")
print("===============================================================")
with open("./account.json",mode="r",encoding="utf-8") as f:
    accountData=json.load(f)
accountName=accountData["accountName"]
urlAddr=accountData["accountUrl"]
sleepTime=accountData["sleepTime"]
print("Current account name: ")
print(accountName)
print("Current sleep time(in Minute): ")
print(sleepTime)

def ping():
    ''' 
    ping 主备网络 
    result: 0->OK, other->error
    '''
    print("Test Internet accessibility......")
    result = os.system(u"ping www.bing.com")

    return result

def login():
    pingRes=ping()
    print("Ping result: ")
    print(pingRes)
    if pingRes:
        print("Internet not accessible......")
        print("Login now.")
        res=requests.get(url=urlAddr)
        # print(res.status_code)
        if res.status_code==200:
            print("Login success!")
            print(res.content)
        else:
            print("Login error!")
            print("Error Code:")
            print(res.status_code)
            print("Error Info:")
            print(res.content)
    else:
        print("Internet already accessible, no need to login again.")

def main():
    while True:   
        login()
        time.sleep(60*sleepTime)
main()