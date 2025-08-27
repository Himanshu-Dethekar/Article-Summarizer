#### Article Summarizer



## Description

Article Summarizer is a Python Flask web application that summarizes long articles into concise summaries using HuggingFace Transformers (t5-small model). The app features a user-friendly interface with validation to handle invalid or nonsensical input.

##### 

##### Features

Summarizes articles entered by the user.

Detects invalid or gibberish input.

Responsive and clean interface (chat-like layout).

Ready for deployment on platforms like PythonAnywhere or Hugging Face Spaces.



##### Technologies Used

Backend: Python, Flask

Machine Learning: HuggingFace Transformers (t5-small)

Frontend: HTML, CSS (modern design, optional JS enhancements)

Dependencies:

flask

transformers

torch

sentencepiece

regex



##### Installation \& Setup (Local)

Clone the repository

git clone https://github.com/Himanshu-Dethekar/Article-Summarizer.git
cd Article-Summarizer



##### Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows



##### Install dependencies

pip install -r requirements.txt



##### Run the app

python app.py

##### 

Open in browser
Navigate to http://127.0.0.1:5000 to access the application.



##### Usage

Enter your article text in the input box.

Click Summarize.

The app generates a concise summary.

If input is invalid, an error message will appear with a red-left-border style.



##### Future Improvements

Improve summary accuracy using larger models.

Add authentication and user history.

Enhance UI with animations and theme toggle.

##### 

##### License

This project is for educational purposes and open for modification.



