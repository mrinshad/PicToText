# PicToText

PicToText is a simple web application that allows users to upload an image and extract text from it using OCR (Optical Character Recognition).

## Features

- Upload an image file
- Extract text from the uploaded image
- Display extracted text in a user-friendly interface
- Copy extracted text to clipboard

## Requirements

- Python 3.x
- Flask
- pytesseract
- Pillow
- Werkzeug

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/PicToText.git
    cd PicToText
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000` to use the application.

## Usage

- Click on the "Choose an Image File" button to upload an image.
- Click on the "Upload Image" button to extract text from the image.
- The extracted text will be displayed in a text area.
- Click the copy icon to copy the extracted text to the clipboard.


