from mixins import WelcomeMixin
from board import TicTacToeBoard


class TicTacToeGame(WelcomeMixin):

    def __init__(self, *args, **kwargs):
        self._symbols = ['O', 'X']
        self._players = []
        self._mark_made = False
        self._active_player = None
        self._board = TicTacToeBoard(size=3)
        self._turn_counter = 0
        super().__init__()
        self._start_game()

    def _start_game(self):
        print("Let the games begin...")
        first_player = self._players[0]
        self._active_player = first_player
        self._play_turn(self._active_player)

    def _play_turn(self, player):
        print("---------------------------")
        print(f"It's {player.name}'s turn.")
        print("---------------------------")
        has_moved = self._mark_square(player)
        while not has_moved:
            self._mark_square(player)
        self._turn_counter += 1
        self._check_board()
        self._mark_other_player_active()
        self._play_turn(player=self._active_player)

    def _mark_other_player_active(self):
        other_player = set(self._players) - set([self._active_player])
        self._active_player = other_player.pop()

    def _check_board(self):
        victory = False
        if self._turn_counter >= 5:
            victory, winner = self._board._do_we_have_a_winner()
            is_tie = self._board._is_tie()
            if is_tie:
                print("Unfortunately, there is a tie. No winner is declared.")
                self._ask_replay()
        if victory:
            self._engage_party(winner)
            self._ask_replay()

    def _ask_replay(self):
        replay = input("Do you want to replay? (y/n): ")
        if replay.lower() == 'y':
            main()
        else:
            print("Thank you for playing.")
            exit()

    def _engage_party(self, winner):
        winner_symbol = winner[0]
        winning_player = [
            player for player in self._players
            if player.symbol == winner_symbol
        ]
        winner_name = winning_player[0].name
        self._update_scores(winner_name)
        print(f"It is done! {winner_name} has seen, come, and conquered!")
        print("His name will be sung for eons in the hall of fame.")
        print("As a victor's gift, I bestow the wisdom of the ages: ")
        print("Wise ones say: ")
        print(self._provide_wisdom())

    def _mark_square(self, player):
        self._board.print_board()
        print("Choose a field to mark.")
        choice = input("Your destiny: ")
        valid_mark = self._validate_mark(choice)
        while not valid_mark:
            self._mark_square(player=self._active_player)
        self._board.set_square_value(
            choice,
            self._active_player.symbol
        )
        return True

    def _validate_mark(self, choice):
        if (int(choice)-1) not in [i for i in range(0, 9)] or choice == '':
            print("That's not a valid squre.")
            return False
        square = self._board._squares[int(choice) - 1]
        if square.is_marked:
            print("That square is already marked!")
            return False
        else:
            return True


def main():
    print("Starting Tic. Tac. Toe.")
    TicTacToeGame()


if __name__ == "__main__":
    main()
