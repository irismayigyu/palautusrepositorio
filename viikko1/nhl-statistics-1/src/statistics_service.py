

from enum import Enum
class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def top(self, how_many, sort_by=None):
        if sort_by == SortBy.POINTS:
            sorted_players = sorted(
                self._players,
                key=lambda player: player.points,
                reverse=True
            )
        elif sort_by == SortBy.GOALS:
            sorted_players = sorted(
                self._players,
                key=lambda player: player.goals,
                reverse=True
            )

        elif sort_by == SortBy.ASSISTS:
            sorted_players = sorted(
                self._players,
                key=lambda player: player.assists,
                reverse=True
            )
        else:
            sorted_players = sorted(
                self._players,
                key=lambda player: player.points,
                reverse=True
            )

        return sorted_players[:how_many]


