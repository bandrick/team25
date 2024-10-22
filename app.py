from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import io

app = Flask(__name__)

# Vorverarbeitungsfunktion für Zebrafisch-Embryonen-Bilder
def preprocess_image(image):
    # 1. Bild schärfen, um feine Details hervorzuheben
    image = image.filter(ImageFilter.SHARPEN)

    # 2. Kontrast verstärken, um Details besser erkennbar zu machen
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Kontrastfaktor erhöhen (z.B. 2)

    # 3. Optional: Rauschunterdrückung durch einen sanften Filter
    image = image.filter(ImageFilter.SMOOTH)

    # 4. Größe auf 224x224 anpassen (falls notwendig für Machine Learning)
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
