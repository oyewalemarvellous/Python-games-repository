#list
store = {}
goods= "oil_filter brake_pad new_tires spark_plugs clutch"
#intoduction
print("Welcome back to mech")
print("we have")
print(goods[0:9])
print(goods[11:19])
print(goods[21:29])
print(goods[31:41])
print(goods[43:48])
print("What do you want to buy")

#choices 
print("do you want to")
print("1.buy an item")
print("2.replace an item")
print("3.remove an item ")
print("4.see purchased item")
print("5.leave")

choice ={1:"buy an item",2:"relace an item",3:"remove an item",4:"see purchased item", 5:"leave"}

#buyer
while True:
    buyer= int(input("what do you want to do "))
    if buyer == 1:
        part=input("what do you want to buy? ")
        amount=int(input("how many "))
        store[part]=amount
    elif buyer == 2:
        part=input("what item do you want to replace? ")
        amount=input("what do you want to replace it with ")
        number=int(input("how many "))
        del store[part]
        store[amount]
        store[amount]=number
    elif buyer == 3:
        part= input("what do you want to remove ")
        del store[part]
    elif buyer == 4:
        print(store)
    elif buyer == 5:
        print("Thank you for shopping ")
        break