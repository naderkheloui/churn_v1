import joblib
import numpy as np
import pandas as pd


def load_model(path='ModelEntraine/model_1.pkl'):
    """
    charger le model sauvegardé
    """

    return joblib.load(path)



def predict_churn(input_data):
    """
    Predit la probabilite de churn (0 ou 1) pour une observation
    input_data : dict ou dataframe des variable explicative
    """
    model = load_model()

    # Si input_data est un dict on transforme vers dataframe
    if isinstance(input_data,dict):
        input_data = pd.DataFrame([input_data])

    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)


    return{
        "prediction ": int(prediction[0]),
        "proba_0 " : float(proba[0][0]),
        "proba_1 " : float(proba[0][1])
    }



exemple = {
    "Geolocalisation__Latitude__s": 45.3948035,
    "Geolocalisation__Longitude__s": 1.3785469,
    "pop_k1500m": 715.652075,
    "pop_k700m": 583.38352,
    "pop_k350m": 336.044399,
    "urban_dens": 88.706382,
    "nb_voisin_moins_200m": 0,
    "nb_voisin_moins_300m": 0,
    "nb_voisin_moins_2000m": 0,
    "dist_voisin_1": 5.87817819,
    "dist_voisin_2": 14.90277636,
    "dist_voisin_3": 15.11298694,
    "mois_actuel": 6,
    "PUDO delivery_m_1": 369,
    "PUDO delivery_m_2": 343,
    "PUDO delivery_m_3": 327,
    "Dropoff_m_1": 75,
    "Dropoff_m_2": 62,
    "Dropoff_m_3": 80,
    "nb_fermeture_annuel_pocket_dropoff": 0,
    "nb_fermeture_annuel_deferred_dropoff": 0,
    "nb_fermeture_annuel_deferred_delivery": 0,
    "nb_fermeture_annuel_pocket_delivery": 0,
    "nb_fermeture_annuel_delivery": 0,
    "nb_fermeture_annuel_stuart re-delivry": 0,
    "nb_fermeture_annuel_fresh_delivery": 0,
    "nb_fermeture_annuel_mail_delivery": 0,
    "nb_fermeture_3_last_months_pocket_dropoff": 0,
    "nb_fermeture_3_last_months_deferred_dropoff": 0,
    "nb_fermeture_3_last_months_deferred_delivery": 0,
    "nb_fermeture_3_last_months_pocket_delivery": 0,
    "nb_fermeture_3_last_months_delivery": 0,
    "nb_fermeture_3_last_months_stuart re-delivry": 0,
    "nb_fermeture_3_last_months_fresh_delivery": 0,
    "nb_fermeture_3_last_months_mail_delivery": 0,
    "dropoff_1_3": 217,
    "dropoff_ANNUEL": 742,
    "PUDO delivery_1_3": 1039,
    "PUDO delivery_ANNUEL": 3642
}

resultat = predict_churn(exemple)
print(resultat)