class person :
    def __init__(self,name="cdsf",address=1231,PN=121):
        self.name=name
        self.address=address
        self.PN=PN
    def getName():
        pass
class student(person):
     def __init__(self, name, address, PN):
         super().__init__(name, address, PN)
        
ahmed=person("ahmed",1212,132132)
student1=student()
print(student1.name)
student1.getName()