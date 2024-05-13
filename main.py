import os
import random
import time

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
normal = "\033[0m"

print(blue, "\n\nLoading the Form....")
print("\n\nPlease wait...", normal)
time.sleep(3)
os.system("clear")

headline = (
    f'{purple}\n\n              _____ BASIC INFORMATION FORM _____{normal}')

print(headline.center(100))

while True:
  name = input("\n\n\nEnter you name ---------------------> ").strip().title()
  if name == "":
    print(red, "\n\n\nName is required", normal)
    continue
  date_birth = input("\n\nEnter your date of birth -----> ").strip()
  tele_phone = input("\n\nEnter your telephone number --> ").strip()
  email = input("\n\nEnter you email -------------------> ").strip()
  address = input("\n\nEnter your address -----------------> ").strip()

  break
nikhil = {
    "name": name,
    "birth": date_birth,
    "telephonenumber": tele_phone,
    "email": email,
    "address": address
}

print()
os.system("clear")
print(green, "\n\nSending you form to company....")
time.sleep(3)
os.system("clear")
print(
    f'{purple}\n\n              _____ BASIC INFORMATION FORM _____\n{normal}')

print(green, "\n\nsuccessfuly submited form 👍", normal)
print("\n\nHere's your message for furthere information\n\n\n")
print(f"""{green}
Hi {nikhil['name']},
what's going on. we are planning to move you to UK with our international marketing 
team. Just to make sure your personal contacts are correct just go through it.
your date of birth is {nikhil['birth']}. your telephone number 
is {nikhil['telephonenumber']} and last your address {nikhil['address']}\n\n
make sure to check your above details. Once you 
respond us ok, we will send you, your flight tickets on {nikhil['email']}  
{normal}""")
