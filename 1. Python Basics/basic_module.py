
def f():
    print("B")

x = 5

print("A")

if __name__ == "basic_module":
    print("I have been imported")
elif __name__ == "__main__":
    print("I have been called directly")
