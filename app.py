from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'Videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', video_uploaded=False)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Call the run_car_counter function to process the uploaded video
            return run_car_counter(filename)
    return 'Error in uploading file'

@app.route('/run_car_counter', methods=['POST'])
def run_car_counter(filename):
    if request.method == 'POST':
        
        if filename != '':
            #video_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
            #uploaded_file.save(video_path)
            # Modify the car-counter.py script to use the uploaded video path
            video_path = 'C:/Users/akash/OneDrive/Desktop/Capstone/Car-Counter-Capstone/Videos' f'/{filename}'
            command = f'python car-counter.py --video_path="{video_path}"'

            os.system(command)
            return 'Car counting process started'
    return 'Error in running car counter'

if __name__ == '__main__':
    app.run(debug=True)