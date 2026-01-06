class Greeting:
    def __init__(self,name):
        self.name = name

    def display_welcome(self):
        print("welcome",self.name)
    def display_congratulations(self):
        print("congratulation",self.name)


obj = Greeting("ezekiel")
obj_2 = Greeting("marvellous")

obj.display_welcome()
obj_2.display_welcome()
obj.display_congratulations()