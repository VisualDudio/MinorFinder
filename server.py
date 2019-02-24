from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room
from DARS_parser import get_courses

app = Flask(__name__)
app.config['SECRET KEY'] = 'shhh'
app.debug = True
app.host = 'localhost'
socketio = SocketIO(app)

courses = [{
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    },
    {
        "c": "CS 241",
        "b": "Systems Programming",
        "a": "4.0"
    }
]

minor = {
    "name": "Statistics",
    "courses": courses,
    "hoursLeft": 9.0
}

minors = [minor, minor]

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('ready')
def sendMinors():
    courses = get_courses("test.html")
    socketio.emit('minors', minors)

if __name__ == "__main__":
    socketio.run(app)