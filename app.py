import os
from flask import Flask, render_template, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_url', methods=['POST'])
def fetch_url():
    target_file = request.form['target_file']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    auth = (username, password)

    urls = []
    with open('urls.txt', 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    results = []
    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(f"{url}/{target_file}", auth=auth)
            elapsed_time = time.time() - start_time
            results.append({
                'url': url,
                'status_code': response.status_code,
                'response_time': elapsed_time,
                'http_status': 'success' if response.status_code == 200 else 'failure'
            })
        except Exception as e:
            results.append({
                'url': url,
                'status_code': 'N/A',
                'response_time': 'N/A',
                'http_status': 'failure'
            })

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
