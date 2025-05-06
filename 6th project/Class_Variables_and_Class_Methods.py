class Student:
    school_name = "Usman Public School System"

    @classmethod
    def show_school(cls):
        print("School Name:", cls.school_name)

Student.show_school()
