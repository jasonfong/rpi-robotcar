import time
from flask import Flask
import motion

app = Flask(__name__)
ctrl = motion.Motion()

def hello():
    return "Hello Flask!"

def forward():
    print "Onward!"
    ctrl.forward()
    time.sleep(3)
    ctrl.stop()
    return "Onward!"

def left():
    print "Left"
    ctrl.left()
    time.sleep(3)
    ctrl.stop()
    return "Left"

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
app.add_url_rule("/left", "left", view_func=left)
app.add_url_rule("/drunk", "drunk", view_func=drunk)
app.run(debug=True, host="0.0.0.0", port=5001)

