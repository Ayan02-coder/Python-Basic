#for loop

#print elements of the following list using a loop

list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)
    
# find a number in list 
num = int(input("Enter a num :"))
for i in list:
    if num == i:
        print("Found")
        break
    
#Range

for el in range(5):
    print(el)
print("----------------------------------------")    
for el in range(1,5):
    print(el)
print("----------------------------------------")     
for el in range(1,10,2):
    print(el)
print("----------------------------------------")

print numbers from 1 to 100

for i in range(1,101):
    print(i)

print("--------------------------------------------")

#print number from 100 to 1

for i in range(100,0,-1):
    print(i)

#print mul table of num
n = int(input("Enter a num: "))
for i in range(1,11):
    print(n*i)
















