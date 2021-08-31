a: str= input("Left-hand side: ")
b: str= input("Right-hand side: ")
A= int(a)
B= int(b)
one: int=A**B
two: float=A/B
three: int=A//B
four: int=A%B

print(a+ " ** "+b+" is "+ str(one))
print(a+" / "+b+" is "+ str(two))
print(a+" // "+b+" is "+ str(three))
print(a+" % "+b+" is "+ str(four))