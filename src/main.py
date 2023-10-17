from typing import List
from d_linked_list import dllist
from file_manager import FileManager
from ballot import Ballot
from candidate import Candidate

INPUT_FILE_NAME = 'test1.csv'


def get_candidate_data(fm: FileManager):
    candidates_list = dllist.DoubleLinkedList()

    candidates_str: List[str] = fm.read_file('../data/candidates.csv')

    for candidate in candidates_str:
        candidates_list.append(Candidate.parseCandidate(candidate))

    return candidates_list


def get_ballots_data(fm: FileManager, max_rank):
    ballots = dllist.DoubleLinkedList()
    invalid_ballots = 0

    ballots_str: List[str] = fm.read_file('../data/ballots.csv')

    for ballot in ballots_str:
        try:
            ballots.append(Ballot.parseBallot(ballot, max_rank))
        except:
            pass

    return ballots


def main():
    fm = FileManager()

    candidate_list: dllist.DoubleLinkedList = get_candidate_data(fm)
    max_rank = candidate_list.count
    ballots_data: dllist.DoubleLinkedList = get_ballots_data(fm, max_rank)

    # dll = dllist.DoubleLinkedList()

    # dll.append(1)
    # dll.append(2)
    # dll.append(3)

    # print(dll)


if __name__ == '__main__':
    main()
