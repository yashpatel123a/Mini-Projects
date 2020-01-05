def isprime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if (number%2 == 0 or number%3 == 0):
        return False
    i = 5
    while i*i <= number:
        if (number%i == 0 or number%(i + 2) == 0):
            return False
        i += 6
    return True

if __name__ == '__main__':
    number = 2
    while True:
        choice = input('Enter your choice for find next prime number(y/n):')
        if choice.lower() == 'y':
            while not isprime(number):
                number += 1
                pass
            print(f'{number} ')
            number += 1
        elif choice.lower() == 'n':
            break
        else:
            print("Please enter a valid choice.")
    