class Student:
        def __init__(self, ):
            self.giveDetails()

        def giveDetails(self,):
            name = input("Enter name: ")
            self.name = name
            rollno = int(input("Enter rollno: "))
            self.rollno = rollno
            dept = input("Enter departement name: ")
            self.dept = dept
            pointer = int(input("Enter pointer: "))
            self.pointer = pointer

        def Result(self, ):
            student_class = {
                '10': 'outstanding',
                '9': 'Excellent',
                '8': 'Very Good',
                '7': 'Good',
                '6': 'Fair',
                '5': 'Average',
                '4': 'pass',
                '3': 'Fail',
                '2': 'Fail',
                '1': 'Fail',
                '0': 'Fail',
            }
            print ("Grade(pointer) \t \t Class")
            if self.pointer <= 10 and self.pointer >9:
                print (self.pointer, "\t \t",   student_class['10'] )
            elif self.pointer <= 9 and self.pointer > 8:
                    print (self.pointer, "\t \t",   student_class['9'] )
            elif self.pointer <= 8 and self.pointer > 7:
                    print (self.pointer, "\t \t",   student_class['8'] )
            elif self.pointer <= 7 and self.pointer > 6:
                    print (self.pointer, "\t \t",   student_class['7'] )
            elif self.pointer <= 6 and self.pointer > 5:
                    print (self.pointer, "\t \t",   student_class['6'] )
            elif self.pointer <= 5 and self.pointer > 4:
                    print (self.pointer, "\t \t",   student_class['5'] )
            elif self.pointer == 4:
                    print (self.pointer, "\t \t",   student_class['4'] )
            else:
                print (self.pointer, "\t \t",   student_class['3'])


s1 = Student()
s1.Result()
