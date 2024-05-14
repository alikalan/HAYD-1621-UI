import streamlit as st
import requests
import json
import time

def app():
    # Set session_state to not done
    if 'picture' not in st.session_state:
        st.session_state['picture']='not done'

    # creating to columns with 0.3/0.7 relation
    col1, col2= st.columns([0.3,0.7])

    col1.markdown("# HOW ARE YOU DOING TODAY? ")
    col1.markdown("### __________ ")
    col1.markdown("#### :orange[TIME TO CHECK YOUR EMOTIONS]")

    # function to track changes on the session_state
    def change_picture_state():
        st.session_state['picture']='done'

    ### changing the input method
    picture = None
    picture_upload = None
    picture_camera = None

    picture_upload = col2.file_uploader("Upload a picture", on_change=change_picture_state)
    picture_camera = col2.camera_input("Please take a picture", on_change=change_picture_state)


    url = 'https://hayd1621-docker-v2-lempkfijgq-uc.a.run.app/upload_your_nice_face'
    #url = 'http://127.0.0.1:8000/upload_your_nice_face'

    if picture_upload is not None:
        picture = picture_upload
    elif picture_camera is not None:
        picture = picture_camera
    if picture is not None:
        # The key 'img' is the name of the form field for the file upload
        files = {'img': picture}
        # Send the POST request with the image file
        response = requests.post(url, files=files)
        print('* * * picture taken * * *')

        #response.content
        data = response.content
        ### Decode the bytes object into a string
        data_str = data.decode('utf-8')
        ### Convert to a dict
        data_dict = json.loads(data_str)

        emotion_list = []
        # for-loop to get the keys and values
        for key, value in data_dict.items():
            result = f"{key} : {round(value,2)}%"
            emotion_list.append(result)

        if st.session_state['picture'] == 'done':
            progress_bar = col2.progress(0)

            for percentage in range(100):
                time.sleep(0.085)
                progress_bar.progress(percentage+1)

            col2.success("Picture uploaded successfully!")

            with st.expander("See your results:"):
                if len(emotion_list) == 1:
                    st.write(f'### Your detected emotions are:')
                    st.write(f'### :blue[{emotion_list[0]}]')
                else:
                    st.write(f'### Your detected emotions are:')
                    st.write(f'### :blue[{emotion_list[0]}]')
                    st.write(f'### :blue[{emotion_list[1]}]')
