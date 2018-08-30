""" --- Stonehenge Game ---

=== CSC148 Winter 2018 ===
University of Toronto
Assignment 2
Submitted by: Eric Koehli

=== Module Description ===
This module contains the Stonehenge game and Stonehenge game state.
"""
from typing import Any, List, Union, Dict, Tuple
from copy import deepcopy
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    A playable stonehenge game implementation. This is a subclass of Game.

    === Public Attributes ===
    current_state: The current state of the game.
    """
    current_state: 'StonehengeGameState'

    def __init__(self, p1_starts: bool = True, size: int = -1) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        If <p1_starts> is true, p1 starts the game. If false, p2 starts.
        """
        while size not in [1, 2, 3, 4, 5]:
            try:
                size = int(input('Enter the side length of the board'
                                 ' between 1 and 5 inclusive: '))
            except ValueError:
                print("Oops! That wasn't in the correct range... Please "
                      "try again.")
        self.current_state = StonehengeGameState(p1_starts, size)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.

        >>> sh = StonehengeGame(True, 2)
        >>> sh2 = StonehengeGame(False, 5)
        >>> sh.get_instructions() == sh2.get_instructions()
        True
        >>> print(sh.get_instructions())
        Welcome to Stonehenge! The goal of the game is to capture at least
        half of the total number of ley-lines before your opponent does.
        Good luck!
        """
        res = 'Welcome to Stonehenge! The goal of the game is to capture at ' \
              'least\nhalf of the total number of ley-lines before your ' \
              'opponent does.\nGood luck!'
        return res

    def is_over(self, state: 'StonehengeGameState') -> bool:
        """
        Return whether or not this game is over at state.

        >>> sh = StonehengeGame(True, 1)
        >>> sh2 = StonehengeGame(True, 2)
        >>> sh_a = sh.current_state.make_move('A')
        >>> sh_b = sh2.current_state.make_move('B')
        >>> sh.is_over(sh_a)
        True
        >>> sh.is_over(sh_b)
        False
        >>> sh2.is_over(sh_a)
        True
        >>> sh2.is_over(sh_b)
        False
        """
        ones, twos = 0, 0
        for board_line in state.board:
            for ch in board_line:
                if ch == 'p1':
                    ones += 1
                elif ch == 'p2':
                    twos += 1

        num_ley_lines = len(state.ley_lines)
        if ones / num_ley_lines >= 0.5:
            return True
        elif twos / num_ley_lines >= 0.5:
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        >>> sh = StonehengeGame(True, 1)
        >>> sh2 = StonehengeGame(True, 2)
        >>> sh_a = sh.current_state.make_move('A')
        >>> sh_b = sh2.current_state.make_move('B')
        >>> sh.is_winner('p1')
        False
        >>> sh.is_winner('p2')
        False
        >>> sh2.is_winner('p1')
        False
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Union[str, int]:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.

        >>> sh = StonehengeGame(size=2)
        >>> sh2 = StonehengeGame(False, 4)
        >>> sh.str_to_move('A')
        'A'
        >>> sh.str_to_move('a')
        'A'
        >>> sh.str_to_move('0')
        -1
        >>> sh2.str_to_move('hi')
        'HI'
        """
        if not string.strip().isalpha():
            return -1
        return string.strip().upper()


