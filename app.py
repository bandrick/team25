from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io

app = Flask(__name__)

# Aggressive Vorverarbeitung für Zebrafisch-Embryonen-Bilder
def preprocess_image(image):
    # Bild schärfen und Kanten erkennen
    image = image.filter(ImageFilter.SHARPEN)
    image = image.filter(ImageFilter.FIND_EDGES)
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(3)
    image = ImageOps.equalize(image)
    saturation_enhancer = ImageEnhance.Color(image)
    image = saturation_enhancer.enhance(2)
    image = image.filter(ImageFilter.SMOOTH)
    image = image.resize((224, 224))
    return image

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Eine Datei ist erforderlich'}), 400

        file = request.files['file']

        # Überprüfen, ob die hochgeladene Datei ein Bild ist
        try:
            img = Image.open(file)
        except IOError:
            return jsonify({'error': 'Die hochgeladene Datei ist kein gültiges Bild'}), 400

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
