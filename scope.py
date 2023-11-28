# Scope - global and local

fname = "Daniel"
lname = "Nguyen"

def greet():
    fname = "Kim"
    lname = "Le"
    print("Inside the fuction")
    print(fname)
    print(lname)

print("Outside the function")
print(fname)
print(lname)
greet()