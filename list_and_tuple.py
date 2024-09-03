#list and tuple

mark = [23,56,45,67,65]
print(mark[0])
print(type(mark))
print(len(mark))
mark[0] = "my mark"
print(mark)

print(mark[3])A
print(mark[1:4])

list = [1,5,3]
print(list)
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)

list1 = ["banana","mango","34","Apple"]
list1.sort()
print(list1)

list.insert(2,9)
print(list)
list2.copy(list)
print(list2)

tuple = (87,24,97,39)
# tuple[0] = 3  #not allow 
print(tuple)
print(type(tuple))
