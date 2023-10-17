from typing import List

from election import Round


class ElectionStats():
    def __init__(self) -> None:
        self.invalid_ballots: int = 0
        self.blank_ballots: int = 0
        self.total_ballots: int = 0
        self.rounds: List[Round] = []
        self.winner = None

    def setInvalidBallot(self, invalid_ballots: int):
        self.invalid_ballots = invalid_ballots

    def setBlankBallot(self, blank_ballots: int):
        self.blank_ballots = blank_ballots

    def setTotalBallot(self, total_ballots: int):
        self.total_ballots = total_ballots
