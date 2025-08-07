from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return {"ok": True}, 200

@app.post("/prepare")
def prepare():
    data = request.get_json(silent=True) or {}
    srt = data.get("srt", "")
    srt = srt.strip() if isinstance(srt, str) else ""
    if not srt:
        return jsonify({"error": "No SRT provided"}), 400
    return jsonify({"srt": srt}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
