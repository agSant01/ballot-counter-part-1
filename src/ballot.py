from typing import List
from typing_extensions import Self
from array_list.array import ArrayList


class InvalidBallotException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Ballot():
    def __init__(self, id: int, rankedCandidates: ArrayList) -> None:
        self.ballotNum = None
        self.rankedCandidates = rankedCandidates

    # public int getBallotNum(); // returns the ballot number
    def getBallotNum(self):
        return self.ballotNum

    # public int getRankByCandidate(int candidateID); // rank for that candidate
    def getRankByCandidate(self, candidateID: int) -> int:
        return self.rankedCandidates.getElement(candidateID)

    # public int getCandidateByRank(int rank); // candidate with that rank
    def getCandidateByRank(self, rank: int) -> int:
        pass

    # public boolean eliminate(int candidateId); // eliminates a candidate
    def elimintate(self, candidateID: int) -> bool:
        return self.rankedCandidates.remove(candidateID)

    @staticmethod
    def parseBallot(ballot_string: str, maxRank: int) -> Self:
        # ballot#,c1:1,c2:2,…,ck:
        split = ballot_string.split(',')

        ballot_id = int(split[0])

        rankedCandidates = ArrayList()

        for _ in range(len(split)):
            rankedCandidates.append(None)

        for vote in split:
            candidateID, rank = vote
            if rank > maxRank:
                raise InvalidBallotException()

            rankedCandidates.insert(candidateID, rank)

        return Ballot(ballot_id, rankedCandidates)


"""
Ballots
You must create a Ballot class,such that an instance of this class can store all of the information
regarding a single ballot. It must contain the ballot number as well as a List to contain the votes
that were cast in that ballot (you can use more than one List if you wish, but technically you can
do it with only one). How you use the list(s) and what you store in them is up to you. Your Ballot
class must contain at least the following methods:
    
public int getBallotNum(); // returns the ballot number
public int getRankByCandidate(int candidateID); // rank for that candidate
public int getCandidateByRank(int rank); // candidate with that rank
public boolean eliminate(int candidateId); // eliminates a candidate

An interface will be provided in the initial code, which you’ll have to implement in your Ballot
class. 
Inside the actual Ballot class, create a constructor such that you could pass the line of text from
the input file and then theconstructor would take care of storing the information accordingly.
You may create as many additional methods as you deem necessary and/or helpful.
"""
