lst = [20, 1, -34, 40, -8, 60, 1, 3]
def main():
    print("Câu a:",lst)
    print("Câu b:",lst[0:3])
    print("Câu c:",lst[4:8])
    print("Câu d:",lst[4:33])
    print("Câu e:",lst[-5:-3])
    print("Câu f:",lst[-22:3])
    print("Câu g:",lst[4:])
    print("Câu h:",lst[:])
    print("Câu i:",lst[:4])
    print("Câu j:",lst[1:5])
    print("Câu k:",-34 in lst)
    print("Câu l:",-34 not in lst)
    print("Câu m:",len(lst))
main()
"""
Câu a: [20, 1, -34, 40, -8, 60, 1, 3]
Câu b: [20, 1, -34]
Câu c: [-8, 60, 1, 3]
Câu d: [-8, 60, 1, 3]
Câu e: [40, -8]
Câu f: [20, 1, -34]
Câu g: [-8, 60, 1, 3]
Câu h: [20, 1, -34, 40, -8, 60, 1, 3]
Câu i: [20, 1, -34, 40]
Câu j: [1, -34, 40, -8]
Câu k: True
Câu l: False
Câu m: 8
"""