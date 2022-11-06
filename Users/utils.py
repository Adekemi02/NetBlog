import os
import secrets
from PIL import Image
from market import app

# FUNCTION TO SAVE THE USER'S PROFILE PICTURE
def save_image(profile_image):
    generate_random = secrets.token_hex(8)
    _, file_ext = os.path.splitext(profile_image.filename)
    image_filename = generate_random + file_ext
    image_path = os.path.join(app.root_path, 'static/profile_pics', image_filename)

    image_size = (125, 125)
    i = Image.open(profile_image)
    i.thumbnail(image_size)

    i.save(image_path)

    return image_filename