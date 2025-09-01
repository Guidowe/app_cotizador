import streamlit as st

st.set_page_config(page_title="DGM quotes", 
                   page_icon="📄", 
                   layout="wide")
import stream_cotiz_previas
import stream_cotiz_actual
import pandas as pd

from streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
refresh_interval_ms = 60 * 1000  # 30 seconds in milliseconds
count = st_autorefresh(interval=refresh_interval_ms, limit=None, key="auto-refresh")

col1, col2 = st.columns([1, 6])
with col1:
    st.image("src/img/logo_dgm.jpg", width=80,heigth=80)
with col2:
    st.markdown("<h1 style='margin-top: 25px;'>DGM - Quotation System</h1>", unsafe_allow_html=True)


USERNAMES = ["DASSA", "Facu","Guido"]
PASSWORDS = ["DASSA3", "123","45s62a"]

def login(username, password):
    if username in USERNAMES and password in PASSWORDS:
        return True
    return False

page_selection = option_menu(
            None,  # No menu title
            ["Create Quote", "Previous quotations"],  # List of menu items
            icons=["arrow-down-circle", "arrow-up-circle"],   
            menu_icon="cast",  
            default_index=0, 
            orientation="horizontal")

if page_selection == "Create Quote":
    stream_cotiz_actual.show_page_cotizar()
if page_selection == "Previous quotations":
    stream_cotiz_previas.show_page_cotiz_prev()