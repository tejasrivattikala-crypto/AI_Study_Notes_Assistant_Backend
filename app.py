from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pathlib import Path

# Flask app create
app = Flask(__name__)
CORS(app)

# React build folder path
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend" / "frontend" / "build"

# Serve React build
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

# API route
@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"success": False, "error": "Please enter some study notes."}), 400
    result = {
        "summary": "short summary text",
        "keywords": ["keyword1", "keyword2"],
        "topics": ["topic1", "topic2"]
    }
    return jsonify({"success": True, "data": result})

if __name__ == "__main__":
    print("Server running at http://127.0.0.1:5000")
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Backend!"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    return jsonify({"message": "Hello from Flask!"})
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Backend!"

@app.route("/api/data")
def get_data():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == "__main__":
    app.run(debug=True)
