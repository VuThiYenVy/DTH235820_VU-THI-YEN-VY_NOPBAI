def NhapDaySoTang(n):
    day=[]
    print("Nhập {n} tăng dần")
    for i in range(n):
        while True:
            try:
                x=int(input(f"Nhập số thứ {i+1}: "))
                if i==0 or x>day[-1]:
                    day.append(x)
                    break
                else:
                    print(f"Số phải lớn hơn {day[-1]}. Vui lòng nhập lại!")
            except ValueError:
                print("Vui lòng nhập số nguyên ")
    return day
n=int(input("Nhập số phần tử: "))
tang=NhapDaySoTang(n)
print("Dãy số tăng dần đã nhập là: ")
print(tang)


    
