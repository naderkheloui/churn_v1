from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict():
    """
    teste la route /predict
    """

    # Exemple de données d'entrée pour la prédiction
    test_data = {
        "Geolocalisation__Latitude__s": 45.3948035,
        "Geolocalisation__Longitude__s": 1.3785469,
        "pop_k1500m": 715.652075,
        "pop_k700m": 583.38352,
        "pop_k350m": 336.044399,
        "urban_dens": 88.706382,
        "nb_voisin_moins_200m": 0,
        "nb_voisin_moins_300m": 0,
        "nb_voisin_moins_2000m": 0
    }

    #Envoyer une requete POST a la route /predict
    reponse = client.post("/predict", json=test_data)

    # verifier le code statut
    assert reponse.status_code == 200


    # Verifier que la reponse contient un champ prediction
    assert "prediction" in reponse.json()