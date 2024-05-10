##### Shawarma Ingredients #####
"""
prompt = "\nEnter the ingredients you want added in your Shawarma"
prompt += "\n(Enter 'quit' to end the program)\n"

active = True
while active:
  ingredient = input(prompt)

  if ingredient == 'quit':
    active = False
  else:
    print(ingredient.title() + " has been added.")
print("\n")
"""

##### Movie Tickets #####
prompt = "\nEnter your age to get your ticket"
prompt += "\n(Enter '-1' to end the program)\n"

active = True
while active:
  age = input(prompt)
  age = int(age)

  if age < 3 and age > 0:
    print("Ticket is free you kid")
  elif age >= 3 and age <= 12:
    print("Your ticket is $10")
  elif age > 12:
    print("Your ticket is $15")
  elif age == -1:
    active = False

