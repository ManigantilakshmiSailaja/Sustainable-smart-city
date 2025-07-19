from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
chatbot = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

def summarize_text(text: str) -> str:
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def granite_chat(prompt: str):
    response = chatbot(prompt, max_length=100, do_sample=True)
    return response[0]['generated_text']