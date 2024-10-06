from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Aktiviere CORS für alle Routen

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'file1' not in request.files or 'file2' not in request.files:
            return jsonify({'error': 'Beide Dateien sind erforderlich'}), 400

        file1 = request.files['file1']
        file2 = request.files['file2']

        content1 = file1.read().decode('utf-8')
        content2 = file2.read().decode('utf-8')

        result = f'Dateien erfolgreich hochgeladen! Länge der ersten Datei: {len(content1)}, Länge der zweiten Datei: {len(content2)}'

        return jsonify({'result': result})
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({'error': 'Fehler bei der Verarbeitung der Dateien!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
