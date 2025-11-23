# Function 1: Print your name 5 times
def print_name():
    for i in range(5):
        print("Alice")

# Function 2: Check if a number is even
def is_even(n):
    if n%2==0:
        return True
    return False

# Function 3: Add two numbers
def add(a,b):
    return a+b

# -------------------------
# Function Calls (Testing)
# -------------------------

print("Printing name 5 times:")
print_name()

print("------------------------")

print("Checking if 10 is even:")
print(is_even(10))  

print("------------------------")

print("Adding 10 and 20:")
print(add(10, 20))  

