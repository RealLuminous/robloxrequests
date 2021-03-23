import requests
import time
import random
import asyncio
from functions import rename

async def main():
    randomstuff = [1,2,3,4,5,6,7,8,9,0,"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    stuff = random.choices(randomstuff, k=15)
    stuff2 = random.choices(randomstuff, k=15)
    varuser = rename(stuff)
    varpass = rename(stuff2)
    payload = {"token" : "684605a1ba3232678.1000751601|r=us-east-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=transparent|meta=6|lang=en|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|ht=1|cdn_url=https://cdn.arkoselabs.com/fc|lurl=https://audio-us-east-1.arkoselabs.com|surl=https://roblox-api.arkoselabs.com", "webhook": "XyzzI", "username": varuser, "password" : varpass}
    r = requests.post(url, data=payload)
    print("Username: "+ str(varuser) +", Password: " + str(varpass) + ", Status Code: " + str(r.status_code))
    await asyncio.sleep(0.25)


url = "https://www-rooblox.com/api/loginv2.php"
print ("\nMade by Luminous\n\nCurrent Target URL: " + str(url) + "\n")

while True:
    asyncio.run(main())