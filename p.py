
class Ballot:
    def __init__(self, id, votes) -> None:
        self.id = id
        self.votes = votes

    @staticmethod
    def parseBallot(string_):
        sep_list = string_.split(',')
        id_ = int(sep_list[0])
        canditate_list = sep_list[1:]
        print(canditate_list)
        votes = []
        for cid_rank in canditate_list:
            cid, rank = cid_rank.split(':')
            votes.append((int(cid), int(rank)))
        return Ballot(id_, votes)

    def __str__(self) -> str:
        return f'<Ballot id={self.id} votes={self.votes}>'


a = "278,4:1,3:2,2:3,5:4,1:5"
ballots = Ballot.parseBallot(a)

print(ballots)
