import streamlit as st

def app():

    st.markdown("<p style='text-align: left;font-size: 45px;font-weight: bold;'>HOW ARE YOU DOING, TODAY?</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: right;font-size: 24px;font-weight: bold; color: #f46524;'> - THE PROJECT - </p>"
                , unsafe_allow_html=True)

    st.write('----')
    ### The Problem
    st.markdown("<p style='text-align: center;font-size: 40px;font-weight: bold; color: #2ab09d;'>THE PROBLEM</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: center;font-size: 22px;font-weight: bold;'>Most people don’t know what they feel, can’t name their emotions in detail or can’t elaborate.</p>"
                , unsafe_allow_html=True)
    st.write('----')
    ### The idea
    st.markdown("<p style='text-align: center;font-size: 40px;font-weight: bold; color: #ffd16a;'>THE IDEA</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: center;font-size: 22px;font-weight: bold;'>A simple gamified app to help people connect to their emotions in less than one minute.</p>"
                , unsafe_allow_html=True)
    st.write('----')
    ### The approach
    st.markdown("<p style='text-align: center;font-size: 40px;font-weight: bold; color: #60b4ff;'>THE APPROACH</p>"
                , unsafe_allow_html=True)

    col1,col2 = st.columns([0.3,0.7])

    col1.image('data_images/HAYD1621 - Final Front.png',caption='Picture taken on the app')
    col2.write('')
    col2.write('')
    col2.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>  Take a daily selfie</p>"
                , unsafe_allow_html=True)
    col2.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>  The app suggests your emotion of the day</p>"
                , unsafe_allow_html=True)
    col2.write('----')
    col2.markdown("<p style='text-align: left;font-size: 22px;font-weight: bold; color: #60b4ff;'>  AFTER THE PICTURE WAS TAKEN</p>"
                , unsafe_allow_html=True)
    col2.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>  The app asks you to confirm or correct</p>"
                , unsafe_allow_html=True)
    col2.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>  You can save your emotion to your Mood Board</p>"
                , unsafe_allow_html=True)

    st.write('----')
