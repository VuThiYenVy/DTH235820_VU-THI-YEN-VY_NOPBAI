def Nhap():
    while True:
        try:
            str=input("Nhập dãy số thực cách nhau bởi dấu ,: ")
            n=[float(x) for x in str.split(',')]
            return n
        except ValueError:
            print("Vui lòng nhập số thực. Nhập lại!")
def SxGiam(n):
    return sorted(n,reverse=True)
n=Nhap()
giam=SxGiam(n)
print("Sau khi sx day so thuc giam: ")
print(giam)