# while loop
"""
number = 1
while number <= 5:
  print(number)
  number += 1
print("\n")
"""

"""
message = ""
while message != 'quit':
  message = input("Guess my name \n")
  if message != "quit":
    print(message)
print("\n")
"""

# Using a flag
"""
active = True
while active:
  message = input("Whats your name \n")

  if message == "quit":
    active = False
  else:
    print(message)
print("\n")
"""

# Using a break to exit a loop
"""
prompt = "\nEnter the name of a city you have visited:"
prompt += "\n(Enter 'quit'  when you are done.) "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print("I would love to go to " + city.title() + "!")
"""

# Using continue in a loop
"""
number = 0
while number < 10:
  number += 1
  if number % 2 == 0:
    continue

  print(number)
"""



