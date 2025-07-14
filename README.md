# VoccaTalk

This is a local, privacy-first voice assistant that runs entirely on your machine. It uses [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) for speech-to-text, a local Large Language Model (LLM) for generating responses, and a text-to-speech (TTS) engine for voice output.

## Features

*   **Voice-in, Voice-out:** Speak to the assistant and get a spoken response.
*   **Local & Private:** All processing is done on your machine. No data is sent to the cloud.
*   **Customizable:** You can swap out the LLM and STT models with any other compatible models.

## How it Works

The application consists of a simple frontend and a Python backend:

*   **Frontend:** A simple web interface (`ui/`) captures audio from your microphone and sends it to the backend.
*   **Backend:** A FastAPI server (`backend/`) that:
    1.  Receives the audio.
    2.  Uses a speech-to-text (STT) model to transcribe the audio to text.
    3.  Sends the transcribed text to a large language model (LLM).
    4.  Receives the response from the LLM.
    5.  (Optional) Uses a text-to-speech (TTS) engine to convert the response to audio and plays it.

## Setup & Run

Simply run the `run.sh` script:

```bash
./run.sh
```

The first time you run it, the script will automatically:

1.  Install the required Python dependencies.
2.  Download the necessary STT and LLM models.
3.  Create a default `config.yaml` file.

After the initial setup, the script will start the backend server. You can then open the `ui/index.html` file in your web browser to use the application.

## Configuration

The `backend/config.yaml` file contains the following settings:

*   `stt.model_path`: Path to the STT model file.
*   `llm.model_path`: Path to the LLM model file.
*   `llm.n_gpu_layers`: Number of LLM layers to offload to the GPU. Set to `-1` to offload all layers.
*   `tts.enabled`: Enable or disable the text-to-speech output.
*   `server.port`: The port for the backend server.

## API Endpoints

The backend server provides the following API endpoints:

*   `POST /api/transcribe`: Transcribes an audio file.
*   `POST /api/ask`: Sends a text prompt to the LLM.
*   `POST /api/speak`: Converts text to speech.
*   `POST /api/voice-in-voice-out`: The main endpoint for voice-based interaction. It takes an audio file, transcribes it, gets a response from the LLM, and optionally speaks the response.
