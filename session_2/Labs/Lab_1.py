W_H=int(input("enter your working hours: "))

if W_H>=40:
    salary=W_H*50
    print(f"your salary is {salary}")
else :
    salary=0.9*W_H*50
    print(f"your salary is {salary}")
    
    