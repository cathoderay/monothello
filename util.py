

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), 
                   (1, 1), (1, -1), (-1, 1), (-1, -1)]


def count_pieces(board, color):
    """Count the pieces in the board of the given color."""
    sum = 0
    for i in range(8):
        for j in range(8):
            if board[(i, j)] == color:
                sum += 1
    return sum


def has_valid_position(board, turn):
    """Return if the turn has any valid position."""
    for i in range(8):
        for j in range(8):
            position = (i, j)
            if is_valid_position(board, position, turn):
                return True
    return False


def valid_positions(board, turn):
    """Return a set with all valid positions for the given turn."""
    valid = list()
    for i in range(8):
        for j in range(8):
            position = (i, j)
            if is_valid_position(board, position, turn):
                valid.append(position)
    return set(valid)


def end_game(board):
    """Return a bool.
    Check the end of the game.

    """
    return not has_valid_position(board, "W") and not \
           has_valid_position(board, "B")


def is_valid_position(board, position, turn):
    """Return a bool.
    Check if the given position is valid for this turn.
    
    """
    if board[position] != "E": return False
    for direction in directions:
        between = 0
        i, j = position
        while True:
            try:
                i += direction[0]
                j += direction[1]
                if board[(i, j)] == "E":
                    break
                if board[(i, j)] != turn:
                    between += 1
                elif between > 0:
                    return True
                else:
                    break                    
            except KeyError:
                break
    return False


def move(board, position, turn):
    """Move to the given position a piece of the color of the turn."""
    to_change = []
    for direction in directions:
        between = 0
        i, j = position
        while True:
            try:
                i += direction[0]
                j += direction[1]
                if board[(i, j)] == "E":
                    break
                if board[(i, j)] != turn:
                    between += 1
                elif between > 0:
                    x, y = position                        
                    for times in range(between+1):
                        to_change.append((x, y))
                        x += direction[0]
                        y += direction[1]
                    break
                else:
                    break
            except KeyError:
                break
    for item in to_change:
        board[item] = turn
