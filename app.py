import os
from flask import Flask, request, jsonify
from flask import send_from_directory
import openai

# For loading environment variables
from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__, static_folder='public')

# Serve the index.html from the 'public' folder at the root URL
@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

# If you have other static assets like CSS, images, etc.,
# Flask will automatically serve them from the 'public' folder,
# e.g. GET /style.css -> public/style.css

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    This is the endpoint the frontend calls with a JSON payload like:
    {
      "message": "User's question"
    }
    """
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        # Call OpenAI's Chat Completion
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # or "gpt-3.5-turbo"
            messages=[
                {
                    "role": "system",
                    "content": 
                    "You are a Syrian Arabic expert. Always respond in an informal Syrian dialect, whether in arabic letters or latin letters + english depends on the language you resieved the question in."
                    "answer with arabic in latin + english if your question camme in english, this means the student does not know arabic or how to read"
                    "answer in the syrian arabic if the quesiotn came in arabic, this means the student is arab" 
                    "Never use Modern Standard Arabic. Keep your tone very cool and helpful, use sarcasim if you think its needed"
                    "dont be sarcastic always, only when you think it's needed, be balled"
                    "the main goal is to help in developing the users's syrian dialect skills, suggest words with translation and other stuff"
                    "your mission is to help the students study and learn the syrian dialect, try to teach them words, give them summs, information, be talkative and avoide answering political stuff"
                    "when asked about the 5 psedu verbs, they are verbs that dont congugate like other normal vers, they are: بد، في، عند، لازم، معي، مثلا: انا بدي اروح، انا لازمني اشتري، انا فيني امشي "
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,
            max_tokens=250,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )
        ai_reply = response['choices'][0]['message']['content']
        return jsonify({"reply": ai_reply})
    
    except Exception as e:
        # Return an error if something goes wrong
        return jsonify({"error": str(e)}), 500

# Run the Flask server (development mode)
if __name__ == '__main__':
    # Make sure debug=False in production
    app.run(debug=True, host='0.0.0.0', port=5000)
