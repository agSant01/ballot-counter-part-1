from d_linked_list.dllist import DoubleLinkedList
from array_list.array import ArrayList
from candidate import Candidate
from ballot import Ballot

# Number of 1’s that the candidate received at the moment of elimination
# - Round in which the candidate was eliminated.
# - Use the following format: Round #: <Candidate name here> was eliminated with n #1’


class Round:
    def __init__(self, roundNumber, oneVotes, candidate: Candidate) -> None:
        self.oneVotes = oneVotes
        self.roundNumber = roundNumber
        self.candidate = candidate

    def __str__(self) -> str:
        return f"Round {self.roundNumber}: {self.candidate.name} was eliminated with {self.oneVotes} #1's"


class ProcessBallots():
    def __init__(self, ballots: DoubleLinkedList, candidates: DoubleLinkedList) -> None:
        self.ballots = ballots
        self.candidates = candidates
        self.rounds = []
        self.winner = None

    def run(self):
        votesPerRank = ArrayList()
        while True:
            vote_count = 0
            rank = 0
            for ballot in self.ballots:
                pass

    def getRounds():
        pass
