from flask import Flask, render_template, request, jsonify
import json
from maestro import Controller
import random
import time
import threading
import math

app = Flask(__name__)
x=Controller()




@app.route('/')
def index():
    return render_template('index.html')

image_urls = [
    "static/eyes.png",
    "static/eyes2.png",
    "static/eyes3.png",
    "static/eyes4.png",
    "static/eyes5.png"
    "static/robot.gif",
]
global current_image
current_image = 5

@app.route('/view')
def view():
    # Choose a random image URL from the list
    random_image_url = random.choice(image_urls)
    return render_template('view.html', image_url=random_image_url)

@app.route('/get_image')
def get_image():
    # Choose a random image URL from the list
    random_image_url = image_urls[current_image]
    return jsonify({"image_url": random_image_url})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    joystick_x = data['joystick_x']
    joystick_y = data['joystick_y']
    slider1 = data['slider1']
    slider2 = data['slider2']
    slider3 = data['slider3']
    global current_image
    current_image=0
    if(int(slider2)>=2):
        current_image=2
    if(int(slider2)<=-2):
        current_image=1
    if(int(slider3)>=2):
        current_image=3
    if(int(slider3)<=-2):
        current_image=4
    if(max([abs(int(joystick_x)),abs(int(joystick_y))])>1):
        print("Moving")
        current_image=5
    
    
    # Call the move function with joystick and slider values
    move(joystick_x, joystick_y, slider1, slider2, slider3)
    
    return 'Data received successfully'

def move(joystick_x, joystick_y, slider1, slider2, slider3):
    # Your move function implementation here
    print("Joystick X:", joystick_x)
    print("Joystick Y:", joystick_y)
    print("Slider 1:", slider1)
    print("Slider 2:", slider2)
    print("Slider 3:", slider3)
    Speed=(joystick_y/100)*1500
    Delta=(joystick_x/100)*1500
    print("Speed:",(joystick_y/100)*1000+6000)
    print("Delta:",(joystick_x/100)*1000)
    print("LWS:",Speed+Delta)
    print("RWS:",Speed-Delta)
    x.setTarget(1,6000-int(Speed-Delta))
    x.setTarget(2,6000+int(Speed+Delta))
    x.setTarget(0,6000+int(slider1)*400)
    x.setTarget(3,6000+int(slider2)*250)
    x.setTarget(4,6000+int(slider3)*250)

if __name__ == '__main__':
    app.run(debug=True)