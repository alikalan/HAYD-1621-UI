import streamlit as st
import requests
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow import expand_dims
from tensorflow import tile
from keras.applications.imagenet_utils import preprocess_input

st.markdown("""# how are you dong, today?
## I hope you're doing well...
Can you post a picture reflecting your current emotion?""")
picture = st.camera_input('Take a picture')

url = 'https://hayd1621-2gsmvh4vlq-ew.a.run.app'
# if picture is not None:
#     picture = preprocess_input(picture)
#     picture = pred(picture)
#     picture
if picture is not None:
    # Open the UploadedFile object using Image.open()
    img = Image.open(picture)
    # Open the image file in binary mode
    # Define the files dictionary to send with the request
    # The key 'image' is the name of the form field for the file upload
    files = {'image': img}
    # Send the POST request with the image file
    response = requests.post(url, files=files)
    # Resize the image to (224, 224)
    #img = img.resize((224, 224))
    print(type(response))
