document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file1', document.getElementById('file1').files[0]);
    formData.append('file2', document.getElementById('file2').files[0]);

    fetch('https://team25.onrender.com', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = `Ergebnis der Berechnung: ${data.result}`;
    })
    .catch(error => {
        console.error('Fehler:', error);
    });
});
