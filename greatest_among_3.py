a = int(input("Enter a 1 number: "))
b = int(input("Enter a 2 number: "))
c = int(input("Enter a 3 number: "))
if a >= b and a >= c:
    print("Greater:",a)
elif b >= c:
    print("Greater:",b)
else:
    print("Greater:",c)
