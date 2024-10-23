from tkinter import *
import random

# Function to handle the logic when a player clicks a button (takes a turn)
def next_turn(row, column):
    global first_player
    
    # If the clicked button is empty and no winner is determined yet
    if buttons[row][column]['text'] == ' ' and check_winner() == False:
        # Set the button text to the current player's symbol (X or O)
        buttons[row][column]["text"] = first_player

        # Check if a winner exists after the move
        if check_winner() is False:
            # Switch turns: if current player is X, change to O, otherwise switch to X
            first_player = players[1] if first_player == players[0] else players[0]
            # Update the label to display whose turn it is
            label.config(text=str(first_player) + " turn")
        # If a winner is found, update the label to show the winner
        elif check_winner() is True:
            label.config(text=str(first_player) + " wins!")
        # If there's a tie, display 'Tie' on the label
        elif check_winner() == 'Tie':
            label.config(text='Tie')

# Function to check if there is a winner or a tie
def check_winner():
    # Check rows for a winner
    for row in range(3):
        # If all 3 buttons in a row are the same and not empty, it's a win
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != ' ':
            # Highlight the winning row in blue
            buttons[row][0].config(bg='blue')
            buttons[row][1].config(bg='blue')
            buttons[row][2].config(bg='blue')
            return True

    # Check columns for a winner
    for column in range(3):
        # If all 3 buttons in a column are the same and not empty, it's a win
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != ' ':
            # Highlight the winning column in blue
            buttons[0][column].config(bg='blue')
            buttons[1][column].config(bg='blue')
            buttons[2][column].config(bg='blue')
            return True

    # Check diagonals for a winner
    # Top-left to bottom-right diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ':
        # Highlight the winning diagonal in blue
        buttons[0][0].config(bg='blue')
        buttons[1][1].config(bg='blue')
        buttons[2][2].config(bg='blue')
        return True

    # Top-right to bottom-left diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' ':
        # Highlight the winning diagonal in blue
        buttons[0][2].config(bg='blue')
        buttons[1][1].config(bg='blue')
        buttons[2][0].config(bg='blue')
        return True

    # If no spaces are left and no winner, it's a tie
    elif check_empty() is False:
        # Highlight all buttons in red to indicate a tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='red')
        return 'Tie'

    # No winner or tie, game continues
    else:
        return False

# Function to check if there are empty spaces on the board
def check_empty():
    space = 9  # Total 9 buttons
    # Loop through all buttons to count empty spaces
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != ' ':
                space -= 1
    # Return True if there are empty spaces left, otherwise False
    return space != 0

# Function to reset the game for a new round
def new_game():
    global first_player
    # Randomly select which player goes first (X or O)
    first_player = random.choice(players)
    # Update label to indicate whose turn it is
    label.config(text=str(first_player) + ' turn')
    # Reset all buttons to empty and default color
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text=' ', bg='#f0f0f0')

# Create the main window for the game
window = Tk()
window.title('Tic Tac Toe')

# Define the two players, X and O
players = ['X', 'O']
# Randomly pick who will start the game
first_player = random.choice(players)

# Initialize the buttons (3x3 grid) with empty spaces
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
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
        # Each button calls the next_turn function when clicked
        buttons[row][column] = Button(frame, text=' ', font=('consolas', 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the Tkinter event loop (game window)
window.mainloop()
