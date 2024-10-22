document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('file');
    const uploadedFile = fileInput.files[0];
    formData.append('file', uploadedFile);

    // Zeige das hochgeladene Bild im Frontend an
    const uploadedImageUrl = URL.createObjectURL(uploadedFile);
    document.getElementById('uploadedImage').src = uploadedImageUrl;

    // Anzeige des Upload-Status
    document.getElementById('output').innerText = "Bild wird verarbeitet...";

    // Sende die Anfrage an das Backend
    fetch('https://team25.onrender.com/upload', {  // Verwende deine tatsächliche Backend-URL
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP-Fehler! Status: ${response.status}`);
        }
        return response.blob();  // Erwarte das verarbeitete Bild als Antwort
    })
    .then(blob => {
        const processedImageUrl = URL.createObjectURL(blob);
        document.getElementById('returnedImage').src = processedImageUrl;
        document.getElementById('output').innerText = "Bild erfolgreich hochgeladen und verarbeitet!";
    })
    .catch(error => {
        console.error('Fehler:', error);
        document.getElementById('output').innerText = `Fehler beim Hochladen oder Verarbeiten des Bildes! Details: ${error.message}`;
    });
});
