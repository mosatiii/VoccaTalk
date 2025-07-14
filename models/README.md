# Models

This application requires a speech-to-text (STT) model and a large language model (LLM).

## STT Model (Whisper)

Download a Whisper model from Hugging Face. For example, to download the base model:

```bash
git lfs install
git clone https://huggingface.co/ggerganov/whisper.cpp
```

## LLM Model (Llama 3)

Download a Llama 3 GGUF model from Hugging Face. For example, to download the 8B instruct model:

```bash
git lfs install
git clone https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF
```

After downloading, update the `config.yaml` file with the correct paths to the models.
