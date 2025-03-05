# Generators have a similar syntax to list comprehensions, but with rounded parantheses:
l = [ 1, 2, 3, 4, 5 ]
squares = ( e * e for e in l ) # generator object

# Produce elements one by one from the generator
elem = next(squares) # 1
elem = next(squares) # 4
elem = next(squares) # 9
# ...

# Can be converted to a list using the list() call
squares_list = list(squares) # Generates all elements at once.


