import os
from PIL import Image

def handle_file(file_upload):
    filename = file_upload.filename
    extension = filename.split('.')[-1]
    STORAGE_FILENAME = os.path.join(os.path.dirname(__file__), f'data/input.{extension}')

    file_upload.save(STORAGE_FILENAME)
        
    return STORAGE_FILENAME, extension