#write a recursive function to calculate sum of first natural numbers

n = int(input("Enter a number: "))
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
     
a = sum(n)
print(a)
print("---------------------------------------------")
# write a recursive function  to print all element in a list
list = [3,7,8,5]
def prlist(list,idx = 0):
    if len(list) == idx:
        return 
    print(list[idx])
    prlist(list,idx+1)
    
prlist(list)
