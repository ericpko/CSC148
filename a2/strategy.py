""" A module for strategies.

=== CSC148 Winter 2018 ===
University of Toronto,
Department of Computer Science
__author__ = 'Eric Koehli'
Assignment 2

=== Module Description ===
This module contains different strategies to be used for playing
a two-player game.
"""
from typing import Union
from stonehenge import StonehengeGame, StonehengeGameState
from subtract_square_game import SubtractSquareGame
from stack import Stack
from wrapper import Wrapper


def interactive_strategy(
        game: Union[StonehengeGame, SubtractSquareGame]) -> Union[str, int]:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(
        game: Union[StonehengeGame, SubtractSquareGame]) -> Union[str, int]:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(
        game: Union[StonehengeGame, SubtractSquareGame]) -> Union[str, int]:
    r"""
    Return a move for <game> by picking a move that will lead to a win,
    if possible.

    Idea: Each move will make a new game state that will have a longest path
    and a shortest path. These are the cases where we have reached a leaf,
    (i.e. we've reached a game state where the game is over). Most of the
    time these two values will be the same, but in some situations they won't.
    I am defining path length here to be the maximum or minimum length of a
    'Tree' (by the definition of height with respect to trees).

    Apply a move -> make a new game state, and find out the "height"
    (by the definition of height for trees) of that 'tree'. For each 'Tree',
    there will be a maximum 'height' (which is the actual def of tree height)
    and a minimum 'height' (which is the shortest length/path of the 'tree').
    After we find out the min/max 'height' of this tree, we can add one to the
    result since we also need to count the move that we just applied.
    Since the 'leafs' of these 'trees' all result in a score of -1 (i.e. the
    game state is over), we can either use (-1) ** height of the tree or
    height % 2 == 0 to find out if the 'height' of our tree is even or odd.
    If the height is even, then that corresponding move can result in a win,
    otherwise, we can't win.

    >>> sh = StonehengeGame(True, 2)
    >>> gs = StonehengeGameState(board_length=2)
    >>> gs2 = gs.make_move('D')
    >>> gs3 = gs2.make_move('B')
    >>> gs4 = gs3.make_move('C')
    >>> gs5 = gs4.make_move('F')
    >>> sh.current_state = gs5
    >>> print(sh.current_state)
            1   2
           /   /
      2 - A - 2   @
         / \ / \ /
    1 - 1 - 1 - E
         \ / \ / \
      2 - 2 - G   2
           \   \
            1   @
    >>> recursive_minimax_strategy(sh)  in ['E', 'G']
    True
    >>> sh2 = StonehengeGame(True, 2)
    >>> gs10 = StonehengeGameState(board_length=2)
    >>> gs11 = gs10.make_move('D')
    >>> gs12 = gs11.make_move('F')
    >>> gs13 = gs12.make_move('A')
    >>> sh2.current_state = gs13
    >>> print(sh2.current_state)
            1   @
           /   /
      1 - 1 - B   @
         / \ / \ /
    @ - C - 1 - E
         \ / \ / \
      2 - 2 - G   @
           \   \
            2   1
    >>> recursive_minimax_strategy(sh2)
    'E'
    >>> sh3 = StonehengeGame(True, 2)
    >>> gs20 = StonehengeGameState(board_length=2)
    >>> gs21 = gs20.make_move('B')
    >>> gs22 = gs21.make_move('A')
    >>> sh3.current_state = gs22
    >>> print(sh3.current_state)
            2   @
           /   /
      1 - 2 - 1   @
         / \ / \ /
    @ - C - D - E
         \ / \ / \
      @ - F - G   1
           \   \
            @   @
    >>> recursive_minimax_strategy(sh3)
    'F'
    """
    current_state = game.current_state
    available_moves = current_state.get_possible_moves()

    best_move = None
    for move in available_moves:
        new_state = current_state.make_move(move)
        game.current_state = new_state

        score = _recursive_is_winner(game)
        if score == 1:
            best_move = move

    # reset our game's current_state attr
    game.current_state = current_state
    if best_move is not None:
        return best_move
    # if all else fails -> no hope of winning is left :(
    return available_moves[0]


def _recursive_is_winner(
        game: Union[StonehengeGame, SubtractSquareGame]) -> int:
    """ Return
    """
    state = game.current_state
    actual_player, other_player = 'p1', 'p2'
    if actual_player == state.get_current_player_name():
        actual_player, other_player = 'p2', 'p1'

    if game.is_winner(actual_player):
        return 1
    elif game.is_winner(other_player):
        return -1
    else:
        scores = []
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            game.current_state = new_state
            score = _recursive_is_winner(game)
            scores.append(score)
    return max(scores)


def _recursive_height_max(
        game: Union[StonehengeGame, SubtractSquareGame]) -> int:
    """
    Return the height of the "Tree-like" game structure.

    (By the definition of height with respect to Tree's).

    These doctests fail on purpose and were used for testing purposes only.

    # >>> sh = StonehengeGame(True, 2)
    # >>> gs = StonehengeGameState(board_length=2)
    # >>> gs2 = gs.make_move('D')
    # >>> gs3 = gs2.make_move('B')
    # >>> gs4 = gs3.make_move('C')
    # >>> gs5 = gs4.make_move('F')
    # >>> sh.current_state = gs5
    # >>> print(sh.current_state)
    #
    # >>> _recursive_height_max(sh)
    #
    # >>> gs6 = gs5.make_move('G')
    # >>> sh.current_state = gs6
    # >>> print(sh.current_state)
    #
    # >>> _recursive_height_max(sh)
    #
    # >>> sh2 = StonehengeGame(True, 2)
    # >>> gs10 = StonehengeGameState(board_length=2)
    # >>> gs11 = gs10.make_move('D')
    # >>> gs12 = gs11.make_move('F')
    # >>> gs13 = gs12.make_move('A')
    # >>> gs14 = gs13.make_move('E')
    # >>> sh2.current_state = gs14
    # >>> print(sh2.current_state)
    #
    # >>> _recursive_height_max(sh2)

    """
    state = game.current_state
    if game.is_over(state):
        return 1
    else:
        heights = []
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            game.current_state = new_state
            height = _recursive_height_max(game)
            heights.append(height)

    # pyta hates it when I return in an else block...
    return 1 + max(heights)


