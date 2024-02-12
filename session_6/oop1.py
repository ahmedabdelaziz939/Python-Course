# class  Car:
#     def __init__(self,color,model,hp,stutus):
#        self.__color=color
#        self.__model=model
#        self.__hp=hp
#        self.__stutus=stutus
#     def stop(self):
#         self.__stutus=False
#     def colorChange(self,newColor):
#         self.__color=newColor 
#     def printColor(self):
#         print(self.__color)


# class student:
#     def __init__(self):
#         self.students=[]
#     def add(self,name,grdes,student_id):
#         x=[]
#         x.append(name)
#         x.append(grdes)
#         x.append(student_id)
#         if x not in self.students:
#             self.students.append(x)
#         else: print("error")
#     def removes(self,id):
#       if id in self.students:
#           self.students.remove(id)
          

# c=student()
# c.add("ahmed",50,1)
# c.removes(["ahmed",50,1])
# print(c.students)


import csv
class Item:
    items=[]
    def __init__(self,name:str,price:float,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.items.append(self)
    def total_price(self):
        return self.price*self.quantity
    @classmethod
    def get_data_csv(cls):
        with open("items.csv","r") as file:
            r=csv.DictReader(file)

            it=list(r)
            Item.items.append(it)
        # for item in items:
        #     Item(
        #         name=item.get('name'),
        #         price=item.get('price'),
        #         quantity=item.get("quantity")
        #     )
        # return Item 
    # def __repr__(self):
    #     return f"Item({self.name}, {self.price} ,{self.quantity})"
item1=Item("cable",100,2)
item1=Item("cable",100,2)
item1=Item("cable",100,2)
item1=Item("cable",100,2)
item1=Item("cable",100,2)
item1.get_data_csv()
print(Item.items)




"""
1 class student
add 
remove 
student info 

2 class student database => list 

"""