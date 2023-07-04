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
    contX = 0
    contO = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == X:
                contX += 1
            elif board[i][j] == O:
                contO += 1
    if board == initial_state():
        return X
    if contX > contO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    movement = set()
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == None:
                movement.add((i,j))
    return movement

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in  actions(board):
        raise Exception("Not possible action")
    
    Newboard = copy.deepcopy(board)
    Newboard[action[0]][action[1]] = player(board)
    return Newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    n = len(board)
    for i in range(n):
        if (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
    # Check columns
    for j in range(n):
        if (board[0][j] == board[1][j] == board[2][j]):
            return board[0][j]
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    n = len(board)
    if winner(board) != None:
        return True
    for i in range(n):
        for j in range(n):
            if  board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    alpha = -99
    beta = 99
    if terminal(board):
        return None

    if player(board) == X:
        return max_alpha_beta(board,alpha, beta)[1]
    else:
        return min_alpha_beta(board,alpha, beta)[1]


def max_alpha_beta(board, alpha, beta):

    if terminal(board):
        return utility(board), None
    value = -99
    movement = None
    
    for action in actions(board):
        auxili = min_alpha_beta(result(board, action),alpha, beta)[0]
        Max = max(alpha, auxili)
        if auxili > value:
            value = auxili
            movement = action
        if value >= beta:
            return [value, movement];
        if value > alpha:
            alpha = value
            
    return [value, movement];

def min_alpha_beta(board, alpha, beta):

    if terminal(board):
        return utility(board), None
    value = 99
    movement = None
    
    for action in actions(board):
        auxili = max_alpha_beta(result(board, action),alpha, beta)[0]
        beta = min(beta, auxili)
        if auxili < value:
            value = auxili
            movement = action
        if value <= alpha:
            return [value, movement];
        if value < beta:
            beta = value
            
    return [value, movement];