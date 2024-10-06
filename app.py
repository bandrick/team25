from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Beide Dateien sind erforderlich'}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    # Verarbeite die Dateien (hier nur als Beispiel)
    content1 = file1.read().decode('utf-8')
    content2 = file2.read().decode('utf-8')

    # Beispiel-Berechnung: Längen der Dateien addieren
    result = len(content1) + len(content2)

    return jsonify({'result': f'Länge der Dateien: {result}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
