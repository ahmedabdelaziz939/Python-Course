# # def sum1(x,y):
# #     return x+y
# # def sub1(x,y):
# #     return x-y
# # def div(x,y):
# #     return x/y
# # def mult(x,y):
# #     return x*y
# # print("""1-add
# #       2-sub
# #       3-div
# #       4-mult
# #       """)
# # op=int(input())
# # x,y=map(float,input().split())
# # if op==1:
# #     result=sum1(x,y)
# # print(result)



# # x=list(map(int,input().split()))
# # def maxx(list1):
# #     max=list1[0]
# #     min=list1[0]
# #     for i in list1:
# #         if i>max:
# #             max=i
# #         if i<min:
# #             min=i
# #     return max,min
# # res1,res2=maxx(x)
# # print(res1,res2)


# # dic={
# #     "1234567891234567":{"name":"ahmed abdelaziz ali",
# #                         "balance":20000}
# # }
# # def transection(x,y,dik):
# #     if x>dik[y]["balance"]:
# #         print("insufficient amount")
# #     elif x>2000:
# #         print("exceeds the limit")
# #     else :
# #         dik[y]["balance"]-=x

# # s=input()
# # transection(3000,s,dic)
# # print(dic[s]["balance"])


# # def factorial(num):
# #     if num == 0 or num== 1:
# #         return 1
# #     else:
# #         return num*factorial(num-1)
# # x=factorial(5)
# # print(x)

# import random 

# class1=[]

# for i in range(10):
#     class1.append(random.randint(0,100))
    
# passed_grade=50


# # for i in class1:
# #      if i >50:
# #           no+=1
 
# passed_student1=sum(grade >= passed_grade for grade in class1)
# failed_student1=sum(grade < passed_grade for grade in class1)
# print(class1)
# print(passed_student1)
# print(failed_student1) 


# try:
#     x = int(input("Enter a positive number: "))
#     if x <= 0:
#         raise ValueError("Input must be a positive number")
# except ValueError as ve:
#     print(f"Error: {ve}")

# Creating a new file or truncating an existing one
# with open('new_file.txt', 'w') as file:
#     file.write("Hello, this is a new file!\n")
#     file.write("Writing some content to the file.")
# with open('new_file.txt','a') as file:
#     file.write("11111:name,zizo")
# dic={}
# c=''
# with open('new_file.txt','r') as file:
#     c=file.read()
#     print(c.strip().split(",")[6])
# for i in range(len(c.strip().splitlines())):
#     pass
# key=c.split(",")[0]
# lista=c.split(",")
# dic[key]={lista[1]:lista[2],lista[3]:lista[4],lista[5]:lista[6]}
# print(dic)


# # adding account
# u=input() #name
# age=int(input()) #pan
# city=input()

# with open('new_file.txt', 'a') as file:
#    file.write(f"person:{u}\n age:{age} \n city:{city}\n")


# nested_dict = {}

# with open('new_file.txt', 'r') as file:
#     current_person = None

#     for line in file:
#         line = line.strip()
#         if line.startswith("person:"):
#             current_person = line.split(":")[1].strip()
#             nested_dict[current_person] = {}
#         elif current_person:
#             key, value = line.split(":")
#             nested_dict[current_person][key.strip()] = value.strip()

# print(nested_dict)


# # Squaring each element in a list
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x%2==0, numbers)
# result = list(squared_numbers)
# print(result)
# # Output: [1, 4, 9, 16, 25]

# def say_hello(a="ahmed"):
#     print(f"hello {a}")
# say_hello("mohamed")

# --------------------------------
# -- File Handling => Read File --
# --------------------------------

# myFile = open("new_file.txt", "r")

# print(myFile)  # File Data Object
# # print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read())
# print(myFile.read(5))

# # print(myFile.readline(5))
# print(myFile.readline())
# print(myFile.readline())

# print(myFile.readlines())
# print(myFile.readlines())
# print(type(myFile.readlines()))

# for line in myFile:

#   print(line)

#   if line.startswith("07"):

#     break

# # Close The File

# myFile.close()


