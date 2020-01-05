from random import randint
class rps:

    def __init__(self):
        self.choice = 0
    
    def revel(self,random_number):
        rps_list = {'1':'Rock','2':'Paper','3':'Scissor'}
        return 'player = ' + rps_list[str(self.choice)] + '\nMachine = ' + rps_list[str(random_number)]

    def choose(self):
        while not (self.choice == 1 or self.choice == 2 or self.choice == 3):
            try:
                self.choice = int(input('Enter your choice:\n1 - Rock\n2 - Paper\n3 - Scissor: '))
            except:
                continue
        
    def compare(self,random_number):
        if random_number == 1:
            return self.choice == 2
        elif random_number == 2:
            return self.choice == 3
        elif random_number == 3:
            return self.choice == 1
    
    def start(self):
        random_number = randint(1,3)
        self.choose()
        print(self.revel(random_number))
        if self.choice == random_number:
            print("Tie")
        elif self.compare(random_number):
            print("Player Won")
        else:
            print('Machine Won')

if __name__ == '__main__':
    rps_game = rps()
    rps_game.start()
