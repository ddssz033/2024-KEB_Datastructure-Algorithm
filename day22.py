def fibo_recursion(number : int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)

n = int(input("input number : "))
for i in range(0, n):
    print(i)
    print(fibo_recursion(i))