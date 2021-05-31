cha = input("Please enter a character:")
if len(cha)>7:
    cal = slice(len(cha)//2-1, len(cha)//2+2)
    print(cha[cal])