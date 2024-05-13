# Return Values
"""
def get_formatted_name(first_name, last_name):
  full_name = (f"Your full name is \n\t {first_name.title()} {last_name.title()}")
  return full_name

print(get_formatted_name("scarlet", "johnson"))
"""

# making an argument optional
"""
def get_formatted_name(first_name, last_name, middle_name=''):
  if middle_name:
    full_name = (f"Your full name is \n\t {first_name.title()} {middle_name.title()} {last_name.title()}")
  else:
    full_name = (f"Your full name is \n\t {first_name.title()} {last_name.title()}")
  return full_name

print("Dave", "Bash")
print("Dave", "Bash", "fedora")
"""

# returning a dictionary
def dev(name, age, role, fav=''):
  dev_dict = {'name': name, 'role': role, 'age': age}

  if fav:
    dev_dict['favorite'] = fav
  return dev_dict

print(dev('andrei', 38, 'senior dev', 'probably'))