def highest_even(list_params):
  for num in list_params:
    if num % 2 != 0:
      list_params.remove(num)
  return print(max(list_params))


list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

highest_even(list_of_numbers)

