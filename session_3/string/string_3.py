##### string methods #####

#  [1] strip()  -> remove right and lift spaces by default 
#      rstrip() -> remove right spaces by default 
#      lstrip() -> remove lift spaces by default 

# string1="      Ahmed      "
# print(string1.strip())
# print(string1.rstrip())
# print(string1.lstrip())

# string1="0000Ahmed000000"
# print(string1.strip())
# print(string1.rstrip())
# print(string1.lstrip())

# string1="#$#$#$#$Ahmed#$#$#$#$"
# print(string1.strip("$#"))
# # print(string1.rstrip("#$"))
# # print(string1.lstrip())


#  [2] title() -> capitalize first char in each word 
# string2="my name is ahmed"
# print(string2.title())

# #  [3] Capitalize() -> capitalize first char in a string
# string3="my name is ahmed"
# print(string3.capitalize())

#  [4] upper() -> capitalize the string
string4="my name is ahmed"
print(string4.upper())
string4.upper()
#  [5] lower() -> lowercase the string
string5="my name is ahmed"
print(string5.lower())

#  [6] zfill(NUMB)   if Num=2   1->01 
x="10"
print(x.zfill(4))

# print(dir(str))