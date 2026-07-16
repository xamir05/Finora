from app.exceptions.base_exception import FinoraException


class ValidationException(FinoraException):
    """
    Se lanza cuando los datos ingresados por el usuario no son válidos.
    """

    pass