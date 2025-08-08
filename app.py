import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

# Configure the Gemini API with your key
genai.configure(api_key="AIzaSyCAu52YMhe3nskX1NCRpSyGKMtQvEvsSck")

# Choose the model you want to use
model = genai.GenerativeModel('gemini-2.0-flash')

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Generate a response from the Gemini API
        response = model.generate_content(user_message)
        bot_response = response.text
        return jsonify({'response': bot_response})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to get a response from the chatbot.'}), 500

if __name__ == '__main__':
    # For a production environment, use a more robust server like Gunicorn or Waitress.
    app.run(debug=True)



