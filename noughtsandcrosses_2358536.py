import random
import os.path
import json
random.seed()

def draw_board(board):
    
    '''developing a  code to draw the board'''

    print(" ----------- ")
    print("| {} | {} | {} | ".format(board[0][0], board[0][1], board[0][2]))
    print(" ----------- ")
    print("| {} | {} | {} | ".format(board[1][0], board[1][1], board[1][2]))
    print(" ----------- ")
    print("| {} | {} | {} | ".format(board[2][0], board[2][1], board[2][2]))
    print(" ----------- ")


    

def welcome(board):

    ''' printing welcome message to the user'''

    print("Welcome to the “Unbeatable Noughts and Crosses” game. ")
    print("The board layout is shown below: ")

    '''calling thr function draw_board(board) in order to display the board'''

    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want. ")
    
    

def initialise_board(board):

    '''initialising the board and
    writing a code to set or change all of the
    elements of the board to one space ' '. '''

    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


    '''this functions aks for players move'''
def get_player_move(board):
        while True:
            try:          
                a= ("""1 2 3
                   4 5 6
                   7 8 9""")
                #print(x)
                cell = int(input(f"Choose your square:{a}: ", ))
                row, col = (cell-1)//3, (cell-1) % 3
                if board[row][col] == ' ':
                    board[row][col] = 'X'

                    '''returing the row and column '''
                    return row, col
                else:
                    print("Cell is already occupied. Try again.")

                    '''incases of exceptions,error message are printed '''
            except ValueError:
                print("Invalid input. Try again.")
            except IndexError:
                print("Invalid cell number. Try again.")
        
    
    
'''this fuction gives the move of the computer
the computer puts a nought 
by importing random function  after that it returns the row and col'''
def choose_computer_move(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

    
'''this code is used to check if either the player or the computer has won
it returns True if someone has won, if not then it returns False'''

def check_for_win(board, mark):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark or \
       board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False



'''this function is used to check if all of the cells are occupuied
this also checks for draw
it return True if it is, False otherwise'''

def check_for_draw(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


'''this function is used to call various functions
and to develop code to play the game'''    
        
def play_game(board):
    ''' a call to the initialise_board(board) function  is given in order to set
    the board cells to all single spaces ' '.'''
    
    initialise_board(board)
    
    '''the board is then drawn with the help of draw_board(board) function'''
    draw_board(board)

    
    mark = 'X'

    '''this is used in loop to get the player move, update and draw the board
    to check if the player has won  check_for_win(board, mark) function is called,
    if the player has won, return 1 for the score
    if the player has not won check for a draw by calling check_for_draw(board)
    if drawn, return 0 for the score
    if not, then call choose_computer_move(board)
    to choose a move for the computer
    update and draw the board'''


    
    while True:
        if mark == 'X':
            print("Player's turn: ")
            get_player_move(board)
            draw_board(board)
            if check_for_win(board, mark):
                print("Player wins!")
                return 1
            if check_for_draw(board):
                print("Draw!")
                return 0
            mark = 'O'


            '''to check if the computer has won by  check_for_win(board, mark) function is called,
     if the computer has won  -1 is return for the score
     if the computer has not won then check_for_draw(board) function is called in order to check for a draw
     if there is a draw then 0 is returned for the score'''


        else:
            print("Computer's turn: ")
            choose_computer_move(board)
            draw_board(board)
            if check_for_win(board, mark):
                print("Computer wins!")
                return -1
            if check_for_draw(board):
                print("Draw!")
                return 0
            mark = 'X'

                    
                
def menu():
    print("Enter one of the following options: ")
    print("        1 - Play the game ")
    print("        2 - Save your score in the leaderboard")
    print("        3 - Load and display the leaderboard")
    print("        q - End the program")
    
    
    '''get user input of either '1', '2', '3' or 'q' is asked
    
    1 - Play the game
    2 - Saves score in file 'leaderboard_2358536.txt'
    3 - Load and display the scores from the 'leaderboard_2358536.txt'
    q - End the program'''

    choice= input("1, 2, 3 or q ? " )
    while choice not in ['1', '2', '3', 'q']:
        choice = input(
            "Invalid option, enter '1' to play the game, '2' to save score, '3' to display leaderboard or 'q' to quit: ")
    return choice



''' in this function a code has been developed to load the leaderboard scores from the file leaderboard.txt
and to return the scores in a Python dictionary 
with the player names as key and the scores as values using JSON
if not then it returns the dictionary in leaders '''
    

def load_scores():
    if os.path.exists("leaderboard_2358536.txt"):
        with open("leaderboard_2358536.txt", "r") as f:
            leaders = json.load(f)
    else:
        leaders = {}
    return leaders
    


''' a code has been developed to ask the player for their name
    and then the function saves the current score to the file 'leaderboard_2358536.txt' '''

    
def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open("leaderboard_2358536.txt", "w") as f:
        json.dump(leaders, f)
    print(f"{name}'s score of {score} has been saved to the leaderboard.")

    return



'''this function displays the leaderboard scores
and passed in the Python dictionary parameter leader '''

def display_leaderboard(leaders):

    print("\nLEADERBOARD:")
    print("-------------")
    for i, (player, score) in enumerate(sorted(leaders.items(), key=lambda x: x[1], reverse=True), start=1):
        print(f"{i}. {player}: {score}")
    print("\n")


