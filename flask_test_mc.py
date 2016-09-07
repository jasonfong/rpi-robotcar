import time
from flask import Flask
import motion

app = Flask(__name__)
ctrl = motion.Motion()

def hello():
    return "Hello Flask!"

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

def drunk():
    ctrl.forward()
    time.sleep(1)
    ctrl.right()
    time.sleep(1)
    ctrl.forward()
    time.sleep(1)
    ctrl.left()
    time.sleep(1)
    ctrl.forward()
    time.sleep(1)
    ctrl.stop()
    return "Left"


app.add_url_rule("/", "index", view_func=hello)
app.add_url_rule("/forward", "forward", view_func=forward)
app.add_url_rule("/backward", "backward", view_func=backward)
app.add_url_rule("/left", "left", view_func=left)
app.add_url_rule("/right", "right", view_func=right)
app.add_url_rule("/drunk", "drunk", view_func=drunk)
app.run(debug=True, host="0.0.0.0", port=5001)

