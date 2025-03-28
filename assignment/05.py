m = int(input("분 단위의 시간 :"))
h = m//60
d = h//24
h = h%24
m = m%60
print(d,"일",h,"시간",m,"분")