if __name__ == "__main__":
    num = int(input())
    b = 0
    while num>0:
        b+=num%10
        num //= 10
        if num == 0 and b>9:
            num = b
            b = 0
        elif b<10 and num == 0:break
    print(b)