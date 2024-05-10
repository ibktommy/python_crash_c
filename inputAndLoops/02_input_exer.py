##### Rental Car #####
"""
rental_car = input("What kind of rental car would you like?\n")
print("Let me see if I can find you a " + rental_car.title())
"""

##### Restaurant Seating #####
"""
group = input("How many people are in the dinner group? \n")
group = int(group)

if group > 8:
  print("Please, wait for a Table")
else:
  print("A Table is ready for your group")
print("\n")
"""

##### Multiples of Ten #####
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
  print(str(number) + " is a multiple of 10")
else:
  print(str(number) + " is not a multiple of 10")
print("\n")
