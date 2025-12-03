import json
import numpy as np
from tkinter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQs
with open("faqs.json", "r") as f:
    faq_data = json.load(f)

questions = list(faq_data.keys())
answers = list(faq_data.values())

# Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

# Function to get best answer
def get_answer(user_question):
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, question_vectors).flatten()
    index = np.argmax(similarities)

    if similarities[index] < 0.2:
        return "Sorry, I don't understand this question."

    return answers[index]

# GUI
root = Tk()
root.title("FAQ Chatbot")
root.geometry("500x550")
root.config(bg="#f5f5f5")

Label(root, text="🤖 FAQ Chatbot", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

chat_window = Text(root, height=20, width=60, state="disabled")
chat_window.pack(pady=10)

user_entry = Entry(root, width=40, font=("Arial", 12))
user_entry.pack(pady=5)

def send_message():
    user_msg = user_entry.get().strip()
    if user_msg == "":
        return

    chat_window.config(state="normal")
    chat_window.insert(END, "You: " + user_msg + "\n")

    bot_reply = get_answer(user_msg)
    chat_window.insert(END, "Bot: " + bot_reply + "\n\n")
    chat_window.config(state="disabled")

    user_entry.delete(0, END)

Button(root, text="Ask", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()
