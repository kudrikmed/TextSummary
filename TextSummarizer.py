from summarizer import Summarizer  # https://pypi.org/project/bert-extractive-summarizer/


class TextSummarizer:
    def __init__(self):
        self.model = Summarizer()

    def summarize(self, text, ratio=0.2):
        result = self.model(text, ratio=ratio)
        return result
