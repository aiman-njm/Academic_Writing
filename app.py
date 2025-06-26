from flask import Flask, request, jsonify
from analyze import analyze_text

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_route():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400
    result = analyze_text(data['text'])
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
