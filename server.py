from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET KEY'] = 'shhh'
app.debug = True

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,host='localhost', port=4000)