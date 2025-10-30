from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form.get('username', '')
    # Server-side escape to prevent XSS
    safe_username = escape(username)
    return render_template('result.html', username=safe_username)

if __name__ == '__main__':
    # Don't run with debug=True in production
    app.run(host='127.0.0.1', port=5000, debug=False)
