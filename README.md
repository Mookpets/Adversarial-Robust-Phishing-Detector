# Adversarial-Robust Phishing Email Detector

A full-stack cybersecurity project designed to detect phishing emails using an adversarially robust DistilBERT model. This invention combines classical ML, deep learning, adversarial defense, and real-time deployment through a Gradio web interface.

---

## 📌 Project Stages

This repository showcases the complete lifecycle of the invention — from classical models to adversarial robustness and deployment.

---

### 🔹 1. Foundation: Classical Machine Learning

Before entering the deep learning space, the project began with classical ML approaches to phishing email detection.

**Folder:** `foundation_ml_models/`  
- `phishing_baseline_svm.ipynb`  
- `model_comparison_classical_deep_phishing.ipynb`

✅ Models used: SVM, Logistic Regression, Naive Bayes, Decision Trees, KNN  
✅ Baseline performance comparison

---

### 🔹 2. Transition to Deep Learning

Moving from traditional ML to Hugging Face's DistilBERT for more context-aware phishing detection.

**Folder:** `deep_learning_models/`  
- `bert_phishing_zefangliu_preprocessed.ipynb`  
- `bert_phishing_detection_huggingface.ipynb`

✅ Tokenization & fine-tuning of `distilbert-base-uncased`  
✅ Significant improvement over traditional ML

---

### 🔹 3. Adversarial Robustness: The Invention

This stage represents the core invention — a model trained to resist adversarial phishing attacks.

**Folder:** `adversarial_training/`  
- `adversarial_distilbert_weighted_training.ipynb`  
- `adversarial_retraining_with_augmented_data.ipynb`  
- `robust_distilbert_phishing_detector_FINAL_optimized.ipynb`

✅ Weighted loss to address class imbalance  
✅ Adversarial retraining using crafted phishing variants  
✅ Final model demonstrates robustness under evasion attempts

---

### 🔹 4. Deployment: Gradio Web App

The invention is deployed as a real-time Gradio app with live input-output capabilities.

**Folder:** `deployment/`  
- `app.py`  
- `movesmodeltohugging.ipynb`

✅ Real-time email classification  
✅ Model hosted via Hugging Face

🔗 **Live Demo:**  
👉 [Try the phishing detector app](https://huggingface.co/spaces/apostleflex/jah-ak-phishing-detector)

---

## 📊 Training Logs and Evaluation

All experiments, model training, and adversarial evaluation were tracked on Weights & Biases.

🔗 [View W&B training run](https://wandb.ai/akataship-models/adversarial-phishing-defense-weighted/runs/7mvmr5u1/overview)

---

## 🗂️ Repo Structure
├── foundation_ml_models/ │ ├── phishing_baseline_svm.ipynb │ └── model_comparison_classical_deep_phishing.ipynb │ ├── deep_learning_models/ │ ├── bert_phishing_zefangliu_preprocessed.ipynb │ └── bert_phishing_detection_huggingface.ipynb │ ├── adversarial_training/ │ ├── adversarial_distilbert_weighted_training.ipynb │ ├── adversarial_retraining_with_augmented_data.ipynb │ └── robust_distilbert_phishing_detector_FINAL_optimized.ipynb │ ├── deployment/ │ ├── app.py │ └── movesmodeltohugging.ipynb │ ├── data/ │ ├── sample_adversarial_emails.csv │ └── phishing_legitimate_sample.csv │ ├── requirements.txt └── README.md

---

## 💡 Tech Stack

- Python, Pandas, Scikit-Learn  
- Hugging Face Transformers (DistilBERT)  
- Gradio for web deployment  
- Weights & Biases for experiment tracking  
- Hugging Face Spaces for public demo hosting

---

## 🔒 Access & Collaboration

This project is currently under **private review**.  
📩 Contact the author directly for collaboration, industry use, or access to full internal assets.

---

## 👤 Author

**Stephen Koomson**  
GitHub: [Mookpets](https://github.com/Mookpets)  
W&B: [akataship](https://wandb.ai/akataship)  
Hugging Face: [apostleflex](https://huggingface.co/apostleflex)
