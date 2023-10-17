from typing_extensions import Self


class InvalidCandidateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Candidate():
    def __init__(self, candidateID, name) -> None:
        self.candidateID = candidateID
        self.name = name
        self.eliminated = False

    @staticmethod
    def parseCandidate(candidate_string: str) -> Self:
        parts = candidate_string.split(',')
        if len(parts) != 2:
            raise InvalidCandidateException()

        return Candidate(int(parts[0]), parts[1])

    def __str__(self) -> str:
        return f"<Candidate id={self.id}, name={self.name}, eliminated={self.eliminated} >"
