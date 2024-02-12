# myList = ["A", "B", "C", 1, 1.5, True]
# print(myList.find("a"))
## printing list 
# print(myList)  

## accessing element
# print(myList[1]) 
# print(myList[-1]) 
# print(myList[-3]) 

## slicing
# print(myList[0:4])  
# print(myList[:4]) 
# print(myList[1:])  
# print(myList[::1]) 
# print(myList[::2]) 

## modifying elements
# myList[1] = 2
# myList[-1] = False
# myList[0:3] = ["n"]
# print(myList)

## adding element
### 1.append()
#mylist = ["A", "B", "C"]
#mylist_1 = ["D", "f", "6"]
###["A", "B", "C",["D", "f", "6"]]
#mylist.append("Alaa")
#mylist.append(100)
#mylist.append(150.200)
#mylist.append(True)
#mylist.append(mylist_1)
#print(mylist)
#print(mylist[2])
#print(mylist[3])
#print(mylist[-1][-1])

### insert()
#f = [1, 2, 3, 4, 5, "A", "B"]
#f.insert(2, "Test")
#f.insert(-1, "rTest")
#print(f)

## Removing Elements
#x = [1, 2, 3, 4, 5, "Ahmed", True, "A", "A"]
#x.remove("A")
#print(x)

##Finding Elements
### count()
#d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
#print(d.count(1))

### index()
#e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
#print(e.index("Ramy"))

#Sorting
# y = [1, 2, 100, 120, -10, 17, 29]
# # y = ["A", "Z", "C"]
# y.sort(reverse=True)
# # y.sort(reverse=True)
# print(y)

# # Reversing
# z= [10, 1, 9, 80, 100, "A", 100]
# z.reverse()
# print(z)

# # Length of a List
# z= [10, 1, 9, 80, 100, "A", 100]
# length_of_list = len(z)
# print(length_of_list)

# # Membership
# z= [10, 9, 80, 100, "A", 100]
# is_present = 1 in z
# print(is_present)


## extend()
#a = [1, 2, 3, 4]
#b = ["A", "B", "C"]
#a.extend(b)
#print(a)


# # pop()
# my_list = [1, 2, 3, 4, 5]

# # Remove and return the element at index 2
# popped_element = my_list.pop(2)
# print("Popped Element:", popped_element)
# print("Updated List:", my_list)


# copy()
original_list = [1, 2, 3]
copied_list = original_list.copy()
# Modify the original list
original_list.append(4)
print("Original List:", original_list)
print("Copied List:", copied_list)


##List Comprehension
#squared_numbers = [x**2 for x in my_list if isinstance(x, int)]
# my_list=[1,2,3,'a',4,'v',5]
# squared_numbers = [x**2 for x in my_list if isinstance(x, int)]
# print(squared_numbers)
