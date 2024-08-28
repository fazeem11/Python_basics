class Employee:
    @staticmethod
    def sample_method(x):
        print("inside static method",x*x )
Employee.sample_method(10)
emp=Employee()
emp.sample_method(8)
