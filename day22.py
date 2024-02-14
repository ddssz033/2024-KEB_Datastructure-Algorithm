def decimal_to_octal(number: int) -> str:
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(n//8) + str(n % 8)

n = int(input("input decimal number : "))
print(decimal_to_octal(n))