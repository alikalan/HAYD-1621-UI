import streamlit as st
import requests
import json
import time
import openai
from params import *

openai.api_key = OPENAI_API_KEY

def app():

    # Set session_state to not done
    if 'picture' not in st.session_state:
        st.session_state['picture']='not done'

    # creating to columns with 0.3/0.7 relation
    st.title(f'HOW ARE YOU DOING TODAY ?')

    st.write(f"### :orange[&#x2600; TIME TO CHECK YOUR EMOTIONS] ")

    col1,col2 = st.columns([0.99,0.01])

    # Create tabs with two options
    tab1, tab2, = st.tabs(["Take a Picture 📸", "Upload a Picture ⬆️"])

    #styling the tabs; color, font size
    st.markdown("""
    <style>
    :root {
        --background-color-light: rgba(255, 255, 255, 0.6);
        --text-color-light: #000;
        --border-color-light: #ccc;
        --background-color-dark: rgba(0, 0, 0, 0.6);
        --text-color-dark: #ff6347;
        --border-color-dark: #444;
    }

    .tabs {
        display: flex;
        border-bottom: 1px solid var(--border-color-light);
        margin-bottom: 20px;
    }

    .tab {
        padding: 10px 20px;
        cursor: pointer;
        border: 1px solid transparent;
        border-radius: 4px 4px 0 0;
        transition: background-color 0.3s, color 0.3s;
        background-color: var(--background-color-light);
        color: var(--text-color-light);
        mix-blend-mode: multiply;
    }

    .tab:hover {
        background-color: rgba(0, 0, 0, 0.1);
    }

    [data-theme="dark"] .tabs {
        border-bottom-color: var(--border-color-dark);
    }

    [data-theme="dark"] .tab {
        background-color: var(--background-color-dark);
        color: var(--text-color-dark);
    }

    [data-theme="dark"] .tab:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }

    </style>
""", unsafe_allow_html=True)

    # function to track changes on the session_state
    def change_picture_state():
        st.session_state['picture']='done'

    ### changing the input method
    picture = None
    picture_upload = None
    picture_camera = None

    picture_upload = tab2.file_uploader("Please upload a picture", on_change=change_picture_state)
    picture_camera = tab1.camera_input("Please take a picture 🤳", on_change=change_picture_state)


    url = 'https://hayd1621-v3-lempkfijgq-ew.a.run.app//upload_your_nice_face'
    # url = 'http://127.0.0.1:8000/upload_your_nice_face'

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
            # result = f"{key} : {round(value,2)}%"
            emotion_list.append(key)

        if st.session_state['picture'] == 'done':
            progress_bar = col1.progress(0)

            for percentage in range(100):
                time.sleep(0.02)
                progress_bar.progress(percentage+1)

            col1.success("Picture uploaded successfully!")

            # create some balloons
            #st.balloons()

            #with st.expander("See your results:"):
            if len(emotion_list) == 1:
                st.write(f"### It seems like you're feeling {emotion_list[0]} today")
                prompt =  f"""
                I'm feeling {emotion_list[0]} today.
                Can you give me three tips for what to do with the rest of my day?
                """
            else:
                st.write(f"### It seems like you're feeling {emotion_list[0]} today, and maybe a little {emotion_list[1]}.")
                prompt =  f"""
                I'm feeling {emotion_list[0]} today, and maybe a little {emotion_list[1]}.
                Can you give me three tips for what to do with the rest of my day?
                """

            top_mood = next(iter(data_dict))
            mood_list = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
            mood_int = int(mood_list.index(top_mood))

        st.write('_______________________________________________')
        st.write(f"##### If you're satisfied with the result, update your mood board!")
        st.write(f"##### Othewise, take another picture.")
        bq_url = 'https://hayd1621-v3-lempkfijgq-ew.a.run.app/save_to_bq'
        # bq_url = 'http://127.0.0.1:8000/save_to_bq'

        st.markdown("""
            <style>
            /* Change the background color of the button */
            .stButton>button {
                background-color: #ff6347; /* Set your desired background color */
                color: white; /* Set text color */
            }
            /* Hover effect for the button */
            .stButton>button:hover {
                background-color: ##60b4ff; /* Set your desired hover background color */
                color: white; /* Set hover text color */
            }
            </style>
        """, unsafe_allow_html=True)

        ### Update to Mood Board

        # cols_mb = st.columns([1, 1, 1])
        # with cols_mb[1]:
        if st.button('Save to mood board!'):
            bq_response = requests.get(bq_url, params={'val': mood_int})
            if bq_response.status_code == 200:
                st.success("Today's mood was successfully saved to the Mood Board!")
            else:
                st.error('Failed to save data to Mood Board.')

        ### OpenAPI integration

        def get_completion(prompt, model="gpt-3.5-turbo-16k"):
            messages = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=1, # this is the degree of randomness of the model's output
            )
            return response.choices[0].message["content"]

        reply = None
        user_input = None

        st.write("Do you want some suggestions for what to do with the rest of your day?")
        # cols_openai = st.columns([1, 1, 1, 1, 1, 1])
        # with cols_openai[0]:
        if st.button("Yes!"):
            st.session_state['chat_with_ai'] = True
        # with cols_openai[1]:
        if st.button("No."):
            st.session_state['chat_with_ai'] = False
            reply = "Ok! No problem :)"

    if 'chat_with_ai' in st.session_state:
        if st.session_state['chat_with_ai']==True:
            user_input = st.text_input("Tell me a bit about yourself and why you are feeling this way", "")
            # cols_submit = st.columns([1, 1, 1, 1, 1, 1, 1])
            # with cols_submit[3]:
            full_prompt = " ".join([prompt, user_input])
            if st.button("Submit!"):
                reply = get_completion(full_prompt)
            st.text_area("ai_reply", label_visibility="hidden", value=reply, height=400)
        else:
            st.text_area("bye", label_visibility="hidden", value=reply, height=400)
