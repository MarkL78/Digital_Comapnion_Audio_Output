from flask import Flask, request, jsonify
import openai

# Initialize the Flask app
app = Flask(__name__)

# Set up OpenAI credentials
openai.api_key = "YOUR_API_KEY"

# Define a route for the API endpoint
@app.route('/api/gpt', methods=['POST'])

def generate_text():
    # Get the input data from the request
    input_data = request.json['input']

    # Generate text using the OpenAI GPT model
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_data,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the response
    output_data = response.choices[0].text.strip()

    # Return the response as JSON
    return jsonify({'output': output_data})

# Run the app
if __name__ == '__main__':
    app.run()
