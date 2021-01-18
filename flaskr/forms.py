from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField

class UploadForm(FlaskForm):

    file_upload = FileField(label='Upload a file with one of the following extensions: .txt, .wav, .jpg, .jpeg, .png', 
                            validators=[DataRequired(), FileAllowed(['txt', 'wav', 'jpg', 'jpeg', 'png'], message='Non-compatible file type')])
    submit = SubmitField('Upload!')