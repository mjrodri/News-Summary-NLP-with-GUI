import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
from transformers import BertTokenizer, BertModel
import torch

# Function to Summarize
def summarize():
    url = utext.get("1.0", "end").strip()

    # Summarization
    nltk.download('punkt')  # Must uncomment and download first. Then not needed after first downloaded

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")
    keywords.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)

    author.delete("1.0", "end")
    author.insert("1.0", article.authors)

    publication.delete("1.0", "end")
    publication.insert("1.0", article.publish_date)

    summary.delete("1.0", "end")
    summary.insert("1.0", article.summary)

    # Sentiment - Polarity of Article
    analysis = TextBlob(article.text)
    sentiment.delete("1.0", "end")
    sentiment.insert("1.0",
                     f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Keyword Extraction using BERT embeddings
    keywords_list = extract_keywords_bert(article.text)
    keywords.delete("1.0", "end")
    keywords.insert("1.0", "\n".join(keywords_list))

    title.config(state="disable")
    author.config(state="disable")
    publication.config(state="disable")
    summary.config(state="disable")
    sentiment.config(state="disable")
    keywords.config(state="disable")

# Function to Refresh
def refresh():
    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")
    keywords.config(state="normal")

    title.delete("1.0", "end")
    author.delete("1.0", "end")
    publication.delete("1.0", "end")
    summary.delete("1.0", "end")
    sentiment.delete("1.0", "end")
    keywords.delete("1.0", "end")
    utext.delete("1.0", "end")

    title.config(state="disable")
    author.config(state="disable")
    publication.config(state="disable")
    summary.config(state="disable")
    sentiment.config(state="disable")
    keywords.config(state="disable")

# Function to extract keywords using BERT embeddings
def extract_keywords_bert(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    # Tokenize and get embeddings
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))
    inputs = tokenizer(text, return_tensors="pt", add_special_tokens=True)
    outputs = model(**inputs)

    # Extract embeddings for each token
    embeddings = outputs.last_hidden_state

    # Average the embeddings to get sentence embeddings
    sentence_embeddings = torch.mean(embeddings, dim=1).squeeze().detach().numpy()

    # Identify important tokens by sorting them based on their attention score
    attention_scores = torch.sum(outputs.attentions[-1], dim=1).squeeze().detach().numpy()
    sorted_indices = attention_scores.argsort()[-5:][::-1]

    # Get corresponding words from tokens
    keywords_list = [tokens[i] for i in sorted_indices]

    return keywords_list

# GUI - Graphical User Interface
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

klabel = tk.Label(root, text="Keywords")
klabel.pack()

keywords = tk.Text(root, height=5, width=140)
keywords.config(state="disabled", bg="#dddddd")
keywords.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn_summarize = tk.Button(root, text="Summarize", command=summarize)
btn_summarize.pack(side="left")

btn_refresh = tk.Button(root, text="Refresh", command=refresh)
btn_refresh.pack(side="left")

root.mainloop()