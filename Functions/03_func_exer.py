# City Names
"""
def city_country(city, country):
  return print(f'"{country.title()} {city.title()}"')

city_country('chile', 'santiago')
"""

# Album
def make_album(name, title, tracks=''):
  if tracks:
    album_dict = {'album_name': name, 'album_title': title, 'tracks': tracks}
  else:
    album_dict = {'album_name': name, 'album_title': title}
  return print(album_dict)

"""
make_album('africa', 'rise')
make_album('grow', 'peace', 8)
make_album('world', 'sing')
"""
# User Album
print("When tired of entering input, press 'q' to stop program!")
get_input = True

while get_input:
  album_name = input("Enter an Album: ")
  if album_name == 'q':
    get_input = False
    break; #stops the execution of the codes below in the while loop body

  album_song = input("Enter a song in the Album: ")

  make_album(album_name, album_song)



  

