# range() is lazy, generates numbers in memory as it needs them
for i in range(0, 100, 2):
    print(i, sep=" ")

print("================")

# enumerate(list) creates an iterable (0, list[0]), (1, list[1]), ...
r = range(5, 10)
for i, elem in enumerate(r): # [(0, 5), (1, 6), ...]
    print(i, " ", elem)

# zip(l1, l2) creates tuples (l1[0], l2[0]), (l1[1], l2[1])...
