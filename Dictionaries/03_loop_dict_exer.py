##### RIVERS #####
rivers = {
  'nile': 'egypt',
  'zambezi': 'zambia',
  'limpopo': 'south africa',
}

# Print sentence about each river
for river, country in rivers.items():
  print("The " + river.title() + " river can be found in " + country.title() + ".")
print('\n')

# Print the name of each River
print("Some Rivers in Africa are: ")
for river in rivers.keys(): 
  print(river.title())
print('\n')

# Print the name of each country
print("The above Rivers are located in these countries respectively: ")
for country in rivers.values():
  print(country.title())
print('\n')


##### POLLING #####
favlang = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

programmers = ['sarah', 'drey', 'marcko', 'jen', 'edward', 'phil']
for programmer in programmers:
  if programmer in favlang.keys():
    print(programmer.title() + ", you have taken the poll. Thanks")
  else:
    print(programmer.title() + ", take a poll to know your fav. lang.")
print('\n')


