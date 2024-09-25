from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML file

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # Get JSON data from the frontend
    input_value = data.get('inputValue')  # Extract input value
    result = my_algorithm(input_value)  # Call your processing function
    return jsonify({'result': result})  # Return the result as JSON

def my_algorithm(input_value):
    return int(input_value) ** 2  # Example algorithm to square the input

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Run on port 5000
