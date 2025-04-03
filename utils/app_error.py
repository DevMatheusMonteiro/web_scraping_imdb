class AppError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message, status_code)