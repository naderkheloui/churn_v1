# app/main.py

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.schemas import ChurnInput
from app.predict import predict_churn
from app.gradio import get_gradio_interface
import gradio as gr

app = FastAPI()

@app.post("/predict")
def predict(input_data: ChurnInput):
    data_dict = input_data.dict()
    prediction = predict_churn(data_dict)
    return prediction

@app.get("/")
def root():
    return RedirectResponse(url="/gradio")

# Monter l'interface Gradio sur le chemin '/gradio'
gradio_app = get_gradio_interface()
app = gr.mount_gradio_app(app, gradio_app, path="/gradio")
