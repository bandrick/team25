document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file1', document.getElementById('file1').files[0]);
    formData.append('file2', document.getElementById('file2').files[0]);

    document.getElementById('output').innerText = "Dateien werden hochgeladen...";

    fetch('https://team25.onrender.com/upload', {  // Korrekte URL mit /upload
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP-Fehler! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('output').innerText = `Ergebnis der Berechnung: ${data.result}`;
    })
    .catch(error => {
        console.error('Fehler:', error);
        document.getElementById('output').innerText = `Fehler beim Hochladen oder Verarbeiten der Dateien! Details: ${error.message}`;
    });
});