def _recursive_height_min(
        game: Union[StonehengeGame, SubtractSquareGame]) -> int:
    """
    Return the minimum height of the "Tree-like" game structure.

    These doctests fail on purpose and were used for testing purposes only.

    # >>> sh = StonehengeGame(True, 2)
    # >>> gs = StonehengeGameState(board_length=2)
    # >>> gs2 = gs.make_move('D')
    # >>> gs3 = gs2.make_move('B')
    # >>> gs4 = gs3.make_move('C')
    # >>> gs5 = gs4.make_move('F')
    # >>> sh.current_state = gs5
    # >>> print(sh.current_state)
    #
    # >>> _recursive_height_min(sh)
    #
    # >>> gs6 = gs5.make_move('G')
    # >>> sh.current_state = gs6
    # >>> print(sh.current_state)
    #
    # >>> _recursive_height_min(sh)
    #
    # >>> sh2 = StonehengeGame(True, 2)
    # >>> gs10 = StonehengeGameState(board_length=2)
    # >>> gs11 = gs10.make_move('D')
    # >>> gs12 = gs11.make_move('F')
    # >>> gs13 = gs12.make_move('A')
    # >>> gs14 = gs13.make_move('E')
    # >>> sh2.current_state = gs14
    # >>> print(sh2.current_state)
    #
    # >>> _recursive_height_min(sh2)

    """
    state = game.current_state
    if game.is_over(state):
        return 1
    else:
        heights = []
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            game.current_state = new_state
            height = _recursive_height_min(game)
            heights.append(height)

    # pyta hates it when I return in an else block...
    return 1 + min(heights)


def iterative_minimax_strategy(
        game: Union[StonehengeGame, SubtractSquareGame]) -> Union[str, int]:
    r"""
    Return a move for <game> by picking a move that will lead to a win,
    if possible.

    >>> sh = StonehengeGame(True, 2)
    >>> gs = StonehengeGameState(board_length=2)
    >>> gs2 = gs.make_move('D')
    >>> gs3 = gs2.make_move('B')
    >>> gs4 = gs3.make_move('C')
    >>> gs5 = gs4.make_move('F')
    >>> sh.current_state = gs5
    >>> print(sh.current_state)
            1   2
           /   /
      2 - A - 2   @
         / \ / \ /
    1 - 1 - 1 - E
         \ / \ / \
      2 - 2 - G   2
           \   \
            1   @
    >>> iterative_minimax_strategy(sh) in ['E', 'G']
    True
    >>> sh2 = StonehengeGame(True, 2)
    >>> gs10 = StonehengeGameState(board_length=2)
    >>> gs11 = gs10.make_move('D')
    >>> gs12 = gs11.make_move('F')
    >>> gs13 = gs12.make_move('A')
    >>> sh2.current_state = gs13
    >>> print(sh2.current_state)
            1   @
           /   /
      1 - 1 - B   @
         / \ / \ /
    @ - C - 1 - E
         \ / \ / \
      2 - 2 - G   @
           \   \
            2   1
    >>> iterative_minimax_strategy(sh2)
    'E'
    """
    current_state = game.current_state
    state = Wrapper(current_state)
    stk = Stack()
    stk.push(state)

    # Here we go:
    while not stk.is_empty():
        state = stk.pop()
        # Update the game's current_state attr to use is_over method
        game.current_state = state.state

        if game.is_over(state.state):
            # remember state is wrapped in a 'Wrapper' object.
            state.score = -1

        elif state.children == []:
            # Then we haven't looked at this state yet.
            # Wrap the new state with the move that made that state.
            for move in state.state.get_possible_moves():
                new_state = state.state.make_move(move)
                wrap = Wrapper(new_state, move=move)
                state.children.append(wrap)

            stk.push(state)
            for child in state.children:
                stk.push(child)

        # Build a helper for this else block for dumb pyta
        else:
            # Then we've already looked at this state. So it should
            # have a list of children
            _iterative_update_score(state)

    # reset the game's current_state attr back to before mutation.
    game.current_state = current_state
    # After the while loop, there should be a wrapper that has children...
    for child in state.children:
        if child.score == -1:
            return child.move

    # There is no hope of winning :(
    available_moves = current_state.get_possible_moves()
    return available_moves[0]


def _iterative_update_score(state: Wrapper) -> None:
    """ Update the score of <state>

    """
    # curr_player, opponent = 'p1', 'p2'
    # if curr_player != curr_state.get_current_player_name():
    #     curr_player, opponent = 'p2', 'p1'
    best_score = -2
    for child in state.children:
        other_score = child.score * -1
        if other_score >= best_score:
            best_score = other_score
    state.score = best_score


def _for_pyta(state: StonehengeGameState) -> None:
    """
    Please ignore this function, it does nothing. I had to include it
    so pyta wouldn't complain about not using StonehengeGameState
    (because I imported it at the top). I imported it for my doctests
    to run, but if I remove the import statement (as pyta recommends I do),
    then all my tests fail.
    """
    state.get_possible_moves()


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
