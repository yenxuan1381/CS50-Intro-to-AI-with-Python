"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    # count the number of X's and O's

    for row in board:
        for elm in row:
            if elm == X:
                count_x += 1
            elif elm == O:
                count_o += 1

    if count_x <= count_o:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # use enumerate to display loop counts

    for y, row in enumerate(board):
        for x, elm in enumerate(row):
            if elm == EMPTY:
                possible_actions.add((y, x))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # a valid action should be a set with only 2 elements
    if len(action) != 2:
        raise Exception("result function: incorrect action")

    # the element of the action should be 0, 1 or 2 only
    if (action[0] < 0 or action[0] > 2) or (action[1] < 0 or action[1] > 2):
        raise Exception("result function: incorrect action value")

    y, x = action[0], action[1]

    board_copy = copy.deepcopy(board)

    if board_copy[y][x] != EMPTY:
        raise Exception("suggested action has already been taken")
    else:
        board_copy[y][x] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check horizontal
    for row in board:
        if (row[0] == row[1] == row[2]) and row[0] != EMPTY:
            return row[0]

    # check vertical
    for col in zip(*board):
        if (col[0] == col[1] == col[2]) and row[0] != EMPTY:
            return col[0]

    # check diagonal
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) \
            and board[1][1] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there's a winner, the game is over
    if winner(board) == X or winner(board) == O:
        return True

    # check if no empty  cells are left
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    elif winner(board) == O:
        return -1

    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None

    # X is the maximizing player
    if current_player == X:
        best_v = -math.inf

        # for every action available,
        for action in actions(board):
            # the minimizing player is going to play optimally
            max_v = min_value(result(board, action))

            # we choose the action that is going to yield the highest utility
            if max_v > best_v:
                best_v = max_v
                best_action = action

    # O is the minimizing player
    elif current_player == O:
        best_v = math.inf

        # for every action available,
        for action in actions(board):
            # the maximizing player is going to play optimally
            min_v = max_value(result(board, action))

            # we choose the action that is going to yield the least utility
            if min_v < best_v:
                best_v = min_v
                best_action = action

    return best_action


def max_value(board):
    """
    returns max_value of all the min_values
    """
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v



def min_value(board):
    """
    returns min_value of all the max_values
    """
    if terminal(board):  # if game over, just return the utility of state
        return utility(board)

    v = math.inf  # iterate over the available actions and return the minimum out of all maximums
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
