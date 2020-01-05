import re
print('Welcome to Calculator')
print("e - Exit\nr - reset")
previous = None
run = True

def performMath():
    global run,previous
    equation = ''
    if previous == None:
        equation = input('Enter euqation:')
    else:
        equation = input(str(previous))
    if equation == 'r':
        previous = None
        pass
    elif equation == 'e':
        print('Good Bye.')
        run = False
    else:
        equation = re.sub('[^0-9+-/*%()]','',equation)
        try:
            if previous == None:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)
        except:
            print('Its not a valid equation.')
            previous = None

while run:
    performMath()
