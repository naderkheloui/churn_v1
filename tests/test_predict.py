from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    """
    teste la route /predict
    """

    # Exemple de données d'entrée pour la prédiction
    test_data = {
        "Geolocalisation__Latitude__s": 45.39,
        "Geolocalisation__Longitude__s": 1.37,
        "pop_k1500m": 715.6,
        "pop_k700m": 583.3,
        "pop_k350m": 336.0,
        "urban_dens": 88.7,
        "nb_voisin_moins_200m": 0,
        "nb_voisin_moins_300m": 0,
        "nb_voisin_moins_2000m": 0,
        "dist_voisin_1": 5.87,
        "dist_voisin_2": 14.90,
        "dist_voisin_3": 15.11,
        "mois_actuel": 6,
        "PUDO_delivery_m_1": 369,
        "PUDO_delivery_m_2": 343,
        "PUDO_delivery_m_3": 327,
        "Dropoff_m_1": 75,
        "Dropoff_m_2": 62,
        "Dropoff_m_3": 80,
        "nb_fermeture_annuel_pocket_dropoff": 0,
        "nb_fermeture_annuel_deferred_dropoff": 0,
        "nb_fermeture_annuel_deferred_delivery": 0,
        "nb_fermeture_annuel_pocket_delivery": 0,
        "nb_fermeture_annuel_delivery": 0,
        "nb_fermeture_annuel_stuart_re_delivry": 0,
        "nb_fermeture_annuel_fresh_delivery": 0,
        "nb_fermeture_annuel_mail_delivery": 0,
        "nb_fermeture_3_last_months_pocket_dropoff": 0,
        "nb_fermeture_3_last_months_deferred_dropoff": 0,
        "nb_fermeture_3_last_months_deferred_delivery": 0,
        "nb_fermeture_3_last_months_pocket_delivery": 0,
        "nb_fermeture_3_last_months_delivery": 0,
        "nb_fermeture_3_last_months_stuart_re_delivry": 0,
        "nb_fermeture_3_last_months_fresh_delivery": 0,
        "nb_fermeture_3_last_months_mail_delivery": 0,
        "dropoff_1_3": 217,
        "dropoff_ANNUEL": 742,
        "PUDO_delivery_1_3": 1039,
        "PUDO_delivery_ANNUEL": 3642
    }

    #Envoyer une requete POST a la route /predict
    reponse = client.post("/predict", json=test_data)

    # verifier le code statut
    assert reponse.status_code == 200


    # Verifier que la reponse contient un champ prediction
    assert "prediction" in reponse.json()