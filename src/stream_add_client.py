import streamlit as st
from services.supabase_service import save_new_client
from services.supabase_service import retrieve_clients
import time

def show_page_add_client():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Add a new client to the database")

        client_name = st.text_input("Detail client/enterprise name")
        client_contact = st.text_input("Detail client email")
        client_reference = st.text_input("Client reference")

        if st.button("Save client in database"):
            if client_name and client_contact and client_reference:
                save_new_client(client_name,client_contact,client_reference)
                st.success("Client saved successfully!")            
            else:
                st.error("Please complete all fields")
    with col2:
        existing_clients = retrieve_clients()
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        st.title("Existing Clients")
=======
        st.title("Existent Clients")
>>>>>>> Stashed changes
=======
        st.title("Existent Clients")
>>>>>>> Stashed changes
        st.dataframe(existing_clients)

if __name__ == "__main__":
    while True:
        show_page_add_client()
        time.sleep(10)  
        st.experimental_rerun() 