from Model.person import person
class Store:
    def __init__(self):
        self.list=[]

    def add(self,newone):
        self.list.append(newone)
    

    def getEmployee(self):
        return self.list   

employee=Store() 
employee.add(person(1,'vani','Pune','HR'))
employee.add(person(2,'Rani','Hyderabad','Manager'))
employee.add(person(3,'Raju','Mumbai','TL'))
employee.add(person(4,'Abhi','pune','Manager'))
employee.add(person(5,'Naresh','mumbai','Developer'))
















































