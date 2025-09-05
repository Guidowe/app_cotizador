import streamlit as st
from services.supabase_service import save_client
import time

def show_page_add_client():
    st.title("Add a new client to the database")

    client_name = st.text_input("Detail client/enterprise name")
    client_contact = st.text_input("Detail client email")
    client_reference = st.text_input("Client reference")

    if st.button("Save client in database"):
        if client_name and client_contact and client_reference:
            save_client(client_name,client_contact,client_reference)
            st.success("Client saved successfully!")            
        else:
            st.error("Please complete all fields")

if __name__ == "__main__":
    while True:
        show_page_add_client()
        time.sleep(10)  
        st.experimental_rerun() 