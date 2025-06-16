from flask import Flask, request, send_file
import requests

app = Flask(__name__)
API_KEY = "TU_API_KEY_DE_ELEVENLABS"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Puedes cambiarla por otra voz

@app.route("/tts", methods=["POST"])
def tts():
    texto = request.json["text"]
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    datos = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    respuesta = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        headers=headers,
        json=datos
    )

    with open("voz.wav", "wb") as f:
        f.write(respuesta.content)

    return send_file("voz.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
