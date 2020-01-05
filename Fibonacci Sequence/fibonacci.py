def fibonacci(limit):
    a = 1
    b = 1
    answer = []
    answer.append(a)
    answer.append(b)
    for _ in range(limit-2):
        a,b = a+b,a
        answer.append(a)
    return answer

if __name__ == '__main__':
    limit = int(input('Enter a limit of fibonacci series: '))
    print(fibonacci(limit))

    