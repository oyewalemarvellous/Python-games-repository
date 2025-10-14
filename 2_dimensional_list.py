list_1=[[1,2,3],[4,5,6],[7,8,9]]
list_2=[[1,2,3],[3,2,1],[4,1,3]]
for i in range(3):
    for j in range(3):
        print((list_1[i][j] + list_2[i][j]))
for g in range(3):
    print(list_1[g][g])
for h in range(3):
    print(list_1[h][0])
for l in range(3):
    for t in range(2):
        print(list_1[l][t],end=" ")
    print()
for u in range(3):
    for w in range(3):
        print(list_1[w][u],end=" ")
    print()
for c in range(0,3,1,):
    for y in range(2,-1,-1):
        print(list_1[c][y],end=" ")
    print()