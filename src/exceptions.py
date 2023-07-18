class BaseFileError(Exception):
    def __init__(self, message: str):
        self.message: str = message


class InstantiateCSVError(BaseFileError):
    def __init__(self, message: str):
        super().__init__(message)


class CSVFileNotFound(BaseFileError):
    def __init__(self, message: str):
        super().__init__(message)
