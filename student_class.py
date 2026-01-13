class Student:
    def __init__(self,name,math,english,science):
        self.name = name 
        self.math = math
        self.english = english
        self.science = science
    def student_name(self):
        print("\nstudent name is " + self.name)
        print("scored a " + str(self.math) + " in maths\n"
        "a " + str(self.science) + " in science \n" + "and a " + str(self.english) + " in english\n")
        print("Total score is " + str(self.math + self.english + self.science) + "/300\n" + "congrates you scored " + str(round((self.math + self.english + self.science) / 300 * 100,2)) + "%")



p1 = Student("ezekiel",87,90,70)
p1.student_name()

p2 = Student("marvellous",70,80,90)
p2.student_name()