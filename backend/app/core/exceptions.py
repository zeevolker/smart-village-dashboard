class AppException(Exception):
    """
    Base application exception.
    """

    def __init__(
        self,
        message: str,
        status_code: int = 400,
    ):
        self.message = message
        self.status_code = status_code


class NotFoundException(AppException):

    def __init__(
        self,
        message: str = "Resource not found",
    ):
        super().__init__(
            message,
            status_code=404,
        )


class BadRequestException(AppException):

    def __init__(
        self,
        message: str,
    ):
        super().__init__(
            message,
            status_code=400,
        )
        
class ConflictException(AppException):
    """
    Conflict exception.
    """

    def __init__(
        self,
        message: str,
    ):
        super().__init__(
            message=message,
            status_code=409,
        )