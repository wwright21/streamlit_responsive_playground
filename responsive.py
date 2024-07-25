import streamlit as st
from streamlit_js_eval import streamlit_js_eval


# set page configurations
st.set_page_config(
    page_title="Responsive playground",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed" # 'collapsed' or 'expanded'
)

# get the screen height to set the heights of the map and line charts
screen_width = streamlit_js_eval(js_expressions='screen.width', key = 'SCR')

st.write(screen_width)