import time

from Tkinter import *
import tkMessageBox

from game import *
from util import *
import minimax


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
        self.difficulty = 1
        self.mode = 1
        self.color_first_player = "B"
        self.create_elements()
        self.window.mainloop()

    def create_elements(self):
        self.load_images()
        self.create_menu()
        self.create_board()
        self.create_details()

    def load_images(self):
        self.white_image = PhotoImage(file="white.gif")
        self.black_image = PhotoImage(file="black.gif")
        self.empty_image = PhotoImage(file="empty.gif")
        self.valid_image = PhotoImage(file="valid.gif")       

    def create_menu(self):
        self.menu = Menu(self.window)
        self.create_game_menu()
        self.create_settings_menu()
        self.create_help_menu()
        self.window.config(menu=self.menu)

    def create_game_menu(self):
        game = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Game", menu=game, underline=0)
        game.add_command(label="New", command=self.create_game, underline=0)
        game.add_separator()
        game.add_command(label="Quit", command=self.bye, underline=0)

    def create_help_menu(self):
        help = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help, underline=0)
        help.add_command(label="About", command=self.show_credits, underline=0)

    def create_settings_menu(self):
        settings = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Settings", menu=settings, underline=0)
        settings.add_checkbutton(label="Show valid positions",
                                 command=self.toggle_show_valid_positions,
                                 underline=0)

        settings.add_separator()

        first_player = Menu(settings, tearoff=0)
        settings.add_cascade(label="First Player", menu=first_player, underline=0)        
        first_player.add_radiobutton(label="Black", variable=self.color_first_player,
                                     command=lambda color="B": self.set_first_player(color),
                                     underline=0)
        first_player.add_radiobutton(label="White", variable=self.color_first_player,
                                     command=lambda color="W": self.set_first_player(color),
                                     underline=0)

        mode = Menu(settings, tearoff=0)
        settings.add_cascade(label="Mode", menu=mode, underline=0)
        mode.add_radiobutton(label="Human vs Human", variable=self.mode,
                             command=lambda v=0: self.set_mode(v),
                             underline=0)
        mode.add_radiobutton(label="Human vs Computer", variable=self.mode, 
                             command=lambda v=1: self.set_mode(v),
                             underline=1)
        mode.add_radiobutton(label="Computer vs Human", variable=self.mode,
                             command=lambda v=2: self.set_mode(v),
                             underline=2)

        difficulty = Menu(settings, tearoff=0)
        settings.add_cascade(label="Difficulty", menu=difficulty, underline=0)
        difficulty.add_radiobutton(label="Baby",
                                   command=lambda depth=0: self.set_difficulty(depth),
                                   underline=0)
        for i in range(1, 5):
            difficulty.add_radiobutton(label="Depth %s" % i,
                                       command=lambda depth=i: self.set_difficulty(depth),
                                       underline=6)

        #set the default values
        first_player.invoke(first_player.index("Black"))
        mode.invoke(mode.index("Human vs Computer"))
        difficulty.invoke(difficulty.index("Depth 2"))

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

    def create_details(self):
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
                         p1_mode=p1_mode, p2_mode=p2_mode)
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
        self.update_board()

    def show_credits(self):
        message = "MonOthello\nv.: 1.0"
        tkMessageBox.showinfo(title="About", message=message)

    def update_score(self):
        self.score["text"] = "%s(%s): %s | %s(%s): %s" % \
                             (self.game.player1.color,
                              self.game.player1.mode, 
                              self.game.player1.score, 
                              self.game.player2.color,
                              self.game.player2.mode, 
                              self.game.player2.score)

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
        valid = self.game.play(position)
        if not valid:
            message = "Invalid move. It's %s's turn." % self.game.turn.color
            self.update_status(message)
        else:
            message = "%s's turn." % (self.game.turn.color)
            self.update_status(message)
            self.update_board()
            self.check_next_turn()

    def computer_play(self):            
        if self.difficulty == 0:
            position = minimax.ingenuos(self.game.board, self.game.turn.color)
            self.game.play(position)
        else:
            minimax.PLAYER = self.game.turn.color
            position = minimax.minimax(self.game.board, self.difficulty, self.game.turn.color)[1]
            self.game.play(position)
        message = "%s's turn." % (self.game.turn.color)        
        self.update_status(message)
        self.update_board()
        self.check_next_turn()       

    def check_next_turn(self):
        if self.game.test_end():
            self.update_status("End of game.")
            self.update_board()
            self.show_end()
            self.pass_turn["state"] = DISABLED
            self.game = False
            return
        if self.game.turn.mode == "C":
            if not has_valid_position(self.game.board, self.game.turn.color):
                self.game.change_turn()
                message = "Computer Passed. Now it's %s's turn." % \
                          (self.game.turn.color)
                self.update_status(message)
                self.update_board()
                return
            else:
                #computer always has a movement to do
                self.update_status("Computer is 'thinking'. Please, wait a moment...")
                self.update_board()            
                self.computer_play()

    def show_end(self):
        message = "End of game."
        tkMessageBox.showinfo(title="End", message=message)

    def update_status(self, message):
        self.status["text"] = message
        self.window.update_idletasks()

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
        if not has_valid_position(self.game.board, self.game.turn.color):
            self.pass_turn["state"] = NORMAL
        elif self.show_valid_positions:
            valid = valid_positions(self.game.board, self.game.turn.color)
            for position in valid:
                self.board[position]["image"] = self.valid_image
        self.update_score()
        self.window.update_idletasks()

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()

if __name__ == "__main__":
    app = Application()
