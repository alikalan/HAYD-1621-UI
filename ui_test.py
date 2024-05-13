import streamlit as st
import requests

st.markdown("""# how are you doing, today?
## I hope you're doing well...
Can you post a picture reflecting your current emotion?""")
picture = st.camera_input('Take a picture')
# picture = st.file_uploader('Take a picture')

url = 'https://hayd1621-docker-v2-lempkfijgq-uc.a.run.app/upload_your_nice_face'
# url = 'http://127.0.0.1:8000/upload_your_nice_face'

if picture is not None:

    # The key 'img' is the name of the form field for the file upload
    files = {'img': picture}
    # Send the POST request with the image file
    response = requests.post(url, files=files)
    # Resize the image to (224, 224)
    #img = img.resize((224, 224))
    print('* * * picture taken * * *')
    print(response.reason)
    response.content
