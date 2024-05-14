import streamlit as st
from streamlit_option_menu import option_menu
import mood_board, about_the_data, project, ui


st.set_page_config(
    page_title='How are you doing today?'
)

st.markdown("""
    <style>
    /* Main content background */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=2812&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
    }

    /* Sidebar background for light theme */
    .sidebar-theme-light {
        background-image: url('https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=2812&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
    }

    /* Sidebar background for dark theme */
    .sidebar-theme-dark {
        background-image: url('https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=2812&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
    }

    /* Sidebar background color */
    .css-1d391kg {
        background-color: #333333;  /* Set your desired sidebar background color */
    }

    /* Surrounding sidebar area background color */
    .css-1d391kg .css-1lcbmhc {
        background-color: #444444;  /* Set your desired surrounding area background color */
    }
    </style>
    <script>
    // Observe theme changes and update sidebar styles accordingly
    const observer = new MutationObserver((mutationsList, observer) => {
        for(const mutation of mutationsList) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                const body = document.querySelector('body');
                const sidebar = document.querySelector('.css-1d391kg');  // Adjust this class if needed
                const sidebarContainer = document.querySelector('.css-1d391kg .css-1lcbmhc');  // Adjust this class if needed
                if (body.classList.contains('theme--dark')) {
                    sidebar.style.backgroundColor = '#333333';  // Dark theme sidebar background color
                    sidebarContainer.style.backgroundColor = '#444444';  // Dark theme surrounding area background color
                } else {
                    sidebar.style.backgroundColor = '#e0e0e0';  // Light theme sidebar background color
                    sidebarContainer.style.backgroundColor = '#f0f0f0';  // Light theme surrounding area background color
                }
            }
        }
    });
    observer.observe(document.querySelector('body'), { attributes: true });
    </script>
    """, unsafe_allow_html=True)



# # Custom CSS to set background images
# st.markdown("""
#     <style>
#     /* Main content background */
#     .stApp {
#         background-image: url('https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=2812&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
#         background-size: cover;
#     }

#     /* Sidebar background for light theme */
#     .sidebar-theme-light {
#         background-image: url('https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=2812&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
#         background-size: cover;
#     }

#     /* Sidebar background for dark theme */
#     .sidebar-theme-dark {
#         background-image: url('https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=2812&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
#         background-size: cover;
#     }
#     </style>
#     <script>
#     // Observe theme changes and update sidebar styles accordingly
#     const observer = new MutationObserver((mutationsList, observer) => {
#         for(const mutation of mutationsList) {
#             if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
#                 const body = document.querySelector('body');
#                 const sidebar = document.querySelector('.css-1d391kg'); // Sidebar class may change
#                 if (body.classList.contains('theme--dark')) {
#                     sidebar.classList.add('sidebar-theme-dark');
#                     sidebar.classList.remove('sidebar-theme-light');
#                 } else {
#                     sidebar.classList.add('sidebar-theme-light');
#                     sidebar.classList.remove('sidebar-theme-dark');
#                 }
#             }
#         }
#     });
#     observer.observe(document.querySelector('body'), { attributes: true });
#     </script>
#     """, unsafe_allow_html=True)


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
        "container": {"padding": "30!important"},
        "icon": {"font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"10px"},
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
