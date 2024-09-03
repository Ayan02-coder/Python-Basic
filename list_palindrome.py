# WAP to check if list contains a palindrome of elements. 
# palindrome is string which reverse is same string
# like s = aba
# reverse of s = aba  its same so it is palindrome
list = [1,2,3,2,1]
list2 = [1,"abc",0,"abc",1]


list1 = []
list1 = list2.copy()
list1.reverse()

if(list2 == list1 ):
    print("palindrome")
else:
    print("Not")
