import json
import random
import time

from typing import Optional


class Player:

    def __init__(self,
                 name: str,
                 symbol: Optional[str] = None,
                 *args,
                 **kwargs):
        self.name = name
        self.symbol = symbol
        self._scores = {}


class WelcomeMixin:

    def __init__(self, *args, **kwargs):
        self._default_filename = 'scores.json'
        self._scores = {}
        self._load_scores()
        self._introduce_players()
        self._show_scores()

    def _introduce_players(self) -> None:
        if not self._players:
            name = input("Welcome to TicTacToe! Please enter your name: ")
            player = Player(name)
            self._players.append(player)
            self._select_symbol(player)
        else:
            second_player_name = input("And the name of the second player: ")
            is_valid, second_name = self._validate_player_names(
                self._players[0].name,
                second_player_name
            )
            if is_valid:
                second_player = Player(
                    name=second_name,
                    symbol=self._symbols.pop()
                )
                self._players.append(second_player)
                print("Someone else has selected a symbol first.")
                print(
                    f"{second_player.name} is stuck with \
                    {second_player.symbol}"
                )
            time.sleep(2)

    def _validate_player_names(self, first_player_name, second_player_name):
        if first_player_name == second_player_name:
            print("That'll get confusing fast. Please us another name.")
            newname = input("Let's try again. Your name is: ")
            self._validate_player_names(first_player_name, newname)
            return True, newname
        else:
            return True, second_player_name

    def _select_symbol(
            self,
            player: Player) -> None:
        symbol = input(f"Hey, {player.name}. Choose your destiny: X or O?: ")
        self._validate_symbol(symbol, player)

    def _validate_symbol(
            self,
            symbol: str,
            player: Player
    ) -> None:
        if symbol.upper() in self._symbols:
            descriptions = ["wisely", "unwisely", "artfully",
                            "skillfully", "proudly", "smartly",
                            "quickly"]
            player.symbol = symbol
            self._symbols.remove(symbol.upper())
            print(f"You have chosen... {random.choice(descriptions)}")
            time.sleep(3.5)
            print(f"Just kidding. {player.name} picked {symbol}.")
            time.sleep(1)
            self._introduce_players()
        else:
            print(
                f"That's not on tap right now, bub. \
                Your options are {self._symbols}"
            )
            self._select_symbol(player)

    def _load_scores(self) -> None:
        try:
            with open(self._default_filename, 'r') as scoreboard:
                self._scores = json.loads(scoreboard.read())
        except FileNotFoundError:
            self._create_new_scores_file()

    def _create_new_scores_file(self) -> None:
        print(
            "Thank you for using TicTacToe for the first time. \
        Setting up score tracking..."
        )
        with open(self._default_filename, "w") as new_scores:
            new_scores.write('{}')

    def _show_scores(self):
        if self._scores:
            for player in self._players:
                player_score = self._scores.get(player.name)
                if player_score:
                    print(
                        f"Beware: {player.name} has a score of {player_score}"
                    )
            print("Hall of fame: ")
            for key, value in self._scores.items():
                print(f"{key}: {value} wins")

    def _update_scores(self, winner_name):
        if winner_name in self._scores.keys():
            self._scores[winner_name] += 1
        else:
            self._scores[winner_name] = 1
        with open(self._default_filename, 'w') as scores:
            scores.write(json.dumps(self._scores))

    def _provide_wisdom(self):
        with open('way_of_mrs_cosmopolite.txt', 'r') as wisdom:
            data = wisdom.readlines()
        selected_nugget_of_the_infinity = random.randint(0, len(data))
        return data[selected_nugget_of_the_infinity]
