import streamlit as st

def app():

    st.title('HOW ARE YOU DOING, TODAY?')

    col_left,col_cen,col_right = st.columns([0.4,0.35,0.25])
    col_right.markdown('### :orange[- Project - ]')
    st.write('----')
