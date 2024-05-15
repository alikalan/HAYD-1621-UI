import streamlit as st
from streamlit_option_menu import option_menu
import mood_board, about_the_data, project, ui


st.set_page_config(
    page_title='How are you doing today?'
)

# Custom CSS to change the background color of the sidebar and its surrounding area
st.markdown("""
    <style>
    /* Sidebar background */
    .css-1d391kg {  /* Adjust this class if needed, depending on Streamlit version */
        background-color: #333333;  /* Set your desired sidebar background color */
    }

    /* Surrounding sidebar area background */
    .css-1d391kg .css-1lcbmhc {  /* Adjust this class if needed, depending on Streamlit version */
        background-color: #444444;  /* Set your desired surrounding area background color */
    }
    </style>
    """, unsafe_allow_html=True)

# JavaScript to dynamically apply light or dark theme classes to the sidebar
st.markdown("""
    <script>
    const observer = new MutationObserver((mutationsList, observer) => {
        for(const mutation of mutationsList) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                const body = document.querySelector('body');
                const sidebar = document.querySelector('.css-1d391kg');  // Adjust this class if needed
                const sidebarContainer = document.querySelector('.css-1d391kg .css-1lcbmhc');  // Adjust this class if needed
                if (body.classList.contains('theme--dark')) {
                    sidebar.style.backgroundColor = '#333333';  // Dark theme sidebar background
                    sidebarContainer.style.backgroundColor = '#444444';  // Dark theme surrounding area background
                } else {
                    sidebar.style.backgroundColor = '#e0e0e0';  // Light theme sidebar background
                    sidebarContainer.style.backgroundColor = '#f0f0f0';  // Light theme surrounding area background
                }
            }
        }
    });
    observer.observe(document.querySelector('body'), { attributes: true });
    </script>
    """, unsafe_allow_html=True)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self,title,function):
        self.apps.append({
            'title': title,
            'function': function
        })

    def run():
        with st.sidebar:
            app = option_menu(
        menu_title = 'How are you doing, today?',
        options = ['Emotions App', 'Mood Board', 'Project', 'About the data'],
        icons = ['app-indicator', 'table','info-square', 'database'],
        menu_icon = 'emoji-smile-fill',
        default_index = 0,
        orientation = 'vertical',
        styles={
        "container": {"padding": "30!important"},
        "icon": {"font-size": "25px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"10px"},
        "nav-link-selected": {"background-color": "#60b4ff"},
    }
    )

        if app == 'Mood Board':
            mood_board.app()

        if app == 'Project':
            project.app()

        if app == 'About the data':
            about_the_data.app()

        if app == 'Emotions App':
            ui.app()

    run()
