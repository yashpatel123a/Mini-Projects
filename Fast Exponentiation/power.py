def power(a,b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    half_pow = power(a,int(b/2))
    if b % 2 == 0:
        return half_pow * half_pow
    else:
        if b > 0:
            return a * half_pow * half_pow
        else:
            return (half_pow * half_pow) / a

if __name__ == '__main__':
    a = int(input('Enter a base: '))
    b = int(input('Enter a power: '))
    print(f'{power(a,b)}')