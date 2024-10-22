from flask import Flask, request, jsonify, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Eine JPEG-Datei ist erforderlich'}), 400

        file = request.files['file']

        # Öffne die JPEG-Datei mit PIL (Pillow)
        img = Image.open(file)

        # Beispiel: Konvertiere das Bild in RGB (falls es nicht bereits RGB ist) und skaliere es auf 300x300
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((300, 300))

        # Speichere das neue Bild in einem Bytestream
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)

        # Rückgabe der bearbeiteten JPEG-Datei
        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({'error': 'Fehler bei der Verarbeitung der Datei!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
