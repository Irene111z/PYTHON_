
#if, else, elif
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = b**2 - 4*a*c
print(D)
if D == 0:
    result = -b/(2*a)
    print("x =", result)
elif D > 0:
    result = (-b + D**(1/2))/(2*a)
    print("x1 =", result)
    result = (-b - D**(1/2))/(2*a)
    print("x2 =", result)
else:
    print("impossible")