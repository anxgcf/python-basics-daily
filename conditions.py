# Program 1: Pass or Fail
mark=int(input("Enter your mark:"))

if mark>=40:
    print("Result: Pass")
else:
    print("Result: Fail")

print("------------------------------")

# Program 2: Check Odd or Even
num=int(input("Enter a number: "))

if num%2==0:
    print("It is Even")
else:
    print("It is Odd")

print("------------------------------")

# Program 3: Biggest of 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>=b and a>=c:
    print("Biggest number is:", a)
elif b>=a and b>=c:
    print("Biggest number is:", b)
else:
    print("Biggest number is:", c)
