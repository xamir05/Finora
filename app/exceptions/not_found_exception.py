from app.exceptions.base_exception import FinoraException


class NotFoundException(FinoraException):
    """
    Se lanza cuando un recurso solicitado no existe.
    """

    pass