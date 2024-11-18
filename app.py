from flask import Flask, render_template, request, jsonify
import openai


app = Flask(__name__)


# Set your OpenAI API key
openai.api_key = "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"


# Default system message
system_msg = (
    "You are a helpful assistant that answers only front-end development-related questions. "
    "If the user asks anything unrelated to front-end development, respond in a funny or sarcastic way, indicating you don't know the answer, and encourage them to ask front-end questions instead. "
    "However, if someone asks about Bitloops or anything about Bitloops, answer that question normally. Don't answer any question too sarcastically or funnily. "
    "All messages should not be too humorous or sarcastic. I just want them to sound a little funny, otherwise they should be formal. "
    "YOU SHOULD ONLY ANSWER QUESTIONS RELATED TO FRONT-END AND BITLOOPS. DONT EVEN HINT TOWARDS THE ANSWER FOR ANY GENERIC QUESTIONS. "
    "Moreover, all the responses should be short, concise & crisp. Expand only when requested / indicated. None of the responses should be very sarcastic. They should be formal."
)


# Chat messages will be stored here
messages = [{"role": "system", "content": system_msg}]




@app.route('/')
def index():
    return render_template('index.html')




@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    messages.append({"role": "user", "content": user_input})




    # Call OpenAI API to get the assistant's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})




    return jsonify({"reply": reply})




if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template




app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
