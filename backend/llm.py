from llama_cpp import Llama

class LLM:
    def __init__(self, model_path, n_gpu_layers=0):
        self.model = Llama(model_path=model_path, n_gpu_layers=n_gpu_layers)

    def generate(self, prompt):
        return self.model(prompt, max_tokens=150)
