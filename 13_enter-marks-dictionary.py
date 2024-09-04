#WAP to enter marks of 3 subject from the user and store them in a dict. start with an empty dictionary & add one by one . use subject name as key and marks as value
dict = {}
x = int(input("enter phy: "))
dict.update({"phy" : x})
x = int(input("enter math: "))
dict.update({"math" : x})
x = int(input("enter IT: "))
dict.update({"IT" : x})
print(dict)
