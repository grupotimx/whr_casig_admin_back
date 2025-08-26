from pydantic import BaseModel

class CSVLoadResult(BaseModel):
    mensaje: str
    dataset: str
    total: int
