a = int(input("정수:"))
b = int(input("정수:"))
c = int(input("정수:"))

if a<b:
    if a<c:
        print("가장 작은 수:",a)
    else:
        print("가장 작은 수:",c)
else:
    if b<c:
        print("가장 작은 수:",b)
    else:
        print("가장 작은 수:",c)