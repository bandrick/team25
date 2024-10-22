from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np
import io

app = Flask(__name__)

# Aggressivere Vorverarbeitung für Zebrafisch-Embryonen-Bilder
def preprocess_image(image):
    # 1. Schärfen des Bildes (verstärkt die Kanten)
    image = image.filter(ImageFilter.SHARPEN)

    # 2. Erhöhte Kantendetektion mit dem FIND_EDGES Filter (sehr aggressiv)
    image = image.filter(ImageFilter.FIND_EDGES)

    # 3. Kontrast stark erhöhen
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(3)  # Kontrastfaktor 3

    # 4. Histogramm-Ausgleich für gleichmäßigere Helligkeit
    image = ImageOps.equalize(image)

    # 5. Sättigung anpassen (stärker betonte Farben)
    saturation_enhancer = ImageEnhance.Color(image)
    image = saturation_enhancer.enhance(2)  # Sättigung erhöhen

    # 6. Rauschunterdrückung durch leichten Glättungsfilter (optional)
    image = image.filter(ImageFilter.SMOOTH)

    # 7. Größe auf 224x224 anpassen
    image = image.resize((224, 224))

    return image

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

        # Wende die Bildvorverarbeitung an
        processed_image = preprocess_image(img)

        # Speichere das neue Bild in einem Bytestream
        img_io = io.BytesIO()
        processed_image.save(img_io, 'JPEG')
        img_io.seek(0)

        # Rückgabe des bearbeiteten Bildes
        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({'error': 'Fehler bei der Verarbeitung der Datei!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
