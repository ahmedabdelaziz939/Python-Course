# # # index(substring,from,to)
# a="My name is Ahmed"
# print(a.index("A",0,13))   #index 11
# print(a.index("A",0,10))   # error substring not found and program stop




# # # find(substring,from,to)
a="My name is ahmed"
print(a.find("A",0,13))   #index 11
# # print(a.find("A",0,10))   # -1 means substring not found and program continue
# # print("Ahmed")
# # rjust(width,fill char) ,rjust(width,fill char) fill char ->by default space
# a="Ahmed"




# print(a.ljust(10))
# print(a.rjust(10))
# print(a.ljust(10,"@"))
# print(a.rjust(10,"@"))
#############################################################3
# #splitlines() ->return List 
# a="""first Line
# second Line
# third Line"""
# print(a)
# print(a.splitlines())

# # e="first Line \nsecond Line \nthird Line"
# # print(e)
# # print(e.splitlines())


# # expandtabs()
# f="my\tname\tis\tAhmed"
# print(f)
# print(f.expandtabs(0))

# # istitle() -> check title return true or false
# # isspace() -> check space return true or false
# # islower() -> check lowercase return true or false
# # isupper() -> check uppercase return true or false
# # isidentifier() -> check var name is valid or not
# x="str"
# # isalpha() -> check characters not number or symbols
# print(x.isalpha())
# y="124ahed#"
# print(y.isalnum())
# # isalnum() -> check characters or number not symbols

# # replace(old, new, count)
# num="one ne ttwo one one two "
# print(num.replace("one", "1",2)) #count

# # "seperator".join()
# a=["Ahmed","Abdelaziz","Ali"]
# print(" ".join(a)) # check type()