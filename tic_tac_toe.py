import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Create buttons for the game board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        """Handle a player's move."""
        if self.board[row][col] == "" and not self.check_winner():
            # Update the board and button
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for a winner or draw
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                # Switch the player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check if the current player has won."""
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def check_draw(self):
        """Check if the game is a draw."""
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        """Reset the game board for a new game."""
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
