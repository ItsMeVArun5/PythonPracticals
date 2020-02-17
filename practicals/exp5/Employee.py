class Employee:
    id = 1001
    DA = 0.10
    HRA = 0.25

    def __init__(self, ):
        self.id = Employee.id
        Employee.id += 1
        self.giveDetails()



    def giveDetails(self, ):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.address = input("Enter Address: ")
        self.phone_no = input("Enter phone number: ")
        self.base_salary = float(input("Enter Salary: "))


    def calculateGrossSalary(self, ):
        # self.getDetails()
        print ("\n-----------------Gross salary--------------------------")
        gross_salary = self.base_salary + self.DA*self.base_salary + self.HRA*self.base_salary 
        print ("Gross salary is: ",gross_salary)

    def getDetails(self, ):
        print ("\n--------------------Employee Details-----------------------")
        print ("ID: ", self.id)
        print ("Name: ", self.name)
        print ("Age: ", self.age)
        print ("Address: ", self.address)
        print ("Phone number: ", self.phone_no)
        print ("Salary: ", self.base_salary)


e1 = Employee()
e2 = Employee()
e1.getDetails()
e1.calculateGrossSalary()
e2.getDetails()
e2.calculateGrossSalary()