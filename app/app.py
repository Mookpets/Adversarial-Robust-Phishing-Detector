import gradio as gr

def phishing_detector(email_text):
    # Dummy prediction logic for now
    if "bank" in email_text.lower() or "account" in email_text.lower():
        return "Phishing"
    else:
        return "Legitimate"

iface = gr.Interface(fn=phishing_detector,
                     inputs="text",
                     outputs="text",
                     title="Phishing Email Detector",
                     description="Enter an email text to check if it's phishing or legitimate.")

if __name__ == "__main__":
    iface.launch()
