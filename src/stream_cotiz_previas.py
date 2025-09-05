from services.supabase_service import get_previous_cotizations
from services.supabase_service import get_previous_cotizations_detail
import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
import time

def show_page_cotiz_prev():
    cotizaciones_previas = get_previous_cotizations()
    st.write("**Previous quotations:**")
    st.dataframe(cotizaciones_previas[["quotation","client","date", "total"]])
    st.write("**Search for details of a specific quotation:**")
    #quotations_available = cotizaciones_previas["quotation"].unique().tolist()
    numero = st.text_input("Pick quotation by number")
    if not numero.strip() == "":
        previous_cotization_detail = get_previous_cotizations_detail(numero)
        st.dataframe(previous_cotization_detail[["quotation","client","date","type","Amount","description"]])
    else:
        st.info("Pick one quotation number to see details")


if __name__ == "__main__":
    while True:
        show_page_cotiz_prev()
        time.sleep(60)  
        st.experimental_rerun() 