def mortgage_calculator(P,r,N):
    if r == 0:
        return P / N
    else:
        return ((r * P) / (1 - (1 + r)**-N))

if __name__ == '__main__':
    P = float(input('Enter the amount borrowed: '))
    R = float(input('Enter the interest rate: '))
    N = int(input("Enter the number of monthly payments: "))
    r = R / (12*100)
    print(f'Your fixed monthly payment equal to {round(mortgage_calculator(P,r,N),2)} per month.')

