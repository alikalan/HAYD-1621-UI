import streamlit as st
from streamlit_option_menu import option_menu
import mood_board, about_the_data, project, ui


st.set_page_config(
    page_title='How are you doing today?'
)

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
        menu_title = 'How are you doing?',
        options = ['Emotions App', 'Project', 'Mood Board', 'About the data'],
        icons = ['app-indicator', 'info-square', 'table', 'database'],
        menu_icon = 'emoji-smile-fill',
        default_index = 0,
        orientation = 'horizontal',
        styles={
        "container": {"padding": "30!important", "background-color": "black"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"10px", "color": "white"},
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
