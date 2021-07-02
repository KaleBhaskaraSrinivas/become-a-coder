class Personal:
    college="ADITYA"
    def __init__(self,name,city,adhar,phno):
        self.__name=name
        self.city=city
        self.adhar=adhar
        self.phno=phno
    def display(self):
        print(self.__name,self.city,self.adhar,self.phno)
    def getname(self):
        return self.__name


class Student(Personal):
    def __init__(self,name,city,adhar,phno,rollno,branch,per):
        super().__init__(name,city,adhar,phno)
        self.rollno=rollno
        self.branch=branch
        self.per=per
    def display(self):
        
        print(self.rollno,self.branch,self.per)


class Faculty(Personal):
    def __init__(self,name,city,adhar,phno,empid,dept,nsh,sal):
        super().__init__(name,city,adhar,phno)
        self.dept=dept
        self.empid=empid
        self.nsh=nsh
        self.salary=sal
    def display(self):
        Personal.display(self)
        print(self.empid,self.dept,self.nsh,self.salary)
    
   

std1=Student("Shiva","KKD","458751525","9951722111","123","ECE",68.67)
fac1=Faculty("Sudhir","RJY","1457896","9059767522",2935,"CSE",4,55000)
fac1.display()


"""
private var using public methods
pro

"""


