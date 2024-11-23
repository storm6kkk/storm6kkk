def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 5  # 可以根据需要修改n的值
print(f"{n}! = {factorial(n)}")
