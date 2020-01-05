from random import randint

class Guess_Game:

    def __init__(self,maximum):
        self.maximum = maximum
        self.choice = -1
        self.attempt = 0
        
    def choose(self):
        self.choice = -1
        while not 0 <= self.choice <= self.maximum: 
            try:
                self.choice = int(input(f"Enter a number in the range of 0 to {self.maximum}:"))
            except:
                print("Please enter a number.")
                continue
        self.attempt += 1

    def compare(self,random_number):
        return random_number == self.choice

    def start(self):
        random_number = randint(0,self.maximum)
        self.choose()
        while not self.compare(random_number):
            if self.choice > random_number:
                print('Go Down')
            else:
                print('Go Up')
            self.choose()
        print('\n****************************')
        print(f'You got it.')
        print(f'Total attempt = {self.attempt}')  
        print('****************************')

    def replay(self):
        rep = ''
        while (rep != 'Y' and rep != 'N'):
            rep = input("play again?(Y/N): ").upper()
        return rep.upper() == 'Y' 


if __name__ == '__main__':        
    while True:
        while True: 
            try:
                maxima = int(input("Enter a maximum range you want to guess: "))
            except:
                print("Please enter a number.")
            else:
                break
        guessgame = Guess_Game(maxima)
        guessgame.start() 
        if not guessgame.replay():
            break
        