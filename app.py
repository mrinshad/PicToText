from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            image = Image.open(io.BytesIO(file.read()))
            extracted_text = pytesseract.image_to_string(image)
    return render_template('index.html', extracted_text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
