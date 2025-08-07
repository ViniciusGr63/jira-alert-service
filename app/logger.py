# Configuração de logs

from loguru import logger
import os

os.makedirs("logs", exist_ok=True)
logger.add("logs/servico.log", rotation="1 MB", level="INFO")
