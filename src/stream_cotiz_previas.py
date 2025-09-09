from services.supabase_service import get_previous_cotizations
from services.supabase_service import get_previous_cotizations_detail
from funciones import pdf_generator

import streamlit as st
import pandas as pd
import time

def show_page_cotiz_prev():
    cotizaciones_previas = get_previous_cotizations()
    st.write("**Previous quotations:**")
    st.dataframe(cotizaciones_previas[["quotation","reference_quote","client","date"]])
    st.write("**Search for details of a specific quotation:**")
    #quotations_available = cotizaciones_previas["quotation"].unique().tolist()
    numero = st.text_input("Pick quotation by number")
    if not numero.strip() == "":
        previous_cotization_detail = get_previous_cotizations_detail(numero)
        df_previous_cot= previous_cotization_detail[["quotation","client","date","type","Amount","description"]]
        st.dataframe(df_previous_cot)
        client_info = previous_cotization_detail.client.values[0]
        date = previous_cotization_detail.date.values[0]
        seller = previous_cotization_detail.seller.values[0]
        refe_quote = previous_cotization_detail.reference_quote.values[0]
        concepts = df_previous_cot[["type", "Amount", "description"]]
        if st.button("Regenerate PDF"):
            pdf_reg = pdf_generator.generate_pdf(numero, client_info, date,seller,refe_quote,concepts, total_amount=0)
            st.download_button(
                label="Download Quotation PDF",
                data=pdf_reg,
                file_name=f"Quotation_{numero}.pdf",
                mime="application/pdf" # PENDIENTE
            )
    else:
        st.info("Pick one quotation number to see details")


if __name__ == "__main__":
    while True:
        show_page_cotiz_prev()
        time.sleep(60)  
        st.experimental_rerun() 