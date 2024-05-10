# moving items from one list to another
"""
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print("verifying user: " + current_user.title())
  confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())
"""

# Removing All Instances of Specific Values from a List
"""
pets = ['dog', 'cat', 'dog', 'rabbit', 'cat']

while 'dog' in pets:
  pets.remove('dog')

print(pets)
"""

# Filling a Dictionary with User Input
responses = {}

polling_active = True

while polling_active:
  name = input("\nWHat is your name? ")
  response = input("Which mountain would you like to climb someday? ")

  responses[name] = response

  repeat = input("Would you like to let another person respond! (yes/no) ")
  if repeat == 'no':
    polling_active = False

print("\n---_ Poll Results _---")
for name, response in responses.items():
  print(name + " would like to climb " + response + ".")

  