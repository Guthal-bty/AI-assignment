import tkinter as tk
import math

board = [""] * 9

root = tk.Tk()
root.title("Tic Tac Toe AI")

buttons = []


def winner(player):

    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def minimax(is_max):

    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if "" not in board:
        return 0

    if is_max:

        best = -math.inf

        for i in range(9):

            if board[i] == "":

                board[i] = "O"

                best = max(
                    best,
                    minimax(False)
                )

                board[i] = ""

        return best

    else:

        best = math.inf

        for i in range(9):

            if board[i] == "":

                board[i] = "X"

                best = min(
                    best,
                    minimax(True)
                )

                board[i] = ""

        return best


def ai_move():

    best_score = -math.inf
    move = None

    for i in range(9):

        if board[i] == "":

            board[i] = "O"

            score = minimax(False)

            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        buttons[move]["text"] = "O"


def click(pos):

    if board[pos] != "":
        return

    board[pos] = "X"
    buttons[pos]["text"] = "X"

    if winner("X"):
        status.config(text="You Win!")
        return

    ai_move()

    if winner("O"):
        status.config(text="AI Wins!")
        return


for i in range(9):

    btn = tk.Button(
        root,
        text="",
        width=8,
        height=4,
        command=lambda i=i: click(i)
    )

    btn.grid(
        row=i//3,
        column=i%3
    )

    buttons.append(btn)

status = tk.Label(
    root,
    text="Play!"
)

status.grid(
    row=4,
    column=0,
    columnspan=3
)

root.mainloop()