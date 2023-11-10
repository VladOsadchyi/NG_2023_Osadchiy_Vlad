from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images")

image_names = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

current_image_index = 0

@app.route('/')
def index():
    return render_template('gallery.html', image_name=image_names[current_image_index])

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(image_folder, filename)

@app.route('/next_image')
def next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_names)
    return render_template('gallery.html', image_name=image_names[current_image_index])

@app.route('/prev_image')
def prev_image():
    global current_image_index
    current_image_index = (current_image_index - 1) % len(image_names)
    return render_template('gallery.html', image_name=image_names[current_image_index])



app.run()
