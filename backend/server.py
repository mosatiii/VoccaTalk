from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import yaml
from stt import STT
from llm import LLM
from tts import TTS
import io

app = FastAPI()

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

stt = STT(config["stt"]["model_path"])
llm = LLM(config["llm"]["model_path"], config["llm"]["n_gpu_layers"])
tts_enabled = config["tts"]["enabled"]
if tts_enabled:
    tts = TTS()

@app.post("/api/transcribe")
def transcribe_audio(audio_file: UploadFile = File(...)):
    content = audio_file.file.read()
    transcription = stt.transcribe(content)
    return {"transcription": transcription["text"]}

@app.post("/api/ask")
def ask_llm(prompt: str):
    response = llm.generate(prompt)
    return {"response": response["choices"][0]["text"]}

@app.post("/api/speak")
def speak_text(text: str):
    if not tts_enabled:
        return {"error": "TTS is disabled in the configuration."}
    
    tts.speak(text)
    return {"status": "success"}

@app.post("/api/voice-in-voice-out")
async def voice_in_voice_out(audio_file: UploadFile = File(...)):
    audio_bytes = await audio_file.read()
    
    # Speech to Text
    transcription = stt.transcribe(audio_bytes)
    prompt = transcription['text']

    # LLM
    llm_response = llm.generate(prompt)
    response_text = llm_response['choices'][0]['text']

    # Text to Speech
    if tts_enabled:
        tts.speak(response_text)
        return {"transcription": prompt, "response": response_text}
    else:
        return {"transcription": prompt, "response": response_text, "audio": None}

app.mount("/", StaticFiles(directory="../ui", html=True), name="ui")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config["server"]["port"])
