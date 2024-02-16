# 동적 프로그래밍을 사용한 피보나치 수열 계산
def fibonacci_dynamic(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n], n + 1

# 재귀를 사용한 피보나치 수열 계산
def fibonacci_recursive(n):
    if n <= 1:
        return n, 1
    else:
        fib_1, count_1 = fibonacci_recursive(n - 1)
        fib_2, count_2 = fibonacci_recursive(n - 2)
        return fib_1 + fib_2, count_1 + count_2 + 1

# 각 방법의 결과 및 연산 횟수 비교
n = 30
fib_dynamic, count_dynamic = fibonacci_dynamic(n)
fib_recursive, count_recursive = fibonacci_recursive(n)

print("동적 프로그래밍 결과:", fib_dynamic)
print("동적 프로그래밍 연산 횟수:", count_dynamic)
print("재귀 결과:", fib_recursive)
print("재귀 연산 횟수:", count_recursive)
