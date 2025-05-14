from fastapi import FastAPI
from pydantic import BaseModel
from DEV.DataPrep.predict import predict_churn


#creer une instance de l API
app = FastAPI(title="Prediction churn", version="1.0")

# Model d entree - validation avec pydantic

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

# Commentaire issu d un collab
"""
code pour authentifier
code pour afficher des stat
"""
#prediction
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de churn prediction"}

@app.post("/predict") # route de prediction POST
def predict(input_data: ChurnInput):
    """
    Recoit des données churn et retourne la prediction 1 ou 0
    """
    data_dict = input_data.dict()
    prediction = predict_churn((data_dict))
    return prediction
