from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

board = [""] * 9
player = "X"

def check_winner():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            status.config(text=f"{board[a]} Wins!")
            disable_buttons()
            return

    if "" not in board:
        status.config(text="Draw!")

def disable_buttons():
    for btn in buttons:
        btn.config(state=DISABLED)

def click(pos):
    global player

    if board[pos] == "":
        board[pos] = player
        buttons[pos].config(text=player)

        check_winner()

        if player == "X":
            player = "O"
        else:
            player = "X"

buttons = []

for i in range(9):
    btn = Button(
        root,
        text="",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status = Label(root, text="Player X Turn", font=("Arial", 14))
status.grid(row=3, column=0, columnspan=3)

root.mainloop()