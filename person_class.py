class Person:
    def __init__(self):
        print("object created")
        self.name = ""
        self.age = 0
    def display(self):
        print(self.name,self.age,self.height,sep= "\n")
object_1 = Person()
object_1.name = "Ezekiel"
object_1.age = 14
object_1.height = 5.11
object_1.display()
object_2 = Person()
object_2.name = "luke"
object_2.age = 15
object_2.height = 6.1
object_2.display()
object_3 = Person()
object_3.name = "luca"
object_3.age = 23
object_3.height = 6.5
object_3.display()

