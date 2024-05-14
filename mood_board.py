import streamlit as st

def app():

    st.write(f'## Store all the moods from images')

    # Define legend labels and corresponding colors
    legend_data = {
        "Happy": "#6DDA76",
        "Angry": "#D82F2F",
        "Test Color": "#fad20c"
    }

    # Display legend using Markdown
    st.markdown("## Legend")
    for label, color in legend_data.items():
        st.markdown(f"<font color='{color}'> &#9632; </font> {label}", unsafe_allow_html=True)
