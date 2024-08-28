
class Employee:
    salary=25000
    def __init__(self,name,department):
        self.name=name
        self.department=department

    def show(self):
        print("name",self.name,"department",self.department,"salary",Employee.salary)
    @classmethod
    def change_salary(cls,salary):
        cls.salary=salary
obj=Employee("crag","IT")
obj.show()
Employee.change_salary(45000)
obj.show()
    
