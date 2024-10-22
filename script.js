document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', document.getElementById('file').files[0]);

    document.getElementById('output').innerText = "Datei wird hochgeladen...";

    fetch('https://team25.onrender.com/upload', {  // Backend-URL verwenden
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP-Fehler! Status: ${response.status}`);
        }
        return response.blob();  // Bild als Blob zurückbekommen
    })
    .then(blob => {
        const imageUrl = URL.createObjectURL(blob);
        document.getElementById('returnedImage').src = imageUrl;
        document.getElementById('output').innerText = "Bild erfolgreich hochgeladen und verarbeitet!";
    })
    .catch(error => {
        console.error('Fehler:', error);
        document.getElementById('output').innerText = `Fehler beim Hochladen oder Verarbeiten der Datei! Details: ${error.message}`;
    });
});
