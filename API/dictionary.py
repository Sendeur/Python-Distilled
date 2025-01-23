
# empty dict
d = dict()

d = { 
    "a" : 0,
    "b" : 1,
}

# get (with default value, if key not present)
c = d.get("c", 2)

# del
del d["b"]

# keys() - returns a dict_keys view. Changes made to dict will be reflected in "kys"
kys = d.keys()
    # Py>3.6 => keys() holds insertion order

# values() - returns a dict_values view. Changes made to dict will be reflected in "vls"
vls = d.values()

# items() - returns a dict_items view. Changes made to dict will be reflected in "itms"
itms = d.items()
