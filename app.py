from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/my_life')
def my_life():
    return render_template('my_life.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
