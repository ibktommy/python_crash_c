# Counting to Twenty
for num in range(1, 21):
  print(num)
print('\n')

# One Million
# for milli in range(1, 1000000):
#   print(milli)

# Summing a Million
oneMillion = list(range(1, 1000001))
minMilliNum = min(oneMillion)
print(minMilliNum)

maxMilliNum = max(oneMillion)
print(maxMilliNum)

sumMilliNum = sum(oneMillion)
print(sumMilliNum)
print('\n')

# Old Numbers from 1 - 20
oldNumberInTwenty = list(range(1, 21, 2))
print('Old Numbers from 1 - 20')
for oldNum in oldNumberInTwenty:
  print(oldNum)
print('\n')

# Threes
print('Mulitples of 3')
multiplesThree = list(range(3, 31, 3))
print(multiplesThree)
print('\n')

# Cubes
print('List of the first 10 cubes')
firstTenCubes = []
for cubeNum in range(1, 11):
  firstTenCubes.append(cubeNum**3)
print(firstTenCubes)
print('\n')

# Cubes - list comprehension
print('Print the cube of the first 10 numbers using "List Comprehension"')
listFirstTenCubes = [cubeNum**3 for cubeNum in range(1, 11)]
print(listFirstTenCubes)