from services.supabase_service import get_previous_cotizations
import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
import time

def show_page_cotiz_prev():
    cotizaciones_previas = get_previous_cotizations()
    st.write("**Previous quotes:**")
    st.dataframe(cotizaciones_previas[["cotizacion","empresa_cliente", "total"]])

if __name__ == "__main__":
    while True:
        show_page_cotiz_prev()
        time.sleep(60)  
        st.experimental_rerun() 