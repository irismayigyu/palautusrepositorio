import unittest
from statistics_service import StatisticsService
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

    def test_top(self):
        pelaaja = self.stats.top(1)
        self.assertEqual(pelaaja[0].points, 124)
        


