a = [26,27,39,63,57,75,11,76,80,18]
key = int(input("키 :"))
cnt = 0
while cnt<10 :
    if key == a[cnt]:
        print(cnt, "에서 탐색 성공")
        break
    cnt = cnt + 1
if cnt ==10:
    print("탐색 실패")

print("====================================")
a=[11,18,26,27,39,57,63,75,76,80]
key = int(input("키 :"))
low = 0
high = 9
while low <= high:
    mid = (low+high)//2
    if key == a[mid]:
        print(mid, "에서 탐색 성공")
        break
    elif key < a[mid]:
        high = mid -1
    else:
        low = mid +1
if low > high :
    print("탐색 실패")