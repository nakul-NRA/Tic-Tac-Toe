import tkinter as tk
from tkinter import messagebox
import random


game = True
board = [[" " for row in range(3)] for col in range(3)]


def check_win(player):
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def player1_move(row, col):
    global game

    if board[row][col] == " " and game:
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")

        if check_win("X"):
            messagebox.showinfo("Game Over", "Player X wins !")
            game = False
        else:
            ct=0
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        ct+=1
            if ct == 0:
                messagebox.showinfo("Game Over", "It's a draw!")
                game = False
            else:
                player2_move()


def player2_move():
    global game
    if game:
        if next_move("O") != -1:
            x = next_move("O")
            row = x//3
            col = x%3
        elif next_move("X") != -1:
            x = next_move("X")
            row = x//3
            col = x%3
        else:
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if board[row][col] == " ":
                    break

        board[row][col] = "O"
        buttons[row][col].config(text="O", state="disabled")

        if check_win("O"):
            messagebox.showinfo("Game Over", "Player O wins!")
            game = False


def next_move(player):

    for row in range(3):
        if board[row][0]==" " and board[row][1]==board[row][2]==player:
            return 3*row
        if board[row][1]==" " and board[row][0]==board[row][2]==player:
            return 3*row+1
        if board[row][2]==" " and board[row][1]==board[row][0]==player:
            return 3*row+2
        
    for col in range(3):
        if board[0][col]==" " and board[1][col]==board[2][col]==player:
            return col
        if board[1][col]==" " and board[0][col]==board[2][col]==player:
            return 3+col
        if board[2][col]==" " and board[1][col]==board[0][col]==player:
            return 6+col
        
    if board[0][0]==" " and board[1][1]==board[2][2]==player:
        return 0
    if board[1][1]==" " and board[0][0]==board[2][2]==player:
        return 4
    if board[2][2]==" " and board[1][1]==board[0][0]==player:
        return 8
    
    if board[0][2]==" " and board[1][1]==board[2][0]==player:
        return 2
    if board[1][1]==" " and board[0][2]==board[2][0]==player:
        return 4
    if board[2][0]==" " and board[1][1]==board[0][2]==player:
        return 6

    return -1


def reset_game():
    global game, board

    game = True
    board = [[" " for row in range(3)] for col in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state="normal")


window = tk.Tk()
window.title("Tic Tac Toe")

buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=" ", width=10, height=5, command=lambda row=row, col=col: player1_move(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        button_row.append(button)
    buttons.append(button_row)

reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

window.mainloop()