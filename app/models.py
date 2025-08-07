# Schemas Pydantic
from pydantic import BaseModel

class Alerta(BaseModel):
    titulo: str
    descricao: str
