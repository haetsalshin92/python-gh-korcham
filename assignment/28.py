lang = []
lang.append("파이썬")
lang.append("C언어")
lang.append("자바")
print(lang)
print(lang[0])



print("===================================")

a=[]
for i in range(1,11):
    a.append(i)
print(a)

print("===================================")

a=[]
for i in range(10, 101,10):
    a.append(i)
for i in range(9,-1,-1):
    print(a[i],end=" ")

print("===================================")
a = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,5):
    temp = a[i]
    a[i] = a[9-i]
    a[9-i] = temp
print(a)

print("===================================")
a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(0,10):
    b.append(a[9-i])
print("b:",b)


print("===================================")

