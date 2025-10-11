print("welcome to our store")
store= {"milk":2.30,"bread":1.00,"sugar":1.50,"biscuit":2.80,"water":3.60,"cake":6.10,"lamp":9.90}
goods ={}
print("we have;\n")
for key,value in store.items():
    print(key,"$" + str(value))

while True:
    item=input("what do you want to buy?(type stop when done buying ) ")
    if item == "stop":
        break
    if item not in  store:
        print("wrong input")
        continue
    quantity=int(input("How many? "))
    goods[item]=quantity
print("item     qty  amt   total")
final_price= 0
for key in goods:
    total=goods[key]*store[key]
    print(key.ljust(9," "),str(goods[key]).ljust(3," "),"$"+str(store[key])," $" + str(round(total,2)))
    final_price+=total 
print(("$" + str(round(final_price,2))).rjust(24," ")) 
    
