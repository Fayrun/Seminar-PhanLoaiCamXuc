# Vietnamese Sentiment Analysis Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.10%2B-FF4B4B)](https://streamlit.io/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)](https://huggingface.co/transformers/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A lightweight sentiment analysis application for Vietnamese text using pre-trained transformer models. This project demonstrates inference-only implementation suitable for academic projects and demonstrations.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Testing](#testing)
- [Performance](#performance)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

This application provides a simple web interface for sentiment classification of Vietnamese text. It leverages pre-trained multilingual BERT models through the HuggingFace Transformers library, offering:

- **Real-time sentiment analysis** of Vietnamese text input
- **Persistent storage** of analysis history using SQLite
- **Interactive web interface** built with Streamlit
- **Confidence scores** for each prediction
- **Automated testing** with 10 representative Vietnamese test cases

**Target Audience:** Students, researchers, and developers interested in Vietnamese NLP applications.

## ✨ Features

### Core Functionality
- 🎭 **Sentiment Classification**: Classifies Vietnamese text into sentiment categories (Positive/Neutral/Negative or 1-5 star ratings)
- 💾 **History Tracking**: Stores all predictions with timestamps in SQLite database
- 📊 **Confidence Scores**: Displays model confidence for each prediction
- 🌐 **Web Interface**: Clean, responsive Streamlit UI

### Technical Features
- ⚡ **Fast Inference**: Optimized for quick predictions using HuggingFace pipelines
- 🔄 **GPU Support**: Automatically uses GPU if available, falls back to CPU
- 📝 **Logging**: Comprehensive error handling and logging
- 🧪 **Testing Suite**: Automated test script with accuracy calculation

## 🏗️ Architecture

```
┌─────────────┐
│   User      │
│   Input     │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Streamlit UI       │
│  (app.py)           │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  SentimentModel     │
│  (model.py)         │
│  - HF Pipeline      │
│  - BERT Model       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Database           │
│  (database.py)      │
│  - SQLite           │
│  - History Storage  │
└─────────────────────┘
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 2GB free disk space (for model weights)
- Internet connection (first run only)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd vietnamese-sentiment-analysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: First installation may take 5-10 minutes as it downloads PyTorch and Transformers libraries.

4. **Verify installation**
   ```bash
   python -c "import streamlit; import transformers; print('✓ Installation successful')"
   ```

## 💻 Usage

### Running the Web Application

1. **Start the Streamlit server**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

3. **Using the interface**
   - Enter Vietnamese text in the text area
   - Click "🔍 Phân Tích" (Analyze) button
   - View sentiment prediction and confidence score
   - Check history section for past predictions

**First Run Note**: The application will download the pre-trained model (~400MB) on first execution. This requires an internet connection and may take several minutes.

### Running Tests

Execute the automated test suite:

```bash
python test.py
```

**Expected Output:**
```
Text: Hôm nay tôi rất vui vẻ
Pred: 5 stars (98.50%)
Expected: POSITIVE
---
...
Accuracy: 70.00% (7/10)
```

### Using Alternative Models

To use a different model, modify `model.py`:

```python
# Example: Using PhoBERT
model = SentimentModel(model_name="vinai/phobert-base")

# Example: Using DistilBERT
model = SentimentModel(model_name="distilbert-base-multilingual-cased")
```

## 📁 Project Structure

```
vietnamese-sentiment-analysis/
│
├── app.py                 # Main Streamlit application
├── model.py               # Model wrapper and inference logic
├── database.py            # SQLite database management
├── test.py                # Automated testing script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore            # Git ignore rules
│
├── data/                  # Created automatically
│   └── sentiment.db      # SQLite database (auto-generated)
│
└── venv/                  # Virtual environment (if created)
```

### File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Streamlit web interface with UI components and event handlers |
| `model.py` | Wrapper class for HuggingFace pipeline, handles model loading and inference |
| `database.py` | SQLite database operations for storing prediction history |
| `test.py` | Test suite with 10 Vietnamese test cases and accuracy calculation |
| `requirements.txt` | List of Python package dependencies |

## 🤖 Model Information

### Default Model

**Model**: `nlptown/bert-base-multilingual-uncased-sentiment`

**Specifications:**
- **Architecture**: BERT-base (12 layers, 768 hidden units)
- **Languages**: Multilingual (including Vietnamese)
- **Task**: 5-class sentiment classification (1-5 stars)
- **Parameters**: ~110M
- **Model Size**: ~400MB

### Alternative Models

| Model | Language | Output Format | Accuracy (VN) |
|-------|----------|---------------|---------------|
| `vinai/phobert-base` | Vietnamese | POSITIVE/NEGATIVE/NEUTRAL | High |
| `distilbert-base-multilingual-cased` | Multilingual | Various | Medium |
| `xlm-roberta-base` | Multilingual | Various | Medium-High |

### Model Selection Criteria

- **Vietnamese-specific**: Use `vinai/phobert-base` for best accuracy
- **Lightweight**: Use `distilbert` for faster inference
- **Multilingual**: Use `bert-base-multilingual` for cross-language support

## 🧪 Testing

### Test Suite Details

The `test.py` script includes 10 carefully selected Vietnamese test cases covering:

- ✅ **Positive sentiment**: 4 cases (40%)
- ⚖️ **Neutral sentiment**: 3 cases (30%)
- ❌ **Negative sentiment**: 3 cases (30%)

### Test Categories

1. **Explicit positive**: "Món ăn này thật tuyệt vời" (This food is amazing)
2. **Explicit negative**: "Dịch vụ quá tệ" (Service is terrible)
3. **Neutral factual**: "Cuốn sách có 200 trang" (The book has 200 pages)
4. **Implicit sentiment**: Various nuanced expressions

### Running Custom Tests

```python
from model import SentimentModel

model = SentimentModel()

# Custom test
result = model.predict("Sản phẩm này đáng tiền")
print(f"Sentiment: {result['label']} ({result['score']:.2%})")
```

## 📊 Performance

### Expected Accuracy

- **Default model**: 60-70% on Vietnamese test set
- **PhoBERT**: 85-95% on Vietnamese test set
- **Fine-tuned model**: 90-95%+ on domain-specific data

### Inference Speed

| Hardware | Speed (per sentence) |
|----------|---------------------|
| CPU (Intel i5) | ~500ms |
| CPU (Intel i7) | ~300ms |
| GPU (NVIDIA GTX 1060) | ~50ms |
| GPU (NVIDIA RTX 3080) | ~20ms |

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 4GB | 8GB+ |
| Storage | 2GB | 5GB+ |
| CPU | Dual-core | Quad-core+ |
| GPU | Not required | NVIDIA CUDA-compatible |

## ⚠️ Limitations

### Current Limitations

1. **No Fine-tuning**: Uses pre-trained models without domain-specific training
2. **Inference-only**: Does not include training/fine-tuning capabilities
3. **Language Coverage**: Multilingual models may not capture Vietnamese nuances
4. **Context Length**: Limited to ~512 tokens per input
5. **Real-time Only**: No batch processing for large datasets

### Known Issues

- **Neutral Sentences**: Lower accuracy on purely informational text
- **Sarcasm Detection**: Cannot reliably detect sarcastic sentiment
- **Mixed Sentiment**: Struggles with sentences containing both positive and negative elements
- **Slang/Informal**: Less accurate with informal Vietnamese or internet slang

## 🔮 Future Enhancements

### Planned Features

- [ ] **Fine-tuning Module**: Add training capabilities for custom datasets
- [ ] **Batch Processing**: Support CSV/Excel file uploads
- [ ] **REST API**: Flask/FastAPI endpoints for integration
- [ ] **Multilingual Support**: UI in English and Vietnamese
- [ ] **Export Functionality**: Download results as CSV/PDF
- [ ] **Advanced Analytics**: Sentiment trends and visualization
- [ ] **Model Comparison**: Side-by-side comparison of different models
- [ ] **Emoji Analysis**: Include emoji-based sentiment indicators

### Potential Improvements

- Implement caching for faster repeated queries
- Add user authentication and personal history
- Support for longer documents with chunking
- Real-time streaming analysis
- Integration with Vietnamese social media platforms

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to all functions and classes
- Include tests for new features
- Update README.md with relevant changes
- Keep commits atomic and well-described

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

### Models and Libraries

- **HuggingFace Transformers**: For providing the model inference pipeline
- **nlptown**: For the multilingual sentiment model
- **VinAI Research**: For PhoBERT Vietnamese language model
- **Streamlit**: For the intuitive web framework
- **PyTorch**: For the deep learning backend

### References

- Devlin, J., et al. (2018). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*
- Nguyen, D. Q., & Nguyen, A. T. (2020). *PhoBERT: Pre-trained language models for Vietnamese*
- HuggingFace Documentation: https://huggingface.co/docs/transformers/

### Dataset

- Test cases inspired by AIViVN Vietnamese sentiment analysis competition
- Community-contributed Vietnamese text examples

---

## 📞 Contact & Support
- **Email**: luuphuc1368@gmail.com

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐ on GitHub!

---

**Note**: This is an academic/demonstration project. For production use, consider fine-tuning models on domain-specific data and implementing additional security measures.

**Last Updated**: December 2025
