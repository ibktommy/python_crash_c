# Passing Arguments In Functions

## positional arguments
"""
def describe_movie(movie_name, movie_producer):
  print(f"I love {movie_name.title()}")
  print(f"{movie_name.title()} is produced by {movie_producer.title()}\n")

describe_movie('endgame', 'marvel')
describe_movie('justice league', 'DC comics')
"""

# keyword arguments - name-value pair
"""
def describe_movie(movie_name = "endgame", movie_producer = "marvel"):
  print(f"I love {movie_name.title()}")
  print(f"{movie_name.title()} is produced by {movie_producer.title()}\n")

describe_movie()
describe_movie(movie_producer="dc comics", movie_name="justice league")
"""
