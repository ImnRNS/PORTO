import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Create the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('porto.html')

# Define a route for the index page
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# Define a route to get information
@app.route('/info', methods=['GET'])
def get_info():
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify({'msg': 'GET info'})

# Define a route to post information
@app.route('/info', methods=['POST'])
def post_info():
    my_name = request.form['my_name']
    print(my_name)
    return jsonify({'msg': 'POST info'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)