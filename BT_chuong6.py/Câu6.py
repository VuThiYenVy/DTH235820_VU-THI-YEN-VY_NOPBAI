import random

print ("Nhập số phần tử n:")
n=int(input())
if n>100:
    print("Không thể tạo list")
else:
    lst=random.sample(range(100),n)
    print("List có {n} só ngẫu nhiên không trùng nhau là:")
    print(lst)