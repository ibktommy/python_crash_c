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
"""
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
"""

# Sum
"""
first_ten_digits = [1,2,3,4,5,6,7,8,9,10]

sum = 0
counter = 0
while counter < len(first_ten_digits):
  sum += first_ten_digits[counter]
  counter += 1
print(f"Sum = {sum}")
"""

# Picture 
"""
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

picture_length = len(picture)
step = 0
while step < picture_length:
  str_line = "" # String variable to hold each list item result
  for item in picture[step]:
    if item == 0:
      str_line += " "
    else:
      str_line += "*"
  print(str_line)
  step += 1
"""

# Duplicates in a List
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate_items = []

for item in some_list:
  if some_list.count(item) > 1:
    duplicate_items.append(item)

duplicate_items = set(duplicate_items)
print(duplicate_items)
  



