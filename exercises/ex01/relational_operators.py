a: str= input("Left-hand side: ")
b: str= input("Right-hand side: ")
A= int(a)
B= int(b)
one= bool(A<B)
two= bool(A>=B)
three= bool(A==B)
four= bool(A!=B)

print(a+ " < "+b+" is "+ str(one))
print(a+" >= "+b+" is "+ str(two))
print(a+" == "+b+" is "+ str(three))
print(a+" != "+b+" is "+ str(four))