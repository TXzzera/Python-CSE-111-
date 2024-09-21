from datetime import datetime

date = datetime.now()
#Getting the current date and time of the system
weekday = date.weekday()
#Getting the current day of the week

subtotal = float(input('What was the subtotal of your shopping? '))
#asking the total of the shopping cart of the user

if subtotal >= 50 and (weekday == 1  or weekday == 2):
#if the subtotal is equal or bigger than $50.00 and the day of the week is tuesday or wednesday, I'll give him a discount of 10%
    subtotal -= subtotal/10
    print(f"On tuesdays and wednesday we have a discount of 10% in the purchases. Your new subtotal is ${subtotal:.2f}")
#The discount of 10% was given, I just decreased 10% of the subtotal.

else: #If the subtotal is less than $50.00 and it's not tuesday or wednesday, the user don't receive a discount.
    print("Unfortunately, we don't have discount today. Just on Tuesday and Wednesday. ")
    print(f"The subtotal is ${subtotal:.2f}")

add_tax = subtotal/6 
print(f"The sale tax is 6%, that correspond to ${add_tax:.2f} ")
#to calculate the sale tax, I just need to divide the subtotal per 6 and decrease this value from the subtotal

amount_due = subtotal + add_tax
print(f"The amount of your shopping is ${amount_due:.2f}")
#Adding the tax to the subtotal, I give to user the real value that he needs to pay on his purchase.
