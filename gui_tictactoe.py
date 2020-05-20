from tkinter import *
from tkinter.messagebox import *
from tkinter import simpledialog

class TicTacToe():
    def __init__(self, master):
        self.master = master
        self.game_board = [[], [], []]
        self.current_player = 'X'
        self.answer = True
        self.player1_name = 'NULL'
        self.player2_name = 'NONE'
        self.bottom_label = ''
        self.gui_interface()

    def game_button(self):
        b = Button(self.master, padx = 1, bg = "navajo white", width = 3, text = "", font = ('arial', 60, 'bold'), relief = "sunken", bd=10)
        return b

    def click(self, row, col):
        if self.answer:
            pass
        else:
            self.game_board[row][col].config(text = self.current_player, state = "disabled")
            if self.current_player == 'X':
                self.current_player = 'O'
                self.bottom_label.config(text = "{}'s Chance".format(self.player2_name))
            else:
                self.current_player = 'X'
                self.bottom_label.config(text = "{}'s Chance".format(self.player1_name))
            self.play_game()

    def initial_gui(self):
        self.answer = askyesno("Welcome", "Do you want to play the game as Single Player ?")
        if self.answer == True:
            self.player1_name = simpledialog.askstring("Player", "Please, Enter Your Name")
            self.player2_name = 'Computer'
        else:
            self.player1_name = simpledialog.askstring("Player 1(X)", "Please, Enter Your Name")
            self.player2_name = simpledialog.askstring("Player 2(O)", "Please, Enter Your Name")

    def gui_interface(self):
        for i in range(3):
            for j in range(3):
                self.game_board[i].append(self.game_button())
                self.game_board[i][j].config(command = lambda row = i, col = j: self.click(row, col))
                self.game_board[i][j].grid(row = i,column = j)
        self.initial_gui()
        label = Label(self.master, text = "{}'s Chance".format(self.player1_name), font = ('arial', 20, 'bold'))
        label.grid(row = 3, column = 0, columnspan = 3)
        self.bottom_label = label

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
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.game_board[i][j]["text"] = ""
                self.game_board[i][j]["state"] = "normal"       

    def play_game(self):
        if(self.check_win()):
            if(self.current_player == 'X'):
                print(showinfo("showinfo", "{} is Winner".format(self.player1_name)))
            else:
                print(showinfo("showinfo", "{} is Winner".format(self.player2_name)))
            self.reset()
        elif(self.check_draw()):
            print(showinfo("showinfo", "Game Drawn"))
            self.reset()

if __name__ == '__main__':
    root = Tk()
    root.title("Tic Tac Toe")
    ttt = TicTacToe(root)
    root.mainloop()
