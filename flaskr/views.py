from flask import render_template, url_for, redirect, flash, send_file, get_flashed_messages
from flaskr import app
from flaskr.forms import UploadForm
from flaskr.file_handler import handle_file
from util.read_files import audio_to_string, text_to_string, image_to_string
from util.summarize import summarize
import os 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    form = UploadForm()

    if form.validate_on_submit():
        file_upload = form.file_upload.data
        path, extension = handle_file(file_upload)

        try:
                if extension == 'wav':
                    data = audio_to_string(path)
                elif extension == 'txt':
                    data = text_to_string(path)
                else:
                    data = image_to_string(path)
            
                summary = summarize(data)
                summary_file = open(os.path.join(os.path.dirname(__file__), 'data/summary.txt'), 'w')
                summary_file.write(summary)
                summary_file.close()
        except:
            return redirect(url_for('corrupted'))

        return send_file(os.path.join(os.path.dirname(__file__), 'data/summary.txt'), as_attachment=True)

    return render_template('upload.html', title='Try it Out', form=form, messages=get_flashed_messages())

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/corrupted')
def corrupted():
    return render_template('corrupted.html')