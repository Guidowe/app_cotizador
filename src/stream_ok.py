import streamlit as st
import stream_cotiz_previas
import stream_cotiz_actual
import stream_add_client
import stream_add_concept
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
#import yaml
#from yaml.loader import SafeLoader

st.set_page_config(page_title="DGM quotes", 
                   page_icon="📄", 
                   layout="wide")
refresh_interval_ms = 60 * 1000  # 30 seconds in milliseconds
count = st_autorefresh(interval=refresh_interval_ms, limit=None, key="auto-refresh")

#with open('config.yaml') as file:
#    config = yaml.load(file, Loader=SafeLoader)

#authenticator = stauth.Authenticate(
#    config['credentials'],
#    config['cookie']['name'],
#    config['cookie']['key'],
#    config['cookie']['expiry_days']
#)
# Hardcoded credentials (store securely in production!)
USERNAMES = ["admin"]
PASSWORDS = ["admin"]

def check_login(username, password):
    return username in USERNAMES and password in PASSWORDS

# Login form
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()#A
        else:
            st.error("Invalid username or password.")
    st.stop()  # Prevents rest of app from showing until logged in
col1, col2 = st.columns([7, 1])
with col1:
        st.markdown(
        """
        <div style="background-color:#43b02a;padding:20px 10px 10px 10px;border-radius:8px;">
            <h1 style="color:white;margin-bottom:0;">DGM - Quotation System</h1>
        </div>
        """,
        unsafe_allow_html=True
        )
with col2:
    st.image("src/img/logo_dgm.jpg", use_container_width =True)

st.markdown(
    """
    <div style="height:2px;border-radius:6px;margin-bottom:10px;"></div>
    """,
    unsafe_allow_html=True
    )

col3, col4 = st.columns([7, 1])
with col3:
    page_selection = option_menu(
                None,  # No menu title
                ["Create Quote", "Previous quotations","Add client","Add concept"],  # List of menu items
                icons=["arrow-down-circle", "arrow-up-circle","person-plus",""],  # List of icons for each item
                menu_icon="cast",  
                default_index=0, 
                orientation="horizontal",
                styles={
                "container": {"padding": "0!important", "background-color": "#B4A7A7F4"},
                "icon": {"color": "white", "font-size": "18px"},
                "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "margin": "0px",
                "color": "white",
            },
            "nav-link-selected": {
                "background-color": "#43b02a",
                "color": "white",
            },
        })

if page_selection == "Create Quote":
    stream_cotiz_actual.show_page_cotizar()
if page_selection == "Previous quotations":
    stream_cotiz_previas.show_page_cotiz_prev()
if page_selection == "Add client":
    stream_add_client.show_page_add_client()    
if page_selection == "Add concept":
    stream_add_concept.show_page_add_concept()
with col4:
    st.button("Logout",use_container_width=True, on_click=lambda: st.session_state.update({"logged_in": False}))
