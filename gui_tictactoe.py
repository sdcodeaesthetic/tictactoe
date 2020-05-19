from tkinter import *
from tkinter.messagebox import *

class TicTacToe():
    def __init__(self, master):
        self.master = master
        self.game_board = [[], [], []]
        self.current_player = 'X'
        self.gui_interface()

    def game_button(self):
        b = Button(self.master, padx = 1, bg = "papaya whip", width = 3, text = "", font = ('arial', 60, 'bold'), relief = "sunken", bd=10)
        return b

    def click(self, row, col):
        self.game_board[row][col].config(text = self.current_player, state = "disabled")
        self.play_game()
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def gui_interface(self):
        for i in range(3):
            for j in range(3):
                self.game_board[i].append(self.game_button())
                self.game_board[i][j].config(command = lambda row = i, col = j: self.click(row, col))
                self.game_board[i][j].grid(row = i,column = j)

    def check_row(self):
        r1 = self.game_board[0][0]["text"] == self.game_board[0][1]["text"] == self.game_board[0][2]["text"] != ''
        r2 = self.game_board[1][0]["text"] == self.game_board[1][1]["text"] == self.game_board[1][2]["text"] != ''
        r3 = self.game_board[2][0]["text"] == self.game_board[2][1]["text"] == self.game_board[2][2]["text"] != ''
        if(r1 or r2 or r3):
            return True
        else:
            return False

    def check_col(self):
        c1 = self.game_board[0][0]["text"] == self.game_board[1][0]["text"] == self.game_board[2][0]["text"] != ''
        c2 = self.game_board[0][1]["text"] == self.game_board[1][1]["text"] == self.game_board[2][1]["text"] != ''
        c3 = self.game_board[0][2]["text"] == self.game_board[1][2]["text"] == self.game_board[2][2]["text"] != ''
        if(c1 or c2 or c3):
            return True
        else:
            return False

    def check_diag(self):
        d1 = self.game_board[0][0]["text"] == self.game_board[1][1]["text"] == self.game_board[2][2]["text"] != ''
        d2 = self.game_board[0][2]["text"] == self.game_board[1][1]["text"] == self.game_board[2][0]["text"] != ''
        if(d1 or d2):
            return True
        else:
            return False

    def check_win(self):
        if(self.check_row() or self.check_col() or self.check_diag()):
            return True
        else:
            return False

    def check_draw(self):
        flag = 1
        for i in range(3):
            for j in range(3):
                if(self.game_board[i][j]["text"] == ""):
                    flag = 0
                    break
        if(flag == 0):
            return False
        else:
            return True

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.game_board[i][j]["text"] = ""
                self.game_board[i][j]["state"] = "normal"
        self.current_player = 'X'        

    def play_game(self):
        if(self.check_win()):
            print(showinfo("showinfo", "{}'s is Winner".format(self.current_player)))
            self.reset()
        elif(self.check_draw()):
            print(showinfo("showinfo", "Game Drawn"))
            self.reset()

if __name__ == '__main__':
    root = Tk()
    root.title("Tic Tac Toe")
    ttt = TicTacToe(root)
    root.mainloop()
