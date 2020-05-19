from tkinter import *
from tkinter import messagebox

class TicTacToe():
    def __init__(self, master):
        self.master = master
        self.playing = True
        self.game_board = [[], [], []]
        self.current_player = 'X'
        self.gui_interface()

    def game_button(self):
        b = Button(self.master, padx = 1, bg = "papaya whip", width = 3, text = "", font = ('arial', 60, 'bold'), relief = "sunken", bd=10)
        return b

    def click(self, row, col):
        self.game_board[row][col].config(text = self.current_player, state = "disabled")

    def gui_interface(self):
        for i in range(3):
            for j in range(3):
                self.game_board[i].append(self.game_button())
                self.game_board[i][j].config(command = lambda row = i, col = j: self.click(row, col))
                self.game_board[i][j].grid(row = i,column = j)

if __name__ == '__main__':
    root = Tk()
    root.title("Tic Tac Toe")
    ttt = TicTacToe(root)
    root.mainloop()
