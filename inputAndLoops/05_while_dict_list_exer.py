# Deli
"""
pie_orders = ['meat pie', 'fish pie', 'chicken pie']
finished_pie = []

while pie_orders:
  current_pie = pie_orders.pop()
  print("The pie being made now is: " + current_pie.title())

  finished_pie.append(current_pie)

print("\nAll ordered pies are done and they are: ")
for pie in finished_pie:
  print("\t" + " " + pie.title() + " can now be collected")

print("\nAll pie have been collected")
"""

# No Meat Pie
"""
pie_orders = ['meat pie', 'fish pie', 'chicken pie', 'meat pie', 'fish pie', 'meat pie']
print("The Deli has run out of meat pie")
finished_pie = []
while 'meat pie' in pie_orders:
  pie_orders.remove('meat pie')

finished_pie = []
while pie_orders:
  current_pie = pie_orders.pop()
  finished_pie.append(current_pie)

print(finished_pie)
"""

# Dream Vacation
print("------ -- VACATION POLL --------")
poll_active = True

poll_result = {}

while poll_active:
  name = input("What is your name?\n")
  question = input("\nIf you could visit one place in the world, where would you like to go?\n")

  poll_result[name] = question

  repeat_question = input("Ask next person? Respond with 'yes/no'\n")
  
  if repeat_question == 'no':
    poll_active = False

print("\n ------ POLL RESULTS ------")
for name, question in poll_result.items():
  print(name.title() + " would like to visit " + question.title())



