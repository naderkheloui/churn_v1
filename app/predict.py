# app/predict.py

from app.model import load_model

# Charge une seule fois le modèle
model = load_model()


def predict_churn(input_data: dict):
    """
    Effectue une prédiction de churn en utilisant le modèle chargé.
    """
    # On transforme l'entrée en array ou DataFrame selon le modèle (ici c'est un dictionnaire)
    import pandas as pd
    input_df = pd.DataFrame([input_data])

    # Prédiction
    prediction = model.predict(input_df)

    return {"prediction": int(prediction[0])}  # Renvoie le résultat de la prédiction sous forme de dictionnaire
