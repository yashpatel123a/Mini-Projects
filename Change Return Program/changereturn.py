def change_return(amount,currency):
    currency.sort(reverse = True)
    counter = 0
    amount_counter = [0]*len(currency)
    while amount> 0:
        amount_counter[counter] = int(amount/currency[counter])
        amount -= amount_counter[counter]*currency[counter]
        counter += 1
    return [(currency[i],amount_counter[i]) for i in range(len(currency))]

if __name__ == '__main__':
    currency = [1,5,10,25]
    currency_name = ['quarter','dime','nickel','pennies']
    amount = int(input('Enter a amount: '))
    change = change_return(amount,currency)
    for i in range(len(currency)-1,-1,-1):
        print(currency_name[i] + f'({change[i][0]}) - {change[i][1]}')




