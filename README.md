# Adversarial-Robust-Phishing-Detector

An advanced phishing email detection system using DistilBERT, adversarial training, and real-time inference with Gradio.

## Features
- Adversarial training
- Robustness against evasion attacks
- Real-time demo with Gradio

## Setup
```bash
git clone https://github.com/Mookpets/Adversarial-Robust-Phishing-Detector.git
cd Adversarial-Robust-Phishing-Detector
pip install -r requirements.txt
```

## Launch App
```bash
cd app
python app.py
```

## Author
Stephen Koomson (Mookpets)

## Training logs & Evaluation
##  Training Logs and Adversarial Evaluation

All model training, validation, and adversarial robustness experiments were tracked and logged using [Weights & Biases (W&B)](https://wandb.ai/stephenkoomsonbiz-kingston-university).

 **View Full Training Metrics and Robustness Evaluations:**  
[![Weights & Biases Dashboard](https://img.shields.io/badge/W%26B-View_Project-orange?logo=weightsandbiases)](https://wandb.ai/stephenkoomsonbiz-kingston-university)

---

> The W&B dashboard includes:
> - Training/validation loss and accuracy
> - Adversarial attack experiments
> - Model robustness evaluations
> - Fine-tuning and defense logs
