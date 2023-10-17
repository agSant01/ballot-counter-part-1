from typing import List


class FileManager():
    def __init__(self) -> None:
        pass

    def read_file(file_name: str) -> List[str]:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def write_file(file_name: str, lines: List[str]) -> None:
        file_to_write = open(file_name, 'w')
        file_to_write.writelines(lines)
        file_to_write.close()
        return
