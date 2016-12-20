import time
from flask import Flask, render_template
import motion
from ultrasonic import Ultrasonic

app = Flask(__name__)
ctrl = motion.Motion()
sensor = Ultrasonic(trig_pin=29, echo_pin=31)

def index():
    return render_template("index.html")

def forward():
    print "Onward!"
    ctrl.forward(100)
    time.sleep(1)
    ctrl.stop()
    return "Onward!"

def backward():
    print "Backwards!"
    ctrl.backward(100)
    time.sleep(1)
    ctrl.stop()
    return "Backwards!"

def left():
    print "Left"
    ctrl.left(75)
    time.sleep(1)
    ctrl.stop()
    return "Left"

def right():
    print "Right"
    ctrl.right(75)
    time.sleep(1)
    ctrl.stop()
    return "Right"

app.add_url_rule("/", "index", view_func=index)
app.add_url_rule("/forward", "forward", view_func=forward)
app.add_url_rule("/backward", "backward", view_func=backward)
app.add_url_rule("/left", "left", view_func=left)
app.add_url_rule("/right", "right", view_func=right)
app.run(debug=True, host="0.0.0.0", port=5001)

