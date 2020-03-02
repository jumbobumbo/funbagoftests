
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

    def point_change_verify_result(self, player: str):
        """
        verifies what how points need to be changed for a player
        :param player: str
        :return:
        """
        other_player = "player_two" if player == "player_one" else "player_one"
        # check the scores
        # player is enough points ahead to just win
        if self.player_scores[player] == 3 and self.player_scores[other_player] < 3:
            self._win(player, other_player)
        # player has one the advantage
        elif self.player_scores[player] == 5 and self.player_scores[other_player] == 4:
            self._win(player, other_player)
        # player has lost the advantage
        elif self.player_scores[player] == 4 and self.player_scores[other_player] == 5:
            self.player_scores[other_player] -= 1
            self._current_score()
        else:
            self.player_scores[player] += 1  # add the point
            # both players are on 40 - deuce time
            if self.player_scores[player] == 3 and self.player_scores[other_player] == 3:
                for x in [player, other_player]:
                    self.player_scores[x] += 1
            self._current_score()

    def _win(self, winner: str, loser: str):
        """
        prints out winning player
        :param winner: str
        :param loser: str
        :return:
        """
        print(f"final score:\n"
              f"{winner} wins!\n"
              f"{winner}: {self.score_dict[self.player_scores[winner]]}\n"
              f"{loser}: {self.score_dict[self.player_scores[loser]]}")

    def _current_score(self):
        """
        prints out the current game score
        :return:
        """
        print("current score:")
        for tennis_player in self.player_scores.keys():
            print(f"{tennis_player}: {self.score_dict[self.player_scores[tennis_player]]}")


if __name__ == "__main__":
    game = ScoreTennis()
    game.point_change_verify_result("player_one")
    for _ in range(4):
        game.point_change_verify_result("player_two")
