class Personal:
    # college="ADITYA"
    def __init__(self, name, city, adhar, phno):
        self.name = name
        self.city = city
        self.adhar = adhar
        self.phno = phno
        self.college = "aditya"

    def display(self):
        print(self.name, self.city, self.adhar, self.phno)

    @staticmethod
    def fun():
        print("hai")


class Student(Personal):
    # college="AEC"
    def __init__(self, name, city, adhar, phno, rollno, branch, per):
        self.rollno = rollno
        self.branch = branch
        self.per = per
        self.college = "aec"

    def display(self):
        super().display()
        print(self.rollno, self.branch, self.per)

    def fun():
        print("hello")


std1 = Student("Shiva", "KKD", "458751525", "9951722111", "123", "ECE", 68.67)
Student.fun()



