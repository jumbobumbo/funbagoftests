
class ScoreTennis:
    def __init__(self):
        self.score_dict = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
            4: "deuce",
            5: "advantage",
        }
        self.player_scores = {
            "player_one": 0,
            "player_two": 0,
        }

    def point_change_verify_result(self, player: str, add_point: bool = True):
        """
        verifies what how points need to be changed for a player
        :param player: str
        :param add_point: bool
        :return:
        """
        other_player = "player_two" if player == "player_one" else "player_one"
        if add_point:
            # check scores first
            if self.player_scores[player] == 3 and self.player_scores[other_player] < 3:
                self._win(player, other_player)
            elif self.player_scores[player] == 5 and self.player_scores[other_player] == 4:
                self._win(player, other_player)
            else:
                self.player_scores[player] += 1
                if self.player_scores[player] == 3 and self.player_scores[other_player] == 3:
                    self.player_scores[player] += 1
                    self.player_scores[other_player] += 1
                self._current_score()
        elif not add_point:
            self.player_scores[player] -= 1
            self._current_score()

    def _win(self, winner: str, loser: str):
        print(f"{winner} wins!\n"
              f"score:\n"
              f"{winner}: {self.score_dict[self.player_scores[winner]]}\n"
              f"{loser}: {self.score_dict[self.player_scores[loser]]}")

    def _current_score(self):
        for tennis_player in self.player_scores.keys():
            print(f"{tennis_player}: {self.score_dict[self.player_scores[tennis_player]]}")
