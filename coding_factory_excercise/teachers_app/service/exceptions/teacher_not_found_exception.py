class TeacherNotFoundError(Exception):
    def __init__(self):
        super().__init__(f"Teacher does not exist.")