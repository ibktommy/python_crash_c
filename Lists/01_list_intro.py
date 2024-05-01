bicyles = ['trek', 'cannondale', 'redline', 'specilaized'];
print(bicyles)

# Accessing elements in a List
print(bicyles[2])
print(bicyles[2].title())
print(bicyles[-1].upper()) # access last element in a list

# Individual values from a list
message = 'My first bicylce was a ' + bicyles[0].title() + '.'
print(message)

# Changing, Adding, and Removing Elements
# modify elements
cars = ['tesla', 'honda', 'benz', 'toyota']
print(cars)

cars[1] = 'kia'
print(cars)

# add element to end of list
cars.append('audi')
print(cars)

# insert element to any position in a list
cars.insert(2, 'mazda')
print(cars)

# remove element from a list (using "del" statement)
del cars[-1]
print(cars)

# remove element from a list (using "pop" statement)
poppedCar = cars.pop()
print(poppedCar.upper())
print(cars)
print('The last car bought was a ' + poppedCar.title() + '.');

# pop item from any position in a List
selectedPoppedCar = cars.pop(2)
print(selectedPoppedCar)

# remove item by its value
cars.remove('kia')
print(cars)