from flask import Flask, render_template, request
from transformers import pipeline
import re
from collections import Counter

app = Flask(__name__)

# Load summarizer
summarizer = pipeline("summarization", model="t5-small")

def is_invalid_text(text):
    text = text.strip()
    
    # 1. Minimum length check
    if len(text) < 50 or len(text.split()) < 10:
        return "Your submission is too short. Please provide at least 50 characters and 10 words."

    # 2. Reject long repeated characters
    if re.search(r"(.)\1{4,}", text.replace(" ", "")):
        return "Your input appears to be nonsensical or overly repetitive."

    # 3. Reject text with very few letters
    total_count = len(text)
    alpha_count = sum(c.isalpha() for c in text)
    if total_count > 0 and (alpha_count / total_count) < 0.4:
        return "Too many non-alphabetic characters detected. Please provide meaningful text."

    # 4. Reject gibberish (words without vowels)
    words_list = text.split()
    meaningful_words = [w for w in words_list if any(c in 'aeiouAEIOU' for c in w) and len(w) > 2]
    if len(meaningful_words) < max(3, len(words_list) * 0.3):
        return "Your input appears to be gibberish. Please provide coherent text."

    # 5. Reject repeated words (excluding common stopwords)
    stopwords = {"the","and","to","of","in","a","for","on","with","is","it","by","its","at","as","an","be","that","this","from"}
    word_counts = Counter([w.lower() for w in words_list if w.lower() not in stopwords])
    if word_counts and max(word_counts.values()) > 5:
        return "Your input has too many repeated words. Please provide meaningful content."


    # 6. Reject if too repetitive overall (low unique word ratio)
    unique_ratio = len(set(words_list)) / len(words_list)
    if unique_ratio < 0.3:
        return "Your input is too repetitive. Please provide diverse meaningful content."

    return None  # valid text

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    error = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]

        # Run validation
        error = is_invalid_text(text)
        if not error:
            try:
                summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            except Exception as e:
                error = f"Summarization failed: {str(e)}"

    return render_template("index.html", summary=summary, error=error, text=text)


if __name__ == "__main__":
    app.run(debug=True)
