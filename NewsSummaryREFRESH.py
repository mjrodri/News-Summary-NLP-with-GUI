# Summarizing News Articles
# Using Natural language Processing
# Machine Learning
# Building a Graphical User Interface
# Simplified Natural Language Processing done for you using these tools

import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

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

    title.config(state="disable")
    author.config(state="disable")
    publication.config(state="disable")
    summary.config(state="disable")
    sentiment.config(state="disable")

# Function to Refresh
def refresh():
    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0", "end")
    author.delete("1.0", "end")
    publication.delete("1.0", "end")
    summary.delete("1.0", "end")
    sentiment.delete("1.0", "end")
    utext.delete("1.0", "end")

    title.config(state="disable")
    author.config(state="disable")
    publication.config(state="disable")
    summary.config(state="disable")
    sentiment.config(state="disable")

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

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn_summarize = tk.Button(root, text="Summarize", command=summarize)
btn_summarize.pack(side="left")

btn_refresh = tk.Button(root, text="Refresh", command=refresh)
btn_refresh.pack(side="left")

root.mainloop()