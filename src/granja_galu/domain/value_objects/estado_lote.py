from enum import Enum


class EstadoLote(str, Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    EN_PREPARACION = "en_preparacion"
