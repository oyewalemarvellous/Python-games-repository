class Car:
    def __init__(self,car_name,car_color,car_speed):
        self.name = car_name
        self.color = car_color
        self.speed = car_speed
    def display(self):
        print(self.name,self.color,self.speed,sep = "\n")

car_1 = Car("toyota","green","210")
car_1.display()