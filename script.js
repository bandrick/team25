document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file1', document.getElementById('file1').files[0]);
    formData.append('file2', document.getElementById('file2').files[0]);

    // Anzeige des Upload-Status
    document.getElementById('output').innerText = "Dateien werden hochgeladen...";

    fetch('https://team25.onrender.com'', {  // Verwende deine tatsächliche Backend-URL
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Zeige das Ergebnis oder eine Erfolgsmeldung an
        document.getElementById('output').innerText = `Ergebnis der Berechnung: ${data.result}`;
    })
    .catch(error => {
        console.error('Fehler:', error);
        document.getElementById('output').innerText = 'Fehler beim Hochladen oder Verarbeiten der Dateien!';
    });
});
