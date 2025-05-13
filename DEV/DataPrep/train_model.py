import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from DEV.DataPrep.data_prep import load_and_prepare_data

def train_and_save_model():

    # Chargement des données
    X_train, X_test, y_train, y_test = load_and_prepare_data()
    # Pipeline: Standardisation + model RF

    pipeline = Pipeline([
        ('scaler', StandardScaler()), #pour normaliser
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))# Model
    ])


    # Entrainement du model
    pipeline.fit(X_train,y_train)


    # Prediction sur le set de test
    y_pred = pipeline.predict(X_test)


    #Evaluation
    print("Rapport de classification: ")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test,y_pred):.2f}")


    # Sauvegarder le model
    joblib.dump(pipeline, '../ModelEntraine/model_1.pkl')


if __name__ == "__main__":
    train_and_save_model()

