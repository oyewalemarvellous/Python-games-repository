Number=(1,2,3,4,5,6,7,[10,22])
for i in range(7):
    print(Number[i])
print(Number[2])

num= {1,2,3,4,5,6,}
num2={6,3,4,5,7,9,8}
print (num.intersection(num2))
print (num2.union(num))
print (num.difference(num2))
print (num2.difference(num))
print (num.symmetric_difference(num2))



