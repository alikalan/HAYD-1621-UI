import streamlit as st
import requests

import numpy as np
import pandas as pd
from PIL import Image

st.markdown("""# how are you doing, today?
## I hope you're doing well...
Can you post a picture reflecting your current emotion?""")

picture = st.camera_input("Take a picture")
url = 'http://127.0.0.1:8000/upload_your_nice_face'
print(picture)

if picture:
    img = Image.open(picture)
    st.write(type(img))
    params = {'img' : img}
    response = requests.post(url, files = params)



# st.write(response)
