# News-Summary-NLP-with-GUI - UPDATE

# Update - BERT-based Keyword Extraction:

Integrated BERT embeddings for keyword extraction.
Utilized the transformers library to load a pre-trained BERT model and tokenizer.
Created a function (extract_keywords_bert) to extract keywords based on attention scores from BERT embeddings.
Displayed the extracted keywords in the GUI under the "Keywords" section.
Enhanced GUI:

Added a new section for displaying extracted keywords.
Adjusted the layout to accommodate the new "Keywords" section.
Functionality:

When the "Summarize" button is pressed, the code now not only provides a summary and sentiment analysis but also extracts and displays keywords from the news article.

This addition enhances the news summarizer by incorporating keyword extraction using advanced neural network-based embeddings from BERT, providing more detailed insights into the main topics of the news articles.

# Refresh Functionality:

Old Version: The initial version lacked a mechanism to refresh the interface after summarization.
Updated Version: A "Refresh" button (btn_refresh) has been added, allowing users to clear the interface and enter new URLs without restarting the application.
Enhanced Code Structure:

Old Version: The code was structured as a single function without a modular approach.
Updated Version: The code has been organized into two main functions (summarize and refresh), improving readability and maintainability.
Improved User Interaction:

Old Version: The initial version relied solely on the "Summarize" button, which presented limitations for users who wanted to input multiple articles successively.
Updated Version: The introduction of the "Refresh" button enhances user experience by providing a convenient way to clear the interface for new inputs.
Code Comments:

Old Version: Lacked comments for code explanation and understanding.
Updated Version: Added comments to explain key sections of the code, making it more accessible for developers and contributors.
Additional Documentation:

Old Version: The initial description lacked specific details about the code structure and features.
Updated Version: The extended README now provides a comprehensive overview, key tools, skills, features, and how to use the application.
Button Styling:

Old Version: Basic buttons with default styling.
Updated Version: Buttons have been given more descriptive names (btn_summarize and btn_refresh) and are positioned using the side attribute.

These improvements aim to make the code more user-friendly, modular, and maintainable, promoting better interaction with the news summarization application.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
News Summarizer
This Python script provides a user-friendly Graphical User Interface (GUI) for summarizing news articles using natural language processing tools. Leveraging tkinter, the GUI allows users to input a news article URL, click the "Summarize" button, and receive a concise overview, including the article's title, author, publication date, summary, and sentiment analysis. The code integrates the newspaper library for article extraction and TextBlob for sentiment analysis. To use the tool, simply run the script, input the desired URL, and explore summarized information effortlessly.

Features:

Simplified Summarization: Utilizes natural language processing to provide a streamlined summary of news articles.
User-Friendly Interface: A GUI built with tkinter enables easy interaction and input from users.
Sentiment Analysis: Includes sentiment analysis, displaying the article's polarity as positive, negative, or neutral.

Download and Run: Requires minimal setup; download the script and run it to start summarizing news articles instantly.

How to Use:

Download: Clone or download the repository to your local machine.
Install Dependencies: Ensure you have Python installed. Run pip install nltk textblob newspaper3k to install the necessary libraries.
Run the Script: Execute the script by running python news_summarizer.py in your terminal or command prompt.
Input URL: Enter the URL of the news article into the provided text field.
Summarize: Click the "Summarize" button to generate a summary and view the information in the GUI.
Feel free to explore and enhance the script to suit your needs! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.
