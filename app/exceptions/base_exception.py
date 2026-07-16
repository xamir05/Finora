class FinoraException(Exception):
    """
    Excepción base de toda la aplicación Finora.
    Todas las excepciones personalizadas deben heredar de esta clase.
    """

    def __init__(self, message: str):
        super().__init__(message)