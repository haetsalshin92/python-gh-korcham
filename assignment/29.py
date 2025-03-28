a = [1,2,3,4,5,6,7,8,9,10]
temp = a[0]
for i in range(0,9):
    a[i] = a[i+1]
a[9]=temp
print(a)

print("===================================")
import random
a = []
for i in range(10):
    a.append(random.randint(1,100))
print(a)

m = a[0]
for i in range(1,10):
    if m<a[i]:
        m=a[i]
print("최댓값:",m)