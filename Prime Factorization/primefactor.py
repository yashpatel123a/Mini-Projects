def prime_factor(number):
    prime = []
    while number % 2 ==0:
        number = number / 2
        prime.append(2)
    for i in range(3,int(number**0.5) + 1,2):
        while number % i == 0:
            number = number / i
            prime.append(i)
    if number > 2:
        prime.append(int(number))
    return list(set(prime))

if __name__ == '__main__':
    number = int(input('Enter a number : '))
    print(prime_factor(number))
