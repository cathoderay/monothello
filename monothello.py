from Tkinter import *
import tkMessageBox

from game import *
import minimax


class Application:

    """GUI of the game."""

    def __init__(self):
        """Initialize the window and the GUI elements."""

        self.window = Tk()
        self.window.title("MonOthello")
        self.window.wm_maxsize(width="460", height="540")
        self.window.wm_minsize(width="460", height="540")


        self.game = False
        self.show_valid_positions = 0
        self.difficulty = 1
        self.mode = 2
        self.color_first_player = 3
        self.heuristic = 4
        self.create_elements()
        self.update_status("Welcome to MonOthello!")
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

        settings.add_checkbutton(label="Show valid positions", variable=self.show_valid_positions,
                                 command=self.toggle_show_valid_positions,
                                 underline=0)

        settings.add_separator()

        first_player = Menu(settings, tearoff=0)
        mode = Menu(settings, tearoff=0)
        heuristic = Menu(settings, tearoff=0)
        difficulty = Menu(settings, tearoff=0)


        settings.add_cascade(label="First Player", menu=first_player, underline=0)        
        first_player.add_radiobutton(label="Black", variable=self.color_first_player,
                                     command=lambda: self.set_first_player("B"),
                                     underline=0)
        first_player.add_radiobutton(label="White", variable=self.color_first_player,
                                     command=lambda: self.set_first_player("W"),
                                     underline=0)



        settings.add_cascade(label="Mode", menu=mode, underline=0)
        mode.add_radiobutton(label="Human vs Human", variable=self.mode, 
                             command=lambda: self.set_mode(0), underline=0)
        mode.add_radiobutton(label="Human vs Computer", variable=self.mode, 
                             command=lambda: self.set_mode(1), underline=1)
        mode.add_radiobutton(label="Computer vs Human", variable=self.mode, 
                             command=lambda: self.set_mode(2), underline=12)


        settings.add_cascade(label="Heuristic", menu=heuristic, underline=0)
        heuristic.add_radiobutton(label="Baby", variable=self.heuristic, underline=0, 
                                  command=lambda: self.set_heuristic(minimax.baby),
                                  value=0)

        heuristic.add_radiobutton(label="Weak", variable=self.heuristic, underline=0,
                                  command=lambda: self.set_heuristic(minimax.weak),
                                  value=1)

        heuristic.add_radiobutton(label="Greedy", variable=self.heuristic, underline=0,
                                  command=lambda: self.set_heuristic(minimax.greedy),
                                  value=2)

        heuristic.add_radiobutton(label="Posicional", variable=self.heuristic, underline=0,
                                  command=lambda: self.set_heuristic(minimax.posicional),
                                  value=3)

        heuristic.add_radiobutton(label="Marc Mandt Posicional", variable=self.heuristic, underline=0,
                                  command=lambda: self.set_heuristic(minimax.marc_mandt_posicional),
                                  value=4)



        settings.add_cascade(label="Difficulty", menu=difficulty, underline=0)
        difficulty.add_radiobutton(label="Depth 1", 
                                   variable=self.difficulty,
                                   command=lambda: self.set_difficulty(1),
                                   underline=6)
        difficulty.add_radiobutton(label="Depth 2", 
                                   variable=self.difficulty,
                                   command=lambda: self.set_difficulty(2),
                                   underline=6)
        difficulty.add_radiobutton(label="Depth 3", 
                                   variable=self.difficulty,
                                   command=lambda: self.set_difficulty(3),
                                   underline=6)
        difficulty.add_radiobutton(label="Depth 4", 
                                   variable=self.difficulty,
                                   command=lambda: self.set_difficulty(4),
                                   underline=6)


        #set the default values
        first_player.invoke(first_player.index("Black"))
        mode.invoke(mode.index("Human vs Computer"))
        difficulty.invoke(difficulty.index(1))
        heuristic.invoke(heuristic.index("Weak"))


    def set_mode(self, m):
        self.mode = m
        print 'Mode changed to:'
        print self.mode

    def set_first_player(self, c):
        self.color_first_player = c
        print 'First player changed to to:'
        print self.color_first_player

    def set_difficulty(self, d):
        self.difficulty = d
        print 'Difficulty changed to:'
        print self.difficulty
    
    def set_heuristic(self, h):
        self.heuristic = h
        print 'Heuristic changed to:'
        print self.heuristic

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
        message = "Let's play! Now it's the %s's turn." % self.game.turn.color
        self.update_status(message)
        self.update_board()
        self.update_score()
        self.update_pass_turn()

    def toggle_show_valid_positions(self):
        self.show_valid_positions = not self.show_valid_positions           
        if self.game:
            self.update_board()

    def pass_turn(self):
        """Pass the turn when it's not possible to play."""
        if not self.game:
            return
        self.game.change_turn()
        if self.game.turn.mode == "C":
            self.computer_play()
        if self.game:
            message = "%s's turn." % self.game.turn.color
            self.update_status(message)
            self.update_board()

    def show_credits(self):
        message = "MonOthello\nv.: 1.0"
        tkMessageBox.showinfo(title="About", message=message)

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
            self.update_score()
            self.update_pass_turn()
            self.check_next_turn()

    def computer_play(self):            

        minimax.PLAYER = self.game.turn.color
        print '------------------------------'
        print 'executing minimax with:'
        print self.game.board
        print self.game.turn.color
        print '------------------------------'
        position = minimax.minimax(self.game.board, 
                                   self.difficulty, 
                                   self.game.turn.color, 
                                   self.heuristic)[1]
        print 'minimax finished with choice: %s' % str(position)
        self.game.play(position)
        message = "%s's turn." % (self.game.turn.color)        
        self.update_status(message)
        self.update_board()
        self.update_score()
        self.update_pass_turn()
        self.check_next_turn()       

    def check_next_turn(self):
        if self.game.test_end():
            self.update_status("End of game.")
            self.update_board()
            self.update_score()
            self.update_pass_turn()
            self.show_end()
            self.game = False
            return
        if self.game.turn.mode == "C":
            if not has_valid_position(self.game.board, self.game.turn.color):
                self.game.change_turn()
                message = "Computer Passed. Now it's %s's turn." % \
                          (self.game.turn.color)
                self.update_status(message)
                self.update_board()
                self.update_pass_turn()
                return
            else:
                #computer always has a movement to do
                self.update_status("Computer is 'thinking'. Please, wait a moment...")
                self.update_board()
                self.computer_play()

    def show_end(self):
        message = "End of game. %s" % self.game.winning_side()
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
                    position.update_idletasks()
                elif self.game.board[(row, column)] == "B":
                    position["image"] = self.black_image
                    position.update_idletasks()
                else:
                    position["image"] = self.empty_image
                    position.update_idletasks()
        if self.show_valid_positions:
            valid = list(valid_positions(self.game.board, self.game.turn.color))
            for position in valid:
                p = self.board[position]
                p["image"] = self.valid_image
                p.update_idletasks()
                

    def update_score(self):
        self.score["text"] = "%s(%s): %s | %s(%s): %s" % \
                             (self.game.player1.color,
                              self.game.player1.mode, 
                              self.game.player1.score, 
                              self.game.player2.color,
                              self.game.player2.mode, 
                              self.game.player2.score)
        self.score.update_idletasks()

    def update_pass_turn(self):
        self.pass_turn["state"] = DISABLED
        if not has_valid_position(self.game.board, self.game.turn.color):
            self.pass_turn["state"] = NORMAL
            self.pass_turn.update_idletasks()

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()

if __name__ == "__main__":
    app = Application()
