# Lists are eterogenuous - can contain any number of items, any types.
l = [0, 1]

# append (at the end)
l.append(2)

# insert (value 3 at position 0)
l.insert(0, 3)

# reassign (slicing)
l[0:2] = [10, 20]
print(l)

# concat
l = l + [30, 40]

# Compute sum of elements in the list
s = sum(l)
