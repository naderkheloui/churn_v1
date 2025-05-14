# app/gradio_ui.py

import gradio as gr
from app.predict import predict_churn

# Fonction qui prend les entrées de Gradio et appelle la fonction de prédiction
def gradio_predict(Geolocalisation__Latitude__s, Geolocalisation__Longitude__s, pop_k1500m, pop_k700m,
                   pop_k350m, urban_dens, nb_voisin_moins_200m, nb_voisin_moins_300m, nb_voisin_moins_2000m):
    # Créer un dictionnaire avec les données d'entrée
    input_data = {
        "Geolocalisation__Latitude__s": Geolocalisation__Latitude__s,
        "Geolocalisation__Longitude__s": Geolocalisation__Longitude__s,
        "pop_k1500m": pop_k1500m,
        "pop_k700m": pop_k700m,
        "pop_k350m": pop_k350m,
        "urban_dens": urban_dens,
        "nb_voisin_moins_200m": nb_voisin_moins_200m,
        "nb_voisin_moins_300m": nb_voisin_moins_300m,
        "nb_voisin_moins_2000m": nb_voisin_moins_2000m
    }

    # Appeler la fonction de prédiction
    result = predict_churn(input_data)

    # Retourner la prédiction
    return f"Prédiction : {result['prediction']}"

# Créer l'interface Gradio
def get_gradio_interface():
    return gr.Interface(
        fn=gradio_predict,
        inputs=[
            gr.Number(label="Latitude"),
            gr.Number(label="Longitude"),
            gr.Number(label="pop_k1500m"),
            gr.Number(label="pop_k700m"),
            gr.Number(label="pop_k350m"),
            gr.Number(label="urban_dens"),
            gr.Number(label="nb_voisin_moins_200m"),
            gr.Number(label="nb_voisin_moins_300m"),
            gr.Number(label="nb_voisin_moins_2000m")
        ],
        outputs=gr.Textbox(label="Prédiction"),
        title="Interface de Prédiction de Churn",
        description="Entrez les données pour obtenir une prédiction."
    )
