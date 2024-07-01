from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
model_path = "./model"
model = AutoModelForTokenClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
nlp = pipeline("token-classification", model=model, tokenizer=tokenizer)

@app.route('/')
def home(): return render_template('index.html')

@app.route('/pos_tag', methods=['POST'])
def pos_tag():
    text = request.json.get('text')
    if not text: return jsonify({"error": "Masukkan Teks"}), 400
    if isinstance(text, str): text = text.encode('utf-8').decode('utf-8')
    results = nlp(text)
    tagged_tokens = [{"word": res["word"].replace('Ġ', ''), "tag": res["entity"].replace('B-', '').replace('I-', '')} for res in results]
    return jsonify({"tagged_tokens": tagged_tokens})
if __name__ == '__main__':
    app.run(port=5007, debug=True)