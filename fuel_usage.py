

def main():
  start_miles = float(input("Enter the initial value of the odometer reading (in miles): "))
  end_miles = float(input("Enter the endless value of the odometer reading (in miles): "))
  amount_gallons = float(input("Enter the amount of fuel in gallons: "))
  mpg = miles_per_gallon(start_miles,end_miles,amount_gallons)
  lp100k = end_miles - start_miles/mpg
  print(f"liters per 100 kilometers: {lp100k:.2f}")
  print(f"miles per gallon of fuel: {mpg:.2f}")
def miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  Return: Fuel efficiency in miles per gallon.
  """
  return
def lp100k(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  return
# Call the main function so that
# this program will start executing.
main()