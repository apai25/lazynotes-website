from summarizer import Summarizer

def summarize(text):

    model = Summarizer()
    summarized_text = model(text, ratio=0.2)

    return summarized_text