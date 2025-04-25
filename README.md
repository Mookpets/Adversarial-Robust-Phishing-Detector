# Adversarial-Robust-Phishing-Detector

An advanced phishing email detection system using DistilBERT, adversarial training, and real-time inference with Gradio. Built to withstand evasion attacks and outperform traditional ML classifiers.

## Highlights
- Built with HuggingFace Transformers (DistilBERT)
- Adversarial training against phishing evasion attacks
- Real-time Gradio interface
- Evaluation logged using Weights & Biases
- Compared against SVM, CNN, LSTM baselines

## Live Demo
[Run it here on HuggingFace Spaces / Gradio] (Add link)

## Dataset
- Original: `zefang-liu/phishing-email-dataset`
- Augmented with adversarial phishing emails

## Project Structure
See folders: `/notebooks`, `/app`, `/scripts`, `/data`

## Setup
```bash
git clone https://github.com/YOUR-USERNAME/Adversarial-Robust-Phishing-Detector.git
cd Adversarial-Robust-Phishing-Detector
pip install -r requirements.txt
