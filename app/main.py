# app/main.py

from fastapi import FastAPI
from app.schemas import ChurnInput
from app.predict import predict_churn

app = FastAPI()

@app.post("/predict")
def predict(input_data: ChurnInput):
    """
    Reçoit des données de churn et retourne la prédiction du modèle.
    """
    data_dict = input_data.dict()  # Convertir l'objet Pydantic en dictionnaire
    prediction = predict_churn(data_dict)  # Appeler la fonction de prédiction
    return prediction

@app.get("/")
def read_root():
    """
    Point d'entrée de l'API, retourne un message de bienvenue.
    """
    return {"message": "Bienvenue sur l'API de churn prediction"}

@app.get("/favicon.ico")
def favicon():
    """
    Empêche l'erreur liée à la recherche du favicon.ico
    """
    return {}
