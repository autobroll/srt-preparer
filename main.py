from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return {"ok": True}, 200

@app.post("/prepare")
def prepare():
    # 1) Essaye JSON
    data = request.get_json(silent=True) or {}
    srt = None
    if isinstance(data, dict):
        srt = data.get("srt")

    # 2) Fallback: form-data / x-www-form-urlencoded
    if not srt:
        srt = request.form.get("srt")

    # 3) Fallback: raw body (texte brut)
    if not srt:
        try:
            srt = request.data.decode("utf-8", errors="ignore")
        except Exception:
            srt = None

    # Validation finale
    if not srt or not isinstance(srt, str) or not srt.strip():
        return jsonify({"error": "No SRT provided"}), 400

    return jsonify({"srt": srt.strip()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
