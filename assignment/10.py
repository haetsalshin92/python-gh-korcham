money=1000
km=int(input("거리 :"))
if km<5:
    print("요금:",money)
elif 5<=km<10:
    print("요금:",money*2)
else:
    print("요금:",money*3)