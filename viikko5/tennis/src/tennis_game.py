class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.score_difference = 0

    def won_point(self, player):
        if player == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        self.score = ""

        if self.player1_score == self.player2_score:
            self.draw(self.player1_score)

        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.score_difference = self.player1_score - self. player2_score
            self.over_three_points()

        else:
            self.under_deuce()

        return self.score

    def under_deuce(self):
        points = 3
        for point in range(1, points):
            if point == 1:
                temp_score = self.player1_score
            else:
                self.score = self.score + "-"
                temp_score = self.player2_score

            if temp_score == 0:
                self.score = self.score + "Love"
            elif temp_score == 1:
                self.score = self.score + "Fifteen"
            elif temp_score == 2:
                self.score = self.score + "Thirty"
            elif temp_score == 3:
                self.score = self.score + "Forty"

    def draw(self, player1_score):
        if player1_score == 0:
            self.score = "Love-All"
        elif player1_score == 1:
            self.score = "Fifteen-All"
        elif player1_score == 2:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"

    def over_three_points(self):
        if self.score_difference == 1:
            self.score = "Advantage player1"
        elif self.score_difference == -1:
            self.score = "Advantage player2"
        elif self.score_difference >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"
