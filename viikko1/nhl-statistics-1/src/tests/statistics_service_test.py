import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_team_jos_pelaaja(self):
        pit = self.stats.team("PIT")
        self.assertEqual(pit[0].name, "Lemieux")

    def test_search_löytyy(self):
        pelaaja = self.stats.search("Gretzky")
        self.assertEqual(pelaaja.name, "Gretzky")

    def test_search_ei_löydy(self):
        pelaaja = self.stats.search("Muumi")
        self.assertIsNone(pelaaja)

    def test_top_points(self):
        pelaaja = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(pelaaja[0].points, 124)

    def test_top_goals(self):
        pelaaja = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(pelaaja[0].name, "Lemieux")

    def test_top_assists(self):
        pelaaja = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(pelaaja[1].name, "Yzerman")

        


