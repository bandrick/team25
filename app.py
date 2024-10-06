from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    # Überprüfe, ob beide Dateien vorhanden sind
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Beide Dateien sind erforderlich'}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    # Lese die Inhalte der Dateien
    content1 = file1.read().decode('utf-8')
    content2 = file2.read().decode('utf-8')

    # Beispielberechnung: Kombiniere die Inhalte oder gib eine einfache Nachricht zurück
    result = f'Dateien erfolgreich hochgeladen! Länge der ersten Datei: {len(content1)}, Länge der zweiten Datei: {len(content2)}'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
