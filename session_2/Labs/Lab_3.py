
grade=float(input("enter your grade: "))
print(grade)
if grade<0 or grade>100:
    print("error, please check your grade again")
elif grade<50:
    print("Failed")
elif grade<65:
    print("Normal")
elif grade<75:
    print("Good")  
elif grade<85:
    print("very Good")
else :
    print("Excellent")  
  

    