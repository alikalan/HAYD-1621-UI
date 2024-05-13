import streamlit as st
import requests
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow import expand_dims
from tensorflow import tile
from keras.applications.imagenet_utils import preprocess_input
import io

st.markdown("""# how are you dong, today?
## I hope you're doing well...
Can you post a picture reflecting your current emotion?""")
picture = st.camera_input('Take a picture')

# picture = st.file_uploader('Take a picture')

# url = 'https://hayd1621-2gsmvh4vlq-ew.a.run.app'
url = 'http://127.0.0.1:8000/upload_your_nice_face'


if picture is not None:

    # The key 'img' is the name of the form field for the file upload
    files = {'img': picture}
    # Send the POST request with the image file
    response = requests.post(url, files=files)
    # Resize the image to (224, 224)
    #img = img.resize((224, 224))
    print('* * * picture taken * * *')
    print(response.reason)
    print(response.content)
