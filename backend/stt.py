from whisper_cpp_python import Whisper

class STT:
    def __init__(self, model_path):
        self.model = Whisper(model_path)

    def transcribe(self, audio_file):
        return self.model.transcribe(audio_file)
