from random import randint
import os
class tic_tac_toe:

    def __init__(self):
        self.board=[' ']*10

    def display_board(self):
        try:
	        os.system('cls')
        except:
            os.system('clear')
        print('\n')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + ' ' )
        print(' --------- ')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + ' ' )
        print(' --------- ')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3] + ' ' )
        print('\n')

    def player_input(self):
        marker=' '
        while (marker!='X' and marker!='O'):
            marker=input("player1 choose 'X' or 'O':").upper()
        if (marker=='X'):
            return ('X','O')
        else:
            return ('O','X')

    def place_marker(self,marker,position):
        self.board[position]=marker

    def win_check(self,mark):
        return ((self.board[1]==self.board[2]==self.board[3]==mark) or
                (self.board[4]==self.board[5]==self.board[6]==mark) or
                (self.board[7]==self.board[8]==self.board[9]==mark) or
                (self.board[1]==self.board[4]==self.board[7]==mark) or
                (self.board[2]==self.board[5]==self.board[8]==mark) or
                (self.board[3]==self.board[6]==self.board[9]==mark) or
                (self.board[1]==self.board[5]==self.board[9]==mark) or
                (self.board[3]==self.board[5]==self.board[7]==mark))

    def choose_first(self):
        if randint(0,1)==0:
            return 'Player1'
        else:
            return 'Player2'

    def space_check(self,position):
        return self.board[position]==' '

    def full_board_check(self):
        return  not ' ' in self.board[1:]

    def player_choice(self):
        position=0
        while position not in [1,2,3,4,5,6,7,8,9] or not  self.space_check(position):
            try:
                position=int(input('Please enter a number: '))
            except ValueError:
                continue
        return position

    def replay(self):
        choice=''
        while (choice!='Y' and choice!='N'):
            choice=input("play again?(Y/N): ").upper()
        return choice.upper()=='Y'

    def start(self):
        print('-----------------------------')
        print('Welcome to Tic Tac Toe game!')
        print('-----------------------------')
        player1_mark,player2_mark=self.player_input()
        player_turn=self.choose_first()
        print(player_turn + ' will go first')
        active_game=True

        while active_game:
            if (player_turn=='player1'):
                self.display_board()
                print(player_turn + ' will go with ' + player1_mark)
                player_position=self.player_choice()
                self.place_marker(player1_mark,player_position)
                if self.win_check(player1_mark):
                    self.display_board()
                    print('********************')
                    print('  PLAYER 1 HAS WON')
                    print('********************')
                    active_game=False
                else:
                    if self.full_board_check():
                        self.display_board()
                        print('****************')
                        print('    TIE GAME')
                        print('****************')
                        break
                    else:
                        player_turn='player2'
            else:
                self.display_board()
                print(player_turn + ' will go with ' + player2_mark)
                player_position=self.player_choice()
                self.place_marker(player2_mark,player_position)
                if self.win_check(player2_mark):
                    self.display_board()
                    print('******************')
                    print(' player 2 has won')
                    print('******************')
                    active_game=False
                else:
                    if self.full_board_check():
                        self.display_board()
                        print('****************')
                        print('    TIE GAME')
                        print('****************')
                        break
                    else:
                        player_turn='player1'


if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')
        ttt = tic_tac_toe()
        ttt.start()
        if not ttt.replay():
            break
    try:
        os.system('cls')
    except:
        os.system('clear')
        