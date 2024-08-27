document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Récupérer les valeurs des champs du formulaire
    const debit = document.getElementById('debit').value;
    const vitesse = document.getElementById('vitesse').value;
    const perte = document.getElementById('perte').value;
    const pression = document.getElementById('pression').value;
    const temperature = document.getElementById('temperature').value;

    // Créer l'objet de données à envoyer
    const data = {
        "Débit d'aspiration": parseFloat(debit),
        "vitesse moteur": parseFloat(vitesse),
        "PI 900\nPERTE DE CHARGE DE L'UNITEE": parseFloat(perte),
        "pression de refoulement": parseFloat(pression),
        "température duct de refoulement": parseFloat(temperature)
    };

    // Envoyer les données à l'API Flask via une requête POST
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = `Predicted Performance: ${result.prediction}`;
    })
    .catch(error => console.error('Error:', error));
});
