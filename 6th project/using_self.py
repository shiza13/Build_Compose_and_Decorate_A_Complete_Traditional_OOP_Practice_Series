class Student:
    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks      

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Maya", 94)
student2 = Student("Ali", 86)

student1.display()
print("------")
student2.display()
