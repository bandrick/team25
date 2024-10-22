from flask import Flask, request, jsonify, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'file1' not in request.files or 'file2' not in request.files:
            return jsonify({'error': 'Beide JPEG-Dateien sind erforderlich'}), 400

        file1 = request.files['file1']
        file2 = request.files['file2']

        # Öffne die JPEG-Dateien mit PIL (Pillow)
        img1 = Image.open(file1)
        img2 = Image.open(file2)

        # Beispiel: Wir kombinieren die beiden Bilder zu einem neuen
        new_image = Image.blend(img1, img2, alpha=0.5)

        # Speichere das neue Bild in einem Bytestream
        img_io = io.BytesIO()
        new_image.save(img_io, 'JPEG')
        img_io.seek(0)

        # Rückgabe der neuen JPEG-Datei
        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({'error': 'Fehler bei der Verarbeitung der Dateien!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
