# send otp via call or send otp api demo
# request integrated api (application programming interface)
import requests
import random
# otp providers api key
API_KEY="43f68128-b053-11f1-90d7-0200cd936042"
# RECEIVER PHONE NUMBERS
phone="7621034549"
# generate otp via random function
otp=str(random.randint(100000,999999))
#otp providers
url=f"https://2factor.in/API/V1/{API_KEY}/SMS/{phone}/{otp}"

# send otp via python script using exception handling
try:
    response=requests.get(url)
    print("status code :",response.status_code)
    print("Response :",response.text)

    if response.status_code==200:
        print("Otp send Successfully")
        # ask user to enter otp
        entered_otp=input("Enter your otp here :")
        # check otp right or wrong
        if entered_otp==otp:
            print("your otp entered successfully authenticated")
        else:
            print("you entered wrong otp try again")

except requests.exceptions.RequestException as e:
    print("Something went wrong while sending OTP or SMS",e)
