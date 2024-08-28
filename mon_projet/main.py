from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import joblib
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Charger le modèle et le scaler utilisés lors de l'entraînement
model = joblib.load('model_real.pkl')
scaler = joblib.load('scaler_real.pkl')

# Assurer que  dossier 'uploads/' existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Lire le fichier Excel téléchargé
        df = pd.read_excel(filepath)

        # Préparer les données pour le modèle
        critical_parameters = [
            'Débit d\'aspiration', 'vitesse moteur', 'PI 900\nPERTE DE CHARGE DE L\'UNITEE',
            'pression de refoulement', 'température duct de refoulement'
        ]

        if all(param in df.columns for param in critical_parameters):
            X = df[critical_parameters]
            X_normalized = scaler.transform(X)

            # Prédire la performance
            predictions = model.predict(X_normalized)

            # Afficher les prédictions 
            print("Prédictions du modèle:", predictions)

            # Calculer la moyenne des prédictions
            average_prediction = predictions.mean()

            # Normaliser la prédiction pour qu'elle soit entre 0 et 100%
            max_prediction = predictions.max()  # Utiliser la prédiction maximale réelle
            min_prediction = predictions.min()  # Utiliser la prédiction minimale réelle
            normalized_performance = (average_prediction - min_prediction) / (max_prediction - min_prediction) * 100
            normalized_performance = max(0, min(100, normalized_performance))

            # Retourner la prédiction au format HTML
            return render_template('index.html', prediction=f"{round(normalized_performance, 1)}%")
        else:
            return "Le fichier ne contient pas les colonnes nécessaires."

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
