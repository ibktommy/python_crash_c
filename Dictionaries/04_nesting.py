# Nesting
aliens = []

# make 30 green aliens
for alien in range(30):
  newAlien = {'color': 'green', 'points': '5', 'speed': 'slow'}
  aliens.append(newAlien)

# print the first 5 aliens
for alien in aliens[:5]:
  print(alien)
print("...")

# make the first 3 aliens yellow
for alien in aliens[0:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

# print the first 5 aliens 
for alien in aliens[:5]:
  print(alien)
print("...")

# A List in a Dictionary
favLangs = {
  'jen': ['python', 'ruby'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],
  'phil': ['python', 'haskell'],
}

for name, langs in favLangs.items():
  print("\n" + name.title() + "'s favorite languages are: ")
  for lang in langs:
    print("\t" + lang.title())
print('\n')

# A Dictionary in a Dictionary
devs = {
  'jen': {
    'role': 'frontend dev',
    'language': ['javascript'],
    'tools': ['vscode'],
  },

  'sarah': {
    'role': 'backend dev',
    'language': ['node js, java'],
    'tools': ['vscode'],
  },

  'drey': {
    'role': 'fullstack dev',
    'language': ['python', 'javascript', 'java'],
    'tools': ['intellij idea', 'vscode'],
  }
}

#get each dev name and languages with tools used and role
for dev, details in devs.items():
  print(dev.title() + ", a " + details['role'].title() + " uses the following language(s):" )
  for lang in details['language']:
    print("\t" + lang.title())
  print("and also use the following tools: ")
  for tool in details['tools']:
    print("\t" + tool.title())
  print('\n')
print('\n')

