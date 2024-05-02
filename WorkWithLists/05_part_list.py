# Slicing a List
evenMultiples = [eachNum**2 for eachNum in range(2, 11, 2)]
print(evenMultiples[0:3])
print(evenMultiples[1:4])
print(evenMultiples[:2])
print(evenMultiples[2:])
print(evenMultiples[-2:])
print('\n')

# Looping through a Slice
print('The last 3 numbers in the list are: ')
for eachNum in evenMultiples[-3:]:
  print(eachNum)
print('\n')

# Copying a List
multiples = evenMultiples[:]
for eachMultiple in range(1, 11, 2):
  multiples.append(eachMultiple**3)
print(multiples)