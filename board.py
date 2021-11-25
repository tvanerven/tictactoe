import re


class TicTacToeSquare:

    def __init__(
            self,
            value: str,
    ):
        self._value = str(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def is_marked(self):
        if self._value.upper() in ['X', 'O']:
            return True
        return False


class TicTacToeBoard:

    def __init__(
            self,
            size: int
    ):
        self.size = size * size
        self._squares = {}
        self._create_board()
        self._active_square = 0

    def _create_board(self) -> None:
        for i in range(self.size):
            self._squares[i] = TicTacToeSquare(value=i+1)

    @property
    def selected_square_value(self):
        selected_square = self.selected_square
        return self._squares[selected_square].value

    @selected_square_value.setter
    def selected_square_value(self, value):
        selected_square = self.selected_square
        self._squares[selected_square].value = value

    def set_square_value(self, choice, symbol):
        index = int(choice) - 1
        self._squares[index].value = symbol

    def _do_we_have_a_winner(self):
        value_string = ''.join(
            square.value for square in self._squares.values()
        )
        row_win, row_string = self._check_rows(value_string)
        column_win, column_string = self._check_columns(value_string)
        diagonal_win, diagonal_string = self._check_diagonals(value_string)
        if row_win:
            winner_symbol = row_string[0]
            return True, winner_symbol
        if column_win:
            is_even = column_string % 2
            if is_even == 0:
                return True, 'X'
            return True, 'O'
        if diagonal_win:
            is_even = diagonal_string % 2
            if is_even == 0:
                return True, 'X'
            return True, 'O'
        return False, ''

    def _is_tie(self):
        value_string = ''.join(
            square.value for square in self._squares.values()
        )
        match = re.search(r'\d', value_string)
        if match:
            return False
        return True

    def _check_rows(self, value_string):
        victory_strings = ['OOO', 'XXX']
        for string in victory_strings:
            if string in value_string:
                return True, string
        return False, value_string

    def _check_columns(self, value_string):
        valid_matches = {
            1: 'X..X..X..',
            3: '.X..X..X.',
            5: '..X..X..X',
            2: 'O..O..O..',
            4: '.O..O..O.',
            6: '..O..O..O',
        }
        win = False
        key = None
        for key, match in valid_matches.items():
            result = re.search(r''.join(match), value_string)
            if result:
                win = True
                key = key
        if win:
            return win, key
        return win, value_string

    def _check_diagonals(self, value_string):
        valid_matches = {
            1: 'X...X...X',
            3: '..X.X.X..',
            2: 'O...O...O',
            4: '..O.O.O..',
        }
        win = False
        key = None
        for key, match in valid_matches.items():
            result = re.search(r''.join(match), value_string)
            if result:
                win = True
                key = key
        if win:
            return win, key
        return win, value_string

    def print_board(self):
        separator = '-+---+---+---|-'
        frame = '--------------------'
        self._squares[0].selected = True
        print("YOUR CURRENT BOARD: ")
        print(frame)
        print(
            ' | '
            + self._squares[0].value
            + ' | '
            + self._squares[1].value
            + ' | '
            + self._squares[2].value
            + ' | '
        )
        print(separator)
        print(
            ' | '
            + self._squares[3].value
            + ' | '
            + self._squares[4].value
            + ' | '
            + self._squares[5].value
            + ' | '
        )
        print(separator)
        print(
            ' | '
            + self._squares[6].value
            + ' | '
            + self._squares[7].value
            + ' | '
            + self._squares[8].value
            + ' | '
        )
        print(frame)
