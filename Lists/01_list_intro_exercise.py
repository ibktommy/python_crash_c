names = ['josh', 'kay', 'tuna', 'deon', 'hafsy']
# print name
print(names[2].title())
print('\n')

# print message to name
message = 'I will be coming over to your place.'
print('Watsup ' + names[0].title() + ',' + ' ' + message)
print('\n')

# guest list
invitedGuests = ['tuna', 'josh', 'kay'];
message = 'You are invited to dinner at my place tonight.'

print(invitedGuests[0].title() + ',' + ' ' + message)
print(invitedGuests[1].title() + ',' + ' ' + message)
print(invitedGuests[2].title() + ',' + ' ' + message)
print('\n')

# changing guest list
print(invitedGuests[-1] + ' will not be able to make it to dinner')


invitedGuests[-1] = 'clara'

print(invitedGuests[0].title() + ',' + ' ' + message)
print(invitedGuests[1].title() + ',' + ' ' + message)
print(invitedGuests[2].title() + ',' + ' ' + message)
print('\n')

# more guests
print("We got a bigger table so I will be inviting more people")

invitedGuests.insert(0, 'deon')
invitedGuests.insert(2, 'mag')
invitedGuests.append('gracy')
print('\n')

print(invitedGuests[0].title() + ',' + ' ' + message)
print(invitedGuests[1].title() + ',' + ' ' + message)
print(invitedGuests[2].title() + ',' + ' ' + message)
print(invitedGuests[3].title() + ',' + ' ' + message)
print(invitedGuests[4].title() + ',' + ' ' + message)
print(invitedGuests[5].title() + ',' + ' ' + message)
print('\n')

#shrinking guests
print("So sorry but now I can only invite two people")
removedPerson = invitedGuests.pop(0)
message = "Sorry, you are no longer invited to the dinner"
print(removedPerson.title() + ',' + ' ' + message)
print('\n')

removedPerson = invitedGuests.pop(2)
message = "Sorry, you are no longer invited to the dinner"
print(removedPerson.title() + ',' + ' ' + message)
print('\n')

removedPerson = invitedGuests.pop(-1)
message = "Sorry, you are no longer invited to the dinner"
print(removedPerson.title() + ',' + ' ' + message)
print('\n')

removedPerson = invitedGuests.pop(-1)
message = "Sorry, you are no longer invited to the dinner"
print(removedPerson.title() + ',' + ' ' + message)
print('\n')

print(invitedGuests[0].title() + ' and ' + invitedGuests[-1].title() + ',' + ' ' + 'you two are still invited to the dinner, thanks.')