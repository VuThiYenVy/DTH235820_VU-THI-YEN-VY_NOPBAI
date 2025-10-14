lst = [3, 0, 1, 5, 2]
x = 2
def main():
    print("Câu a:",lst[0])
    print("Câu b:",lst[3])
    print("Câu c:",lst[x])
    print("Câu d:",lst[-x])
    print("Câu e:",lst[x+1])
    print("Câu f:",lst[x]+1)
    print("Câu g:",lst[lst[x]])
    print("Câu h:",lst[lst[lst[x]]])
main()

"""
Câu a: 3
Câu b: 5
Câu c: 1
Câu d: 5
Câu e: 5
Câu f: 2
Câu g: 0
Câu h: 3
"""