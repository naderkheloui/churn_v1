# app/schemas.py

from pydantic import BaseModel

class ChurnInput(BaseModel):
    Geolocalisation__Latitude__s: float
    Geolocalisation__Longitude__s: float
    pop_k1500m: float
    pop_k700m: float
    pop_k350m: float
    urban_dens: float
    nb_voisin_moins_200m: int
    nb_voisin_moins_300m: int
    nb_voisin_moins_2000m: int