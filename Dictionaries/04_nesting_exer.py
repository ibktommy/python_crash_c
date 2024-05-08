##### People #####
person1 = {
  'firstName': 'brad',
  'lastName': 'traversy',
  'age': 42,
}

person2 = {
  'firstName': 'andre',
  'lastName': 'neagoi',
  'age': 38,
}

person3 = {
  'firstName': 'john',
  'lastName': 'smilga',
  'age': 40,
}

tutors = [person1, person2, person3]
#print each tutor
for tutor in tutors:
  print(tutor['firstName'].title() + " " + tutor['lastName'].title() + " is " + str(tutor['age']) + " years old.")
print('\n')


##### Favourite Places #####
favorite_places = {
  'dave': ['tokyo', 'kuwait', 'mexico'],
  'dapo': ['singapore', 'canada', 'malaysia'],
  'scarlett': ['nigeria', 'israel', 'russia'],
}

for name, places in favorite_places.items():
  print(name.title() + " favorite places include: \t")
  for place in places:
    print(place.title())
  print('\n')
print('\n')


##### Cities #####
cities = {
  'abuja': {
    'country': 'nigeria',
    'population': 1500000,
    'fact': 'capital of nigeria',
  },
  'dubai': {
    'country': 'united arab emirate',
    'population': 2000000,
    'fact': 'capital of UAE',
  },
  'beijing': {
    'country': 'china',
    'population': 10000000,
    'fact': 'capital of china',
  }
}

for city, details in cities.items():
  print("The following are information about " + city.title() + "\t")
  for param, value in details.items():
    print(param.title() + ": " + str(value))
print('\n')

