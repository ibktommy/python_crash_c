# PYHTON DICTIONARY

alienZero = {'color': 'green', 'points': 5}


# Accessign values in a Dictionary
print(alienZero['color'])
print(alienZero['points'])

alienZeroPoint = alienZero['points']
print("AlienZero has " + str(alienZeroPoint) + ' ' + 'points')
print('\n')

# Adding New key-value pairs
alienZero['x-pos'] = 0
alienZero['y-pos'] = 25
print(alienZero)
print('\n')

# Modifying Values in a Dictionary
alienZero['color'] = 'yellow'
print(alienZero)
print('\n')

# Removing key-value pairs
del alienZero['points']
print(alienZero)
print('\n')

# Dicitionary of Similar Objects
favlang = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}
print("Sarah's fav prog language is " + favlang['sarah'].title())
