import time

from Tkinter import *
import tkMessageBox

from engine import *
from minimax import *


class Application:

    """GUI of the game."""

    def __init__(self):
        """Initialize the window and the GUI elements."""

        self.window = Tk()
        self.window.title("MonOthello")
        self.window.wm_maxsize(width="460", height="520")
        self.window.wm_minsize(width="460", height="520")

        self.game = False
        self.show_valid_positions = False
        self.difficulty = 0
        self.mode = 1
        self.color_first_player = "B"
        self.white_image = PhotoImage(file="white.gif")
        self.black_image = PhotoImage(file="black.gif")
        self.empty_image = PhotoImage(file="empty.gif")
        self.valid_image = PhotoImage(file="valid.gif")

        self.create_elements()
        self.window.mainloop()

    def create_elements(self):
        self.create_menu()
        self.create_board()
        self.create_options()

    def create_menu(self):
        menu = Menu(self.window)

        game = Menu(menu, tearoff=0)
        game.add_command(label="New", command=self.create_game, underline=0)
        game.add_command(label="Quit", command=self.bye, underline=0)
        menu.add_cascade(label="Game", menu=game, underline=0)

        settings = Menu(menu, tearoff=0)
        settings.add_checkbutton(label="Show valid positions", 
                                 command=self.toggle_show_valid_positions,
                                 underline=0)

        first_player = Menu(settings, tearoff=0)
        first_player.add_radiobutton(label="Black",
                                     variable=self.color_first_player,
                                     command=lambda color="B": self.set_first_player(color),
                                     underline=0)

        first_player.add_radiobutton(label="White",
                                     variable=self.color_first_player,
                                     command=lambda color="W": self.set_first_player(color),
                                     underline=0)
        settings.add_cascade(label="First Player", menu=first_player, underline=0)        

        mode = Menu(settings, tearoff=0)
        mode.add_radiobutton(label="Human vs Human",
                             variable=self.mode,
                             command=lambda v=0: self.set_mode(v),
                             underline=0)
        mode.add_radiobutton(label="Human vs Computer",
                             variable=self.mode,
                             command=lambda v=1: self.set_mode(v),
                             underline=1)
        mode.add_radiobutton(label="Computer vs Human",
                             variable=self.mode,
                             command=lambda v=2: self.set_mode(v),
                             underline=9)
        settings.add_cascade(label="Mode", menu=mode, underline=0)

        difficulty = Menu(settings, tearoff=0)
        difficulty.add_radiobutton(label="Baby",
                                   variable=self.difficulty,
                                   command=lambda depth=0: self.set_difficulty(depth),
                                   underline=0)
        settings.add_cascade(label="Difficulty", menu=difficulty, underline=0)

        menu.add_cascade(label="Settings", menu=settings, underline=0)

        help = Menu(menu, tearoff=0)
        help.add_command(label="About", command=self.show_credits, underline=0)
        menu.add_cascade(label="Help", menu=help, underline=0)
        
        self.window.config(menu=menu)

    def create_board(self):
        self.score = Label(self.window)
        self.score.pack()
        self.board = dict()
        back = Frame(self.window)
        back.pack(fill=BOTH, expand=1)

        for row in range(8):
            frame = Frame(back)
            frame.pack(fill=BOTH, expand=1)
            for column in range(8):
                button = Button(frame,
                                state=DISABLED,
                                command=lambda position=(row, column): self.go(position))
                button["bg"] = "gray"
                button.pack(side=LEFT, fill=BOTH, expand=1, padx=0, pady=0)
                self.board.update( {(row, column): button} )

    def create_options(self):
        self.pass_turn = Button(self.window, text="Pass", 
                                state=DISABLED,
                                command=self.pass_turn)
        self.pass_turn.pack(side=RIGHT)
        self.status = Label(self.window)
        self.update_status("Welcome to MonOthello!")
        self.status.pack(side=LEFT)

    def create_game(self):
        """Instantiate a game from the engine module."""
        message="Are you sure you want to restart?"
        if self.game and \
           not tkMessageBox.askyesno(title="New", message=message):
                return
        if self.mode == 0:
            p1_mode = p2_mode = "H"
        elif self.mode == 1:
            p1_mode = "H"
            p2_mode = "C"
        else:
            p1_mode = "C"
            p2_mode = "H"
        self.game = Game(p1_color=self.color_first_player,
                         p1_mode=p1_mode, p2_mode=p2_mode,
                         difficulty=self.difficulty)
        self.game.start()
        if self.mode == 2:
            self.computer_play()
        self.update_board()
        message = "Let's play! Now it's the %s's turn." % self.game.turn.color
        self.update_status(message)
        print self.game

    def toggle_show_valid_positions(self):
        self.show_valid_positions = not self.show_valid_positions           
        if self.game:
            self.update_board()

    def set_mode(self, value):
        self.mode = value

    def set_first_player(self, color):
        self.color_first_player = color

    def set_difficulty(self, v):
        self.difficulty = v

    def pass_turn(self):
        """Pass the turn when it's not possible to play."""
        if not self.game:
            return
        self.game.change_turn()
        if self.game.turn.mode == "C":
            self.computer_play()
        message = "%s's turn." % self.game.turn.color
        self.update_status(message)

    def show_credits(self):
        message = "MonOthello\nv.: 1.0"
        tkMessageBox.showinfo(title="About", message=message)

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()

    def update_score(self):
        self.score["text"] = "%s: %s | %s: %s" % \
                             (self.game.player1.color, 
                              self.game.player1.score, 
                              self.game.player2.color, 
                              self.game.player2.score)

    def update_status(self, message):
        self.status["text"] = message

    def go(self, position):
        if not self.game:
            return
        if self.game.turn.mode == "C":
            message = "It's the computer turn. Please, wait a moment."
            self.update_status(message=message)
        else:
            self.play(position)

    def play(self, position):
        """Move a piece to the given position."""
        if self.game:
            if not self.game.play(position):
                message = "Invalid move. It's %s's turn." % self.game.turn.color
                self.update_status(message)
                return
            print self.game
            message = "%s's turn." % (self.game.turn.color)
            self.update_status(message)
            self.update_board()          
            self.check_next_turn()

    def computer_play(self):
        if self.difficulty == 0:
            position = ingenuos(self.game.board, self.game.turn.color)
            self.game.play(position)
        print self.game
        self.update_board()
        self.check_next_turn()

    def check_next_turn(self):
        if self.game.test_end():
            self.show_end()
            self.game = False
            self.pass_turn["state"] = DISABLED
            return
        if self.game.turn.mode == "C":
            if not self.game.board.has_valid_position(self.game.turn.color):
                self.game.change_turn()
                message = "Computer Passed. Now it's %s's turn." % \
                          (self.game.turn.color)
                self.update_status(message)
                self.update_board()
            else:
                #computer always has a movement to do
                self.computer_play()
                try:
                    message = "%s's turn." % (self.game.turn.color)
                    self.update_status(message)
                    self.update_board()
                except:
                    pass
        else:
            if not self.game.board.has_valid_position(self.game.turn.color):
                message = "%s must pass." % (self.game.turn.color)
                self.update_status(message)
                self.update_board()
            else:
                message = "%s's turn." % (self.game.turn.color)
                self.update_status(message)
                self.update_board()

    def show_end(self):
        message = "End of game."
        tkMessageBox.showinfo(title="End", message=message)

    def disable_pieces(self):
        for i in range(8):
            for j in range(8):
                position = self.board[(i, j)]
                position["state"] = DISABLED

    def update_board(self):
        """Update the pieces from the engine's board."""
        for row in range(8):
            for column in range(8):
                position = self.board[(row, column)]
                position["state"] = NORMAL
                if self.game.board[(row, column)] == "W":
                    position["image"] = self.white_image
                elif self.game.board[(row, column)] == "B":
                    position["image"] = self.black_image
                else:
                    position["image"] = self.empty_image


        self.pass_turn["state"] = DISABLED
        if not self.game.board.has_valid_position(self.game.turn.color):
            self.pass_turn["state"] = NORMAL
        elif self.show_valid_positions:
            valid_positions = self.game.board.valid_positions(self.game.turn.color)
            for position in valid_positions:
                self.board[position]["image"] = self.valid_image
        self.update_score()


if __name__ == "__main__":
    app = Application()
