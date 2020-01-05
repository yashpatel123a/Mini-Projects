def division(numerator,denominator,limit):
    value = ''
    temp = int(numerator/denominator)
    numerator = (numerator - (temp*denominator))*10
    value = value + str(temp) + '.'
    for _ in range(0,limit):
        temp = int(numerator/denominator)
        numerator = ((numerator) - (temp*denominator))*10
        value += str(temp)
    return value

if __name__ == '__main__':
    limit = int(input("Enter a number to generate π (pi) up to that many decimal places: "))
    print(division(245850922,78256779,limit)) 