from app.exceptions.base_exception import FinoraException


class DatabaseException(FinoraException):
    """
    Se lanza cuando ocurre un error relacionado con la base de datos.
    """

    pass