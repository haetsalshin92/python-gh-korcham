a = int(input("정수1:"))
m = a
while a!= 0:
    if a<m:
        m = a
    a = int(input("정수2:"))
print("최소값 :",m)