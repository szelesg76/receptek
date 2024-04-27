from pydantic import BaseModel, Field
from typing import Optional


class Uzlet:
    def __init__(self, uzlet_id, uzlet_nev) -> None:
        self._uzlet_id: int = uzlet_id
        self._uzlet_nev: str = uzlet_nev

    def __str__(self) -> str:
        return f"{self._uzlet_id} - {self._uzlet_nev}"
    
    @property
    def uzlet_id(self) -> int:
        return self._uzlet_id
    
    @uzlet_id.setter 
    def uzlet_id(self, uj_uzlet_id):
        self._uzlet_id = uj_uzlet_id
    

class UzletRequest(BaseModel):
    """Üzlet osztály validálására használt osztály

    Args:
        BaseModel (_type_): Pydantic modul osztálya
    """
    uzlet_id: Optional[int] = Field(None, alias='uzlet_id:  nem kötelező mező')
    uzlet_nev: str = Field(min_length=3, max_length=25)
    
    class Config:
        json_schema_extra = {
            'example': {
                'uzlet_nev': 'Tesztüzlet'
            }
        }
