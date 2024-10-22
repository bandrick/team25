from flask import Flask, request, jsonify, send_file
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# Vorverarbeitungsschritte für Machine Learning
def preprocess_image(image):
    # 1. Größe ändern auf 224x224
    image = image.resize((224, 224))
    
    # 2. Konvertiere das Bild in ein NumPy-Array
    image_array = np.array(image)

    # 3. Normalisierung der Pixelwerte auf den Bereich [0, 1]
    image_array = image_array.astype('float32') / 255.0

    return image_array

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Eine JPEG-Datei ist erforderlich'}), 400

        file = request.files['file']

        # Öffne die JPEG-Datei mit PIL (Pillow)
        img = Image.open(file)

        # Konvertiere das Bild in RGB (falls es nicht bereits RGB ist)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Wende die Vorverarbeitung an
        processed_image = preprocess_image(img)

        # Beispiel: Gib das verarbeitete Array zurück (als Debug, nicht für Produktion)
        # In der Praxis würdest du dieses Array an deinen ML-Algorithmus übergeben
        print("Verarbeitetes Bild:", processed_image.shape)

        # Zum Test: Speichere das Bild nach der Größenanpassung und sende es zurück
        img_io = io.BytesIO()
        img = Image.fromarray((processed_image * 255).astype(np.uint8))  # Bild zurückkonvertieren
        img.save(img_io, 'JPEG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({'error': 'Fehler bei der Verarbeitung der Datei!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
