# Slices
firstHundredDigits = list(range(1, 101))
print('First Hundred Digits are : ')
print(firstHundredDigits)
print('\n')

print('The first 3 numbers in the list are: ')
print(firstHundredDigits[:3])
print('\n')

print('Three items of the middle of the list are: ')
print(firstHundredDigits[48:51])
print('\n')

print('Last three items in the list')
print(firstHundredDigits[-3:
print('\n')])

# My Pie, Your Pie
myPie = ['fish pie', 'chicken pie']
friendPie = myPie[:]

myPie.append('pizza pie')
friendPie.append('bread pie')

print('My favorite pies are: ')
for pie in myPie:
  print(pie.title())
print('\n')

print('My friend fav pie are: ')
for pie in friendPie:
  print(pie)
