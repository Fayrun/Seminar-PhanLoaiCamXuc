import torch
from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class SentimentModel:
    def __init__(self, model_name="nlptown/bert-base-multilingual-uncased-sentiment"):
        self.model_name = model_name
        self.device = 0 if torch.cuda.is_available() else -1
        self.classifier = None
        try:
            # We use the HuggingFace pipeline for simplicity (inference-only)
            # Using a multilingual model that supports Vietnamese sentiment analysis
            self.classifier = pipeline(
                "sentiment-analysis",
                model=self.model_name,
                device=self.device,
            )
            logger.info(f"Loaded model {self.model_name} on device {self.device}")
        except Exception as e:
            logger.exception("Failed to load model. Falling back to a safer pipeline if possible.")
            # Provide a helpful error message to the calling code
            self.classifier = None
            self.load_error = str(e)

    def predict(self, text):
        if not self.classifier:
            return {"error": f"Model not loaded: {getattr(self, 'load_error', 'unknown') }"}
        try:
            result = self.classifier(text)
            if isinstance(result, list) and len(result) > 0:
                r = result[0]
                # Normalize label (some models return LABEL_0, POSITIVE, etc.)
                label = r.get('label')
                score = float(r.get('score', 0.0))
                return {"label": label, "score": score, "text": text}
            return {"error": "Empty result from model"}
        except Exception as e:
            return {"error": str(e)}
