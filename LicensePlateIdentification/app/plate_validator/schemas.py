from pydantic import BaseModel

class Plate(BaseModel):
    plate_number: str
