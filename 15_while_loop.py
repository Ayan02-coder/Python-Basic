#while loop question

#print numbers from 1 to 100
i = 1
while i <=100:
    print(i)
    i += 1
    
print("-------------------------------------------")

#print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
    
print("--------------------------------------------")

#print multiplication of table of number n
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1
    
# print("---------------------------------------------")
#print a element of the following list using loop 

list =[1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list) :
    print(list[i])
    i += 1

print("---------------------------------------------")

# find a number in list
list =[1,4,9,16,25,36,49,64,81,100]
num = int(input("Enter a number for searching: "))
i = 0
while i < len(list):
    if num == list[i]:
        print("Find at index",i)
    i += 1


#WAP to find the sum of first n numbers
n = int(input("Enter a number: "))
sum =0
i = 1
while i <=n:
    sum += i
    i += 1
    
print(sum)








