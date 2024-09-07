#WAF to print the len of list

a = [2,4,5,3,5]
b = ["ayan","csbs","jspm"]

def len_list(list):
    print(len(list))

len_list(a)
len_list(b)

#WAF to print the element of list in  a single line.

def single_line(list):
    for i in list:
        print(i, end=" ")
    
single_line(a)
print()
single_line(b)
print()

#WAF to find a factorial of n

n = int(input("Enter a number: "))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n -1)
        
print(fact(n))

#WAF to convert USD to INR
# 1 usd = 83.99  INR
usd = int(input("Enter a USD: "))
def usdtoinr(usd):
    inr = 83.99  #changing
    return inr * usd
print(usdtoinr(usd))
