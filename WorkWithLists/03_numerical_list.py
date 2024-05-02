# Range function
for number in range(1, 6):
  print(number)
print('\n')

# Range with 'List' function
firstTenNumbers = list(range(1, 11))
print(firstTenNumbers)

# Range with 'List' and omitting some numbers
oldNumbers = list(range(1, 11, 2))
print(oldNumbers)

# Range to make 'list of first ten squared numbers'
squaredNumbers = []
for eachNum in range(1, 11):
  squaredNumbers.append(eachNum*eachNum)
print(squaredNumbers)

# 'mix, max and sum' functions
minNum = min(firstTenNumbers)
print('The smallest number in the first ten numbers is: ' + str(minNum))
print('\n')

maxNum = max(firstTenNumbers)
print('The largest number in the first ten numbers is: ' + str(maxNum))
print('\n')

sumNum = sum(firstTenNumbers)
print('The sum of numbers of the first ten numbers is: ' + str(sumNum))
print('\n')

# List comprehension - creating list in shorter code
evenNumbers = [eachNum**2 for eachNum in range(1, 11)]
print(evenNumbers)