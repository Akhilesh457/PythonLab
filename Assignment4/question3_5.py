#Question 3
result1 = 10 + 5 * 2     # Output: 20
result2 = (10 + 5) * 2  # Output: 30
#Question 4
num = int(input("Enter a decimal number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))
#Question 5
def square_list():
    squares = []
    for i in range(1, 31):
        squares.append(i ** 2)
    print(squares)

square_list()