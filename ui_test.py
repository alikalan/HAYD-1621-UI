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

# Display camera input widget
if picture is not None:
    pil_image = Image.fromarray(picture)
    pil_image.save("captured_image.jpg")
    st.image(pil_image, caption="Captured Image")
else:
    st.write("No image captured.")

# if st.session_state.picture is not None:
#    img = Image.open(st.session_state.picture)
#    st.write(type(img))
#    params = {'img' : img}
#    response = requests.post(url, files = params)

# st.write(response)
