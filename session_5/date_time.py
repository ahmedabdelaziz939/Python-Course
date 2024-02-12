import datetime 

# # print(dir(datetime))
# # print(dir(d.datetime))

# # Print The Current Date and Time
# print(datetime.datetime.now())

# # print("#" * 40)

# # # Print The Current Year
# print(datetime.datetime.now().year)

# # # # Print The Current Month
# print(datetime.datetime.now().month)

# # # # Print The Current Day
# print(datetime.datetime.now().day)

# # # Print Start and End Of Date
# print(datetime.datetime.min)
# print(datetime.datetime.max)


# # # Print The Current Time
# print(datetime.datetime.now().time())


# # # Print The Current Time Hour
# print(datetime.datetime.now().time().hour)

# # # Print The Current Time Minute
# # print(datetime.datetime.now().time().minute)

# # # Print The Current Time Second
# # print(datetime.datetime.now().time().second)


# # # Print Start and End Of Time
# print(datetime.time.min)
# print(datetime.time.max)

# # # # Print Specific Date
# print(datetime.datetime(1982, 10, 25))
# # print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

# myBirthDay = datetime.datetime(1982, 10, 25)   #.year
# dateNow = datetime.datetime.now()              #.year

# # print(f"My Birthday is {myBirthDay} And ", end="")
# # # print(f"Date Now Is {dateNow}")

# print(f" I Lived For {(dateNow - myBirthDay)}")
# print(f" I Lived For {(dateNow - myBirthDay).days} Days.")


# import datetime
myBirthday = datetime.datetime(1982, 1, 25)

# print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%m/%Y"))
# print(myBirthday.strftime("%d, %B, %Y"))
# print(myBirthday.strftime("%d/%B/%Y"))
# print(myBirthday.strftime("%d - %B - %Y"))
# print(myBirthday.strftime("%B - %Y"))