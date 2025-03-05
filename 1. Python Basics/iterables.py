seq = (1, 2, 3, 4)  # immutable
seq = "1234"        # immutable
seq = [1, 2, 3, 4]
seq = {1, 2, 3, 4}

# Unpacking
a, b, c, d = seq
a, *extra = seq     # extra = [ 2, 3, 4 ] - always a list
a, *_ = seq     # [ 2, 3, 4 ] ignored
# *extra can appear in the middle as well
a, *extra, b = seq # a=1, extra=[2, 3], b=4

# Expansion
l = [ 0, *seq, 5 ]

# Conversions
l = list(seq)
t = tuple(seq)
s = set(seq)
min(seq)
max(seq)
any(seq)
all(seq)
sum(seq)
sorted_seq = sorted(seq)

# Slicing seq[start:end:slice]

# Named slice
firstTwo = slice(0, 2)
print(seq[firstTwo])
