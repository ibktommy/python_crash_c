# Looping through all key-value pairs
user_0 = {
  'username': 'henrico',
  'firstName': 'henry',
  'lastName': 'jacob',
}

for key, value in user_0.items():
  print("\nKey: " + key)
  print("Value: " + value.title())
print('\n')

favlang = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

for name, lang in favlang.items():
  print(name.title() + "'s" + " favourite prog. lang. is " + lang.title())
print('\n')

# Looping through all keys in a Dictionary
for name in favlang.keys():
  print(name.title())
print('\n')

friends = ['phil', 'sarah']
for name in favlang.keys():
  print(name.title())

  if name in friends:
    print("Hi " + name.title() + "," + " I see your fav prog. lang. is " + favlang[name].title())
print('\n')

# Looping through all Values in a Dictionary
print("The following languages are favourites: ")
for lang in favlang.values():
  print(lang.title())
print('\n')


# Getting disctinct values in a Dictionary using "set"
for lang in set(favlang.values()):
  print(lang.title())
print('\n')