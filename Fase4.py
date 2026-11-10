import logging
import math
import re
import sys
from abc import ABC, abstractmethod
from datetime import datetime


# =============================================================
# 1. CONFIGURACIÓN DEL REGISTRO DE EVENTOS Y ERRORES
# =============================================================

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    manejador = logging.FileHandler(
        "software_fj.log",
        mode="a",
        encoding="utf-8"
    )
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    """Registra un evento informativo."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra un error sin traza de excepción."""
    logger.error(mensaje)

def registrar_excepcion(mensaje):
    """Registra el error y la traza de la excepción actual."""
    logger.exception(mensaje)


  
    logger.exception
