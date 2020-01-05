def calc(num1,num2,operation):
    if operation not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'
    if operation == '+':
        return(str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 + num2))
    if operation == '-':
        return(str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 - num2))
    if operation == '*':
        return(str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 * num2))
    if operation == '/':
        if num2 == 0:
            return 'not divisable'
        else:
            return(str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 / num2))

if __name__ == '__main__':
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    operation = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')
    print(calc(a, b, operation))
    