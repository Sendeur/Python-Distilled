# Elements must be immutable objects

# constructors
s = { 0, 1, 2 }       # literal
s = set([ 0, 1, 2 ])  # construct from collection
s2 = { 1, 2, 3 }

# set comprehensions
names = [ "A", "A", "B", "C" ]
s = { name for name in names }

# union
u = s | s2

# intersection
u = s & s2

# difference
u = s - s2

# symmetric difference (elements that are in either of them, but NOT in both)
u = s ^ s2

# add (a single element)
s.add("D")

# update (add multiple elements)
s.update({"D", "E", "F"})

# remove (if !exists, raise KeyError)
s.remove("A")

# discard (if !exists, noop)
s.discard("A")


