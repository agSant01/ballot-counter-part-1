from file_manager import FileManager


class InputData():
    def __init__(self, file_manager: FileManager, file_name: str) -> None:
        self.file_manager = file_manager
        self.file_name = file_name
