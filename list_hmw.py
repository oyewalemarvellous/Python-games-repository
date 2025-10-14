number_list=[]
for i in range(3):
    second_list=[]
    for j in range(3):
        user = int(input("what number do you want to add? "))
        second_list.append(user)
    number_list.append(second_list)
print(number_list)

for a in range(3):
    for b in range(3):
        print(number_list[a][b],end=" ")
    print()