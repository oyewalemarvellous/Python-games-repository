class Mobile:
    def __init__(self,battery):
        self.battery = battery
    def battery_percent(self):
        return self.battery 
    def charging(self):
        self.battery += 2
    def using(self):
        self.battery -= 4    
phone = Mobile(70)
mobile= phone.battery_percent()
print(mobile)
phone.using()
print(str(phone.battery_percent()) + "%")
phone.charging()
print(str(phone.battery_percent()) + "%")
while phone.battery_percent() < 100:
        phone.charging()
print(str(phone.battery_percent()) + "%")
while phone.battery_percent() > 20:
    phone.using()
print(str(phone.battery_percent()) + "%")

