def cubesum(num):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total


def isArmstrong(num):
    return num == cubesum(num)


def PrintArmstrong():
    print("Armstrong numbers between 1 and 1000:")
    for i in range(1, 1001):
        if isArmstrong(i):
            print(i)

