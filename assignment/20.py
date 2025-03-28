n=int(input("정수:"))
count=0
for i in range (1, n+1):
    if n%i == 0:
        count = count +1
        print(i, end=" ")
print("약수 총 갯수:",count)