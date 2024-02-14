def decimal_to_octal(number: int) -> str:
    octal = ''
    while number > 0:
        octal = str(number % 8) + octal
        number = number // 8
    return octal

n = int(input("input decimal number : "))
print(decimal_to_octal(n))