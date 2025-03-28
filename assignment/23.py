a=1
b=1
sum = a+b
print(a,b, end=" ")
for i in range (3,21):
    c = a+b
    print(c, end=" ")
    sum = sum +c
    a =b
    b =c
print("총합계",sum)