# recursive
def _factorial(num):
    if num < 0:
        raise ValueError("number must be positive.")
    if num == 0:
        return 1
    else:
        return num*_factorial(num - 1)

# iterative
def factorial(num):
    result = 1
    if num < 0:
        raise ValueError("number must be positive.")
    while num > 0:
        result *= num
        num -= 1
    return result

if __name__ == '__main__':
    num = int(input('Enter a number: '))
    print(f"{factorial(num)}")
    