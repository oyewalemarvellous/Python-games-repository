maths={"david","ezekiel","emmanuel","jake","luke"}
english={"luke","leon","drue","ezekiel"}
science={"luke","emmanuel","david","fion","micheal","leon"}
'''print(english.intersection(maths))
    print(maths.difference(english))
    print(maths.symmetric_difference(english))
    print(maths.union(english))'''
print((science.intersection(english)).intersection(maths))
student=((maths.union(english)).union(science))
print(maths.intersection(english).difference(science))
print("home work")
student2=(science & maths )|(english & science)|(english & maths)
student3=student-student2
print(student3)
'''print(english.intersection(science).difference(maths))'''
print(student2)