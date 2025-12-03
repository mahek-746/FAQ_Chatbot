# FAQ_Chatbot
A simple FAQ Chatbot built with Python, Tkinter, and Cosine Similarity.
This desktop app answers frequently asked questions (FAQs) using basic NLP — beginner-friendly and offline!

📌 Features

Interactive GUI using Tkinter

Answers questions based on predefined FAQ dataset

Uses TF-IDF Vectorizer + Cosine Similarity for matching

Offline and lightweight

Beginner-friendly code — perfect for learning Python NLP

💻 Demo

(optional: add your screenshot here)

🛠️ Installation

Clone the repository

git clone https://github.com/<your-username>/CodeAlpha_FAQ_Chatbot.git
cd CodeAlpha_FAQ_Chatbot


Install required libraries

pip install scikit-learn numpy


⚠️ Make sure Tkinter is installed.
It comes pre-installed with Python on most systems.

📂 Files
File	Description
faq_chatbot.py	Main Python script for the chatbot GUI
faqs.json	FAQ dataset used by the chatbot
README.md	Project documentation
🚀 How to Run

Run the chatbot:

python faq_chatbot.py


A window will open where you can:

Type a question

Click Ask

Get the most relevant answer from FAQs

📝 Sample FAQs
{
    "What is AI?": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that helps systems learn from data.",
    "What is Python?": "Python is a popular high-level programming language widely used in AI and ML.",
    "How does a chatbot work?": "A chatbot uses NLP to understand text and respond with the best matching answer.",
    "What is CodeAlpha?": "CodeAlpha is a platform that provides internships and training programs for students."
}


You can edit faqs.json to add your own questions and answers.

⚙️ How it Works

User enters a question

TF-IDF converts the FAQ questions into vectors

Cosine Similarity finds the most similar question

Bot returns the corresponding answer

If similarity < 0.2 → bot responds: "Sorry, I don't understand this question."

🛠️ Tools & Libraries

Python 3.x

Tkinter (GUI)

scikit-learn (TF-IDF + Cosine Similarity)

NumPy

🌟 Future Improvements

Modern, responsive UI

Add voice input/output

Include more FAQs dynamically

Integrate with web-based chatbot
