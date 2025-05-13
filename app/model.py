# app/model.py

import os
import pickle
import joblib


def load_model():
    """
    Charge le modèle entraîné depuis le fichier .pkl.
    Le chemin est calculé dynamiquement pour être robuste à l'exécution.
    """
    model = joblib.load('ModelEntraine/model_0.pkl')

    return model
