#CSE 111 - Programming with functions
#Name: Bruno de Sousa Teixeira

import math
pi = math.pi

print('This program will help you to calculate the volume of a tire.')
width = float(input("Enter the widht of the tire: "))
asp_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire: "))

volume = pi * width**2 * asp_ratio * (width*asp_ratio +2540 * diameter)/ 10000000000
print(f"The aproximmate volume of the tire is {volume:.2f}")

from datetime import datetime
date = datetime.now()

#Stretch challenge

firstname = ' '
lastname = ' '
phone_number = ' '

def appendtolist():
    with open('volumes.txt', 'at') as volumes_tire:
      volumes_tire.write(f'{date:%Y-%m-%d}, {float(width)}, {float(asp_ratio)}, {float(diameter)}, {volume:.2f} {firstname} {lastname} {phone_number}')

buy_option  = input("Do you want to buy the tire with the measures that you entered in the system? ")
option = buy_option.lower()

while option != "yes" and option != "no":
  print ("You put an incorrect value, please type 'yes' or 'no'. ")
  option = input("Do you want to buy the tire with the measures that you entered in the system? ")

if option == "yes":
  print("Let me get some of your informations to finish your shopping: ")
  firstname = input("What's your first name? ")
  lastname = input("What's your last name? ")
  phone_number = input("What's your phone number? ")
  appendtolist()
  print ("Your order was concluded! ")

elif option == "no":
  print("Ok, thank you for came here. If you decide to buy with us, let me know! ")

     

  
     
   
