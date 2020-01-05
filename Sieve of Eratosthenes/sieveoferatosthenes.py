def SieveOfEratosthenes(n):
    primes  = [True]*(n+1)
    p = 2
    while(p*p <= n):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False
        p +=1

    for p in range(2,n):
        if primes[p]:
            print(p,end = ' ')

if __name__ == '__main__':
    num  = int(input('Enter a number: '))
    SieveOfEratosthenes(num)
    