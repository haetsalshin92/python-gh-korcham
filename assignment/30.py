import random
a = []
for i in range(10):
    a.append(random.randint(1,100))
print(a)

m = a[0]
for i in range(1,10):
    if m>a[i]:
        m=a[i]
print("최소값:",m)


print("===================================")
a=[]
for i in range(1,102):
    a.append(0)
for i in range(2,101):
    if a[i]==0:
        for j in range(i*2, 101, i):
            a[j]=1
for i in range(2,101):
    if a[i]==0:
        print(i, end=" ")

print("===================================")
b=[]
n = int(input("10진수: "))
while n!=0:
    b.append(n%2)
    n=n//2
for i in range(len(b)-1, -1,-1):
    print(b[i], end=" ")

print("===================================")
