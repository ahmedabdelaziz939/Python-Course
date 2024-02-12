x=[]
for i in range(10):
    y=int(input(f"Enter value numer {i+1}: "))
    x.append(y)
num_to_search=int(input("Enter a value to search: "))
print(f"value is exist at element number {x.index(num_to_search)+1}")