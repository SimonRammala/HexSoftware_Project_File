from tkinter import *
import random

def next_turn(row=None, column=None):
    global first_player, computer

    # If it's the player's turn (human)
    if first_player != computer:
        # If the clicked button is empty and no winner is determined yet
        if buttons[row][column]['text'] == ' ' and check_winner() == False:
            buttons[row][column]["text"] = first_player
            if check_winner() is False:
                first_player = computer  # Switch to the computer's turn
                label.config(text="Computer's turn")
                window.after(500, computer_move)  # Wait 500ms before the computer moves
            elif check_winner() is True:
                label.config(text=str(first_player) + " wins!")
            elif check_winner() == 'Tie':
                label.config(text='Tie')

def computer_move():
    global first_player, computer
    
    if check_winner() is False:
        row, column = random_move()
        buttons[row][column]["text"] = computer
        if check_winner() is False:
            first_player = players[0]  # Switch to the human's turn
            label.config(text="Your turn")
        elif check_winner() is True:
            label.config(text=str(computer) + " wins!")
        elif check_winner() == 'Tie':
            label.config(text='Tie')

def random_move():
    available_moves = [(row, col) for row in range(3) for col in range(3) if buttons[row][col]['text'] == ' ']
    return random.choice(available_moves)

# Function to check if there is a winner or a tie
def check_winner():
    # Check rows, columns, and diagonals for a winner
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != ' ':
            buttons[row][0].config(bg='blue')
            buttons[row][1].config(bg='blue')
            buttons[row][2].config(bg='blue')
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != ' ':
            buttons[0][column].config(bg='blue')
            buttons[1][column].config(bg='blue')
            buttons[2][column].config(bg='blue')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ':
        buttons[0][0].config(bg='blue')
        buttons[1][1].config(bg='blue')
        buttons[2][2].config(bg='blue')
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' ':
        buttons[0][2].config(bg='blue')
        buttons[1][1].config(bg='blue')
        buttons[2][0].config(bg='blue')
        return True

    # If no spaces are left and no winner, it's a tie
    if check_empty() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='red')
        return 'Tie'

    return False

# Function to check if there are empty spaces on the board
def check_empty():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == ' ':
                return True
    return False

# Function to reset the game for a new round
def new_game():
    global first_player
    first_player = random.choice(players)
    label.config(text=str(first_player) + ' turn' if first_player != computer else "Computer's turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text=' ', bg='#f0f0f0')

    if first_player == computer:
        window.after(500, computer_move)

# Create the main window for the game
window = Tk()
window.title('Tic Tac Toe')

# Define the two players, X and O
players = ['X', 'O']
first_player = random.choice(players)
 
if first_player == 'X':
    computer = 'O'
else:
    'X'  # Assign computer the opposite symbol

# Initialize the buttons (3x3 grid) with empty spaces
buttons = [
    [None, None, None], 
    [None, None, None], 
    [None, None, None]
]


# Label to display the current player's turn
label = Label(text=str(first_player) + ' turn', font=('consolas', 40))
label.pack(side='top')

# Restart button to start a new game
restart_button = Button(text='Restart', font=('consolas', 20), command=new_game)
restart_button.pack(side='top')

# Create a frame to hold the Tic Tac Toe grid
frame = Frame(window)
frame.pack()

# Create the 3x3 grid of buttons for the game board
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text=' ', font=('consolas', 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the Tkinter event loop (game window)
window.mainloop()
