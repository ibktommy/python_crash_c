# Conditional Tests
name = 'Tomide'
print(name == 'tomide')
print(name != 'Tomide')
print(name == 'Tomide')
print('\n')

print('Tests using the "and" keyword and the "or" keyword')
number = 24
print(number <= 46 and number >= 20)
print(number <= 46 or number >= 20)
print('\n')

print('Checking an item presence in a list')
evenNumbers = [eachNum for eachNum in range(2, 21, 2)]
print(3 in evenNumbers)
print(10 in evenNumbers)
print(5 not in evenNumbers)
print('\n')

# Alien Colors #1
print("Alien color game")
alien_color = 'green'
if alien_color == 'green':
  print('Player just earned 5 points')
print('\n')

# Stages of Life
age = 68

if age < 2:
  print("Still a baby")
if age >= 2 and age < 4:
  print("A Toddler here")
if age >= 4 and age < 13:
  print("A kid already")
if age >= 13 and age < 20:
  print("A Teenager, woah!")
if age >= 20 and age < 65:
  print("Adulthood has set in")
if age >= 65:
  print("Finally, an Elder!")
print('\n')


# Hello Admin
usernames = ['doenDev', 'magDev', 'atomDev', 'scarlett', 'widow', 'admin']

for username in usernames:
  if username == 'admin':
    print("Hello " + username + ',' +  " would you like to see a status report?")
  else: 
    print("Hello " + username + ',' + ' thank you for logging in again.')
print('\n')

# No Users
usernames = []
if not usernames: 
  print("We need to find some users!")
print('\n')

# Checking Usernames
current_users = ['atom', 'deon', 'maggy', 'scarlett', 'widow']
new_users = ['Maggy', 'pedro', 'widow', 'calisey']

for newUser in new_users:
  if newUser.lower() in current_users:
    print("This username " + "'" + newUser + "'" + " has already been taken.")
  else: print(newUser.title() + " is available")
print('\n')

# Ordinal Numbers
nums = [num for num in range(1, 10)]
print(nums)

for num in nums:
  if num == 1:
    print("1st")
  elif num == 2:
    print("2nd")
  elif num == 3:
    print("3rd")
  else:
    print(str(num) + "th")
print('\n')





