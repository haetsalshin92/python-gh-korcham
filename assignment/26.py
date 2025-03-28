for i in range(1,11):
    print(i, "약수:", end=" ")
    for j in range (1, i+1):
        if i%j == 0:
            print(j, end=" ")
    print()

print("=================================")
for i in range(2, 101):
    chk = 1
    for j in range(2, i):
        if i%j ==0:
            chk = 0
            break
    if chk ==1:
        print(i, end=" ")

print("=================================")
n =0
sum =0
for i in range (1,11):
    n = n+i
    sum = sum+n
print(sum)

print("=================================")
