from transformers import pipeline


def medical_summarize(text):
    summarizer = pipeline("summarization", model="Falconsai/medical_summarization")
    result = summarizer(text, max_length=230, min_length=30, do_sample=False)
    return result[0]['summary_text']
