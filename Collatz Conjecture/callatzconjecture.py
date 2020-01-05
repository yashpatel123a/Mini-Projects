def collatzconjecture(number):
    step = 0
    while number!=1 and number > 0:
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        step += 1
    return step

if __name__ == '__main__':
    number = int(input('Enter the number: '))
    print(f'total {collatzconjecture(number)} steps required.')
    
