def b2d(number):
    decimal_number = 0
    i = 0
    while number > 0:
        decimal_number += number % 10*(2**i)
        number = int(number / 10)
        i += 1
    return decimal_number

def d2b(number):
    binary_number = 0
    i = 0
    while number > 0:
         binary_number += number % 2*(10**i)
         number = int(number / 2)
         i += 1
    return binary_number


if __name__ == '__main__':
    choice = ''
    while not (choice == '1' or choice == '2'):
        choice = input("1 - decimal to binary\n2 - binary to decimal\nEnter your choice : ")
        if choice == '1':
            decimal_number = int(input('Enter a decimal number: '))
            print(f'your binary conversion is {d2b(decimal_number)}')
        elif choice == '2':
            binary_number = int(input('Enter a binary number: '))
            print(f'your deciml conversion is {b2d(binary_number)}')
        else:
            print('Enter a valid choice.')


