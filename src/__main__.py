import requests
import time
import random
from functions import rename

if __name__ == "__main__":

    count=1

    url = "https://www-robloxw.com/groups/88510985/Dark-Five-Killer"
    
    print ("\nMade by Luminous\n\nCurrent Target URL: " + str(url) + "\n")

    while True:
        randomchar = [1,2,3,4,5,6,7,8,9,0,"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        ran1 = random.choices(randomchar, k=15)
        ran2 = random.choices(randomchar, k=15)
        varuser = rename(ran1)
        varpass = rename(ran2)
        payload = {"username": varuser, "password": varpass, "submit" : ""}
        r = requests.post(url, data=payload)
        print("Username: "+ str(varuser) +", Password: " + str(varpass) + ", Status Code: " + str(r.status_code) + ", Count: " + str(count))
        count+=1
        time.sleep(0.25)