class StonehengeGameState(GameState):
    """
    The Game State for the game Stonehenge.

    === Public Attributes ===
    ley_lines:
           A dictonary data structure to store the current
           ley-line information in the game. Each key is a
           string of a ley-line and each value is a list of
           cells in that ley-line.
    board:
           A representation of the current stonehenge board.
           Each sublist contains a row of the board.
    """
    ley_lines: Dict[str, List[str]]
    board: List[List[str]]

    def __init__(self, is_p1_turn: bool = True, board_length: int = 1,
                 ley_lines: Dict[str, List[str]] = None,
                 board: List[List[str]] = None) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        >>> shgs = StonehengeGameState()
        >>> shgs.ley_lines
        {'ley_line1': ['@', 'A'], 'ley_line2': ['@', 'B', 'C'], 'ley_line3': \
['@', 'A', 'B'], 'ley_line4': ['@', 'C'], 'ley_line5': ['@', 'B'], \
'ley_line6': ['@', 'C', 'A']}
        """
        GameState.__init__(self, is_p1_turn)
        if ley_lines is None:
            self.ley_lines = self._build_ley_lines(board_length)
            self.board = self._make_board(board_length)
        else:
            self.ley_lines, self.board = ley_lines, board

    def _build_ley_lines(self, board_length) -> Dict[str, List[str]]:
        """A helper method to create the data structure to hold the ley-line
        information from the game.
        """
        if board_length == 1:
            ley_lines = {'ley_line1': ['A'], 'ley_line2': ['B', 'C'],
                         'ley_line3': ['A', 'B'], 'ley_line4': ['C'],
                         'ley_line5': ['B'], 'ley_line6': ['C', 'A']}
        elif board_length == 2:
            ley_lines = {'ley_line1': ['A', 'C'], 'ley_line2': ['B', 'D', 'F'],
                         'ley_line3': ['A', 'B'], 'ley_line4': ['E', 'G'],
                         'ley_line5': ['C', 'D', 'E'],
                         'ley_line6': ['F', 'G'], 'ley_line7': ['E', 'B'],
                         'ley_line8': ['F', 'C'], 'ley_line9': ['G', 'D', 'A']}
        elif board_length == 3:
            ley_lines = {'ley_line1': ['A', 'C', 'F'],
                         'ley_line2': ['B', 'D', 'G', 'J'],
                         'ley_line3': ['A', 'B'], 'ley_line4': ['E', 'H', 'K'],
                         'ley_line5': ['C', 'D', 'E'], 'ley_line6': ['I', 'L'],
                         'ley_line7': ['F', 'G', 'H', 'I'],
                         'ley_line8': ['J', 'K', 'L'],
                         'ley_line9': ['I', 'E', 'B'], 'ley_line10': ['J', 'F'],
                         'ley_line11': ['K', 'G', 'C'],
                         'ley_line12': ['L', 'H', 'D', 'A']}
        elif board_length == 4:
            ley_lines = {'ley_line1': ['A', 'C', 'F', 'J'],
                         'ley_line2': ['B', 'D', 'G', 'K', 'O'],
                         'ley_line3': ['A', 'B'],
                         'ley_line4': ['E', 'H', 'L', 'P'],
                         'ley_line5': ['C', 'D', 'E'],
                         'ley_line6': ['I', 'M', 'Q'],
                         'ley_line7': ['F', 'G', 'H', 'I'],
                         'ley_line8': ['N', 'R'],
                         'ley_line9': ['J', 'K', 'L', 'M', 'N'],
                         'ley_line10': ['O', 'P', 'Q', 'R'],
                         'ley_line11': ['N', 'I', 'E', 'B'],
                         'ley_line12': ['O', 'J'],
                         'ley_line13': ['P', 'K', 'F'],
                         'ley_line14': ['Q', 'L', 'G', 'C'],
                         'ley_line15': ['R', 'M', 'H', 'D', 'A']}
        else:
            ley_lines = {'ley_line1': ['A', 'C', 'F', 'J', 'O'],
                         'ley_line2': ['B', 'D', 'G', 'K', 'P', 'U'],
                         'ley_line3': ['A', 'B'],
                         'ley_line4': ['E', 'H', 'L', 'Q', 'V'],
                         'ley_line5': ['C', 'D', 'E'],
                         'ley_line6': ['I', 'M', 'R', 'W'],
                         'ley_line7': ['F', 'G', 'H', 'I'],
                         'ley_line8': ['N', 'S', 'X'],
                         'ley_line9': ['J', 'K', 'L', 'M', 'N'],
                         'ley_line10': ['T', 'Y'],
                         'ley_line11': ['O', 'P', 'Q', 'R', 'S', 'T'],
                         'ley_line12': ['U', 'V', 'W', 'X', 'Y'],
                         'ley_line13': ['T', 'N', 'I', 'E', 'B'],
                         'ley_line14': ['U', 'O'],
                         'ley_line15': ['V', 'P', 'J'],
                         'ley_line16': ['W', 'Q', 'K', 'F'],
                         'ley_line17': ['X', 'R', 'L', 'G', 'C'],
                         'ley_line18': ['Y', 'S', 'M', 'H', 'D', 'A']}
        for ley_line in ley_lines:
            if '@' not in ley_lines[ley_line]:
                ley_lines[ley_line].insert(0, '@')
        return ley_lines

    def _make_board(self, board_length: int) -> List[List[str]]:
        """Return a list of strings that represents the current state
        of the stonehenge game's board.

        This is a helper function for __init__
        """
        if board_length == 1:
            board = '      @   @\n     /   /\n@ - A - B\n     \\ / \\\n  @ - ' \
                    'C   @\n       \\\n        @\n'
        elif board_length == 2:
            board = '        @   @\n       /   /\n  @ - A - B   @\n   ' \
                    '  / \\ / \\ /\n@ - C - D - E\n     \\ / \\ / \\\n  ' \
                    '@ - F - G   @\n       \\   \\\n        @   @\n'
        elif board_length == 3:
            board = '          @   @\n         /   /\n    @ - A - B   @\n   ' \
                    '    / \\ / \\ /\n  @ - C - D - E   @\n  ' \
                    '   / \\ / \\ / \\ /\n@ - F - G - H - I\n   ' \
                    '  \\ / \\ / \\ / \\\n  @ - J - K - L   @\n    ' \
                    '   \\   \\   \\\n        @   @   @\n'
        elif board_length == 4:
            board = '            @   @\n           /   /\n    ' \
                    '  @ - A - B   @\n         / \\ / \\ /\n    @ - C - D - E' \
                    '   @\n       / \\ / \\ / \\ /\n  @ - F - G - H - I   @\n' \
                    '     / \\ / \\ / \\ / \\ /\n@ - J - K - L - M - N\n  ' \
                    '   \\ / \\ / \\ / \\ / \\\n  @ - O - P - Q - R   @\n   ' \
                    '    \\   \\   \\   \\\n        @   @   @   @\n'
        else:
            board = '              @   @\n             /   /\n    ' \
                    '    @ - A - B   @\n           / \\ / \\ /\n    ' \
                    '  @ - C - D - E   @\n         / \\ / \\ / \\ /\n  ' \
                    '  @ - F - G - H - I   @\n    ' \
                    '   / \\ / \\ / \\ / \\ /\n  @ - J - K - L - M - N   @\n ' \
                    '    / \\ / \\ / \\ / \\ / \\ /\n@ - O - P - Q - R' \
                    ' - S - T\n     \\ / \\ / \\ / \\ / \\ / \\\n' \
                    '  @ - U - V - W - X - Y   @\n     ' \
                    '  \\   \\   \\   \\   \\\n        @   @   @   @   @\n'
        board = self._organize_board(board)
        return board

    def _organize_board(self, str_board: str) -> List[List[str]]:
        """Return a list of a list of strings, where each sublist
        is a line in the board game.

        This is a helper function for _make_board and __init__.
        """
        board = list(str_board)
        outter_list = []
        i, j = 0, 0
        for ch in board:
            j += 1
            if ch == '\n':
                outter_list.append(board[i:j])
                i = j
        # remove the last \n
        length = len(outter_list)
        outter_list[length - 1].pop()
        return outter_list

    def __str__(self) -> str:
        r"""
        Return a string representation of the current state of the game.

        >>> shgs = StonehengeGameState()
        >>> print(shgs)
              @   @
             /   /
        @ - A - B
             \ / \
          @ - C   @
               \
                @
        >>> shgs2 = StonehengeGameState(True, 2)
        >>> print(shgs2)
                @   @
               /   /
          @ - A - B   @
             / \ / \ /
        @ - C - D - E
             \ / \ / \
          @ - F - G   @
               \   \
                @   @
        >>> print(StonehengeGameState(True, 3))
                  @   @
                 /   /
            @ - A - B   @
               / \ / \ /
          @ - C - D - E   @
             / \ / \ / \ /
        @ - F - G - H - I
             \ / \ / \ / \
          @ - J - K - L   @
               \   \   \
                @   @   @
        >>> print(shgs2.make_move('E'))
                @   @
               /   /
          @ - A - B   1
             / \ / \ /
        @ - C - D - 1
             \ / \ / \
          @ - F - G   1
               \   \
                @   @
        """
        board = deepcopy(self.board)
        for board_line in board:
            for i in range(len(board_line)):
                if board_line[i] == 'p1':
                    board_line[i] = '1'
                elif board_line[i] == 'p2':
                    board_line[i] = '2'
        res = ''
        for board_line in board:
            res += ''.join(board_line)
        return res

    def get_possible_moves(self) -> List[str]:
        """
        Return all possible moves that can be applied to this state.

        >>> shgs = StonehengeGameState()
        >>> shgs.get_possible_moves()
        ['A', 'B', 'C']
        >>> shgs2 = StonehengeGameState(board_length=5)
        >>> shgs2.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        >>> new_state = shgs.make_move('A')
        >>> new_state.get_possible_moves()
        []
        >>> shgs = StonehengeGameState(board_length=2)
        >>> shgs.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        >>> first_move = shgs.make_move('A')
        >>> second_move = first_move.make_move('D')
        >>> second_move.get_possible_moves()
        ['B', 'C', 'E', 'F', 'G']
        """
        all_cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                     'W', 'X', 'Y']
        legal_moves = []
        ones, twos = 0, 0
        for board_line in self.board:
            for cell in board_line:
                if cell in all_cells:
                    legal_moves.append(cell)
                elif cell == 'p1':
                    ones += 1
                elif cell == 'p2':
                    twos += 1

        num_ley_lines = len(self.ley_lines)
        if ones / num_ley_lines >= 0.5:
            return []
        elif twos / num_ley_lines >= 0.5:
            return []
        return legal_moves

    def make_move(self, move: str) -> 'StonehengeGameState':
        """
        Return the GameState that results from applying move to this GameState.

        >>> shgs = StonehengeGameState(board_length=1)
        >>> shgs2 = StonehengeGameState(board_length=2)
        >>> shgs3 = StonehengeGameState(board_length=1)
        >>> repr(shgs) == repr(shgs2)
        False
        >>> repr(shgs) == repr(shgs3)
        True
        >>> new_state1 = shgs.make_move('A')
        >>> repr(new_state1) == repr(shgs3)
        False
        >>> repr(shgs) == repr(new_state1)
        False
        """
        new_ley_lines, ley_line_location = self._update_ley_lines(move)
        new_board = self._update_board(move, ley_line_location)
        new_state = StonehengeGameState(not self.p1_turn,
                                        ley_lines=new_ley_lines,
                                        board=new_board)
        return new_state

    def _update_ley_lines(self, move: str) -> Tuple[Dict[str, List[str]],
                                                    Dict[int, str]]:
        """Return an updated version of <self.ley_lines> based
        off of <move>.

        This is a helper function for make_move.
        """
        if self.get_current_player_name() == 'p1':
            player = '1'
        else:
            player = '2'
        new_ley_lines = deepcopy(self.ley_lines)
        for ley_line in new_ley_lines.values():
            for i in range(len(ley_line)):
                if ley_line[i] == move:
                    ley_line[i] = player
        ley_line_location = self._check_ley_markers(new_ley_lines)
        return new_ley_lines, ley_line_location

    def _check_ley_markers(self,
                           ley_lines: Dict[str, List[str]]) -> Dict[int, str]:
        """Check all the <ley_lines> to see if the move that was just
        applied claimed any of ley-lines. Return a dictionary where each
        key is an int that represents the ley-line that was claimed and the
        value is a string of which player claimed it.
        """
        ley_line_location = {}
        for ley_line in ley_lines:
            ley_line_num = self._get_ley_line_location(ley_line)
            # ley_lines[ley_line] is a list of one of the ley-lines
            if '@' not in ley_lines[ley_line]:
                continue
            ones, twos = 0, 0
            for i in range(len(ley_lines[ley_line])):
                if ley_lines[ley_line][i] == '1':
                    ones += 1
                elif ley_lines[ley_line][i] == '2':
                    twos += 1

            ley_line_length = len(ley_lines[ley_line]) - 1
            if ones / ley_line_length >= 0.5:
                ley_lines[ley_line][0] = 'p1'
                ley_line_location[ley_line_num] = 'p1'
            elif twos / ley_line_length >= 0.5:
                ley_lines[ley_line][0] = 'p2'
                ley_line_location[ley_line_num] = 'p2'
        return ley_line_location

    def _get_ley_line_location(self, ley_line: str) -> int:
        """Return the integer that occurs in <ley_line>.

        This is a helper function for _check_ley_markers.
        """
        nums = []
        for ch in ley_line:
            if ch.isdigit():
                nums.append(ch)
        str_val = ''.join(nums)
        return int(str_val)

    def _update_board(self, move: str,
                      ley_line_location: Dict[int, str]) -> List[List[str]]:
        """Return an updated version of attribute <self.board> based off
        <move> and <ley_lines>.

        Part 1: Apply the move by modifying the board.
        Part 2: Change any ley-line markers, IF needed.
        """
        new_board = deepcopy(self.board)
        if self.get_current_player_name() == 'p1':
            player = '1'
        else:
            player = '2'
        # Part 1:
        found = False
        while not found:
            for line in new_board:
                if self._update_board_part_1(move, player, line):
                    found = True

        # Part 2:
        for location, player in ley_line_location.items():
            self._update_board_part_2(location, player, new_board)
            # seen = 0
            # for board_line in new_board:
            #     for i in range(len(board_line)):
            #         if (board_line[i] == '@' or board_line[i] == 'p1' or
            #                 board_line[i] == 'p2'):
            #             seen += 1
            #             if seen == location:
            #                 board_line[i] = player

        return new_board

    def _update_board_part_1(self, move: str, player: str,
                             line: List[str]) -> bool:
        """Update the board by replacing <move> with the <player>
        that made the move. Return True iff <line> has been modified.
        """
        for i in range(len(line)):
            if line[i] == move:
                line[i] = player
                return True
        return False

    def _update_board_part_2(self, location: int, player: str,
                             new_board: List[List[str]]) -> None:
        """
        Helper function for _update_board
        """
        seen = 0
        for board_line in new_board:
            for i in range(len(board_line)):
                if (board_line[i] == '@' or board_line[i] == 'p1' or
                        board_line[i] == 'p2'):
                    seen += 1
                    if seen == location:
                        board_line[i] = player

    # def _update_board_part_2b(self, location: int, player: str, seen: int,
    #                           board_line: List[str], i: int) -> None:
    #     """
    #
    #     """
    #     if (board_line[i] == '@' or board_line[i] == 'p1' or
    #             board_line[i] == 'p2'):
    #         seen += 1
    #         if seen == location:
    #             board_line[i] = player

    # def _update_board_part_2b(self, location: int, player: str, seen: int,
    #                           board_line: List[str]) -> int:
    #     """Modify <board_line> at the '@' given by <location>
    #     with <player>. <seen> is the number of '@' symbols
    #     seen so far.
    #     """
    #     for i in range(len(board_line)):
    #         if (board_line[i] == '@' or board_line[i] == 'p1' or
    #                 board_line[i] == 'p2'):
    #             seen += 1
    #             if seen == location:
    #                 board_line[i] = player
    #     return seen

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).

        >>> shgs = StonehengeGameState(board_length=1)
        >>> shgs2 = StonehengeGameState(board_length=2)
        >>> shgs3 = StonehengeGameState(board_length=1)
        >>> repr(shgs) == repr(shgs2)
        False
        >>> repr(shgs) == repr(shgs3)
        True
        >>> print(repr(shgs))
        Current player: p1
        ley_line1: ['@', 'A']
        ley_line2: ['@', 'B', 'C']
        ley_line3: ['@', 'A', 'B']
        ley_line4: ['@', 'C']
        ley_line5: ['@', 'B']
        ley_line6: ['@', 'C', 'A']
        """
        res = ''
        if self.p1_turn:
            player = 'p1'
        else:
            player = 'p2'
        res += 'Current player: {}\n'.format(player)
        for ley_line in self.ley_lines:
            res += '{}: {}\n'.format(ley_line, self.ley_lines[ley_line])
        return res.strip()

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        >>> shgs = StonehengeGameState(board_length=1)
        >>> shgs2 = StonehengeGameState(board_length=2)
        >>> shgs.rough_outcome()
        1
        >>> shgs2.rough_outcome()
        0
        >>> new_state = shgs.make_move('A')
        >>> new_state.rough_outcome()
        -1
        """
        player, opponent = 'p1', 'p2'
        if player != self.get_current_player_name():
            player, opponent = 'p2', 'p1'

        if self._is_over(opponent):
            # Then the current player loses.
            return self.LOSE

        # for each move, check if the player that made the move won
        for move in self.get_possible_moves():
            new_state = self.make_move(move)  # opponent is the current player
            if self._is_over_player(new_state, player):
                return self.WIN

        for move in self.get_possible_moves():
            new_state = self.make_move(move)  # opponent is the current player
            for next_move in new_state.get_possible_moves():
                next_state = new_state.make_move(next_move)  # player
                if self._is_over_player(next_state, opponent):
                    return self.LOSE

            if self._is_over_player(new_state, opponent):
                return self.LOSE

        return self.DRAW

    def _is_over(self, opponent: str) -> bool:
        """Return true iff the game is over.
        """
        score = 0
        for board_line in self.board:
            for cell in board_line:
                if cell == opponent:
                    score += 1
        num_ley_lines = len(self.ley_lines)
        if score / num_ley_lines >= 0.5:
            return True
        return False

    def _is_over_player(self, state: 'StonehengeGameState',
                        player: str) -> bool:
        """Return true iff the game is over.
        """
        score = 0
        for board_line in state.board:
            for cell in board_line:
                if cell == player:
                    score += 1

        num_ley_lines = len(state.ley_lines)
        if score / num_ley_lines >= 0.5:
            return True

        return False

    # def is_over_v2(self) -> bool:
    #     """
    #     Return whether or not this game is over at state.
    #
    #     This method is to be used for the iterative strategy.
    #
    #     >>> sh = StonehengeGameState(board_length=1)
    #     >>> sh2 = StonehengeGameState(board_length=2)
    #     >>> sh_a = sh.make_move('A')
    #     >>> sh_b = sh2.make_move('B')
    #     >>> sh.is_over_v2()
    #     False
    #     >>> sh_a.is_over_v2()
    #     True
    #     >>> sh_b.is_over_v2()
    #     False
    #     """
    #     ones, twos = 0, 0
    #     for board_line in self.board:
    #         for ch in board_line:
    #             if ch == 'p1':
    #                 ones += 1
    #             elif ch == 'p2':
    #                 twos += 1
    #
    #     num_ley_lines = len(self.ley_lines)
    #     if ones / num_ley_lines >= 0.5:
    #         return True
    #     elif twos / num_ley_lines >= 0.5:
    #         return True
    #     return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
