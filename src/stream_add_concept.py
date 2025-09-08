import streamlit as st
from services.supabase_service import save_concept
from services.supabase_service import retrieve_concepts
import time

def show_page_add_concept():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Add a new concept to the database")

        Code = st.text_input("Enter code of the concept")
        account = st.text_input("Enter account name")
        type = st.text_input("Enter type of concept")
        amount = st.text_input("Enter default amount")
        description = st.text_input("Enter description")

        if st.button("Save concept in database"):
            if Code and account and type and amount:
                save_concept(Code,account,type,amount,description)
                st.success("Concept saved successfully!")            
            else:
                st.error("Please complete all fields")
    with col2:
        existing_concepts = retrieve_concepts()
        st.title("Existing Concepts")
        st.dataframe(existing_concepts)

if __name__ == "__main__":
    while True:
        show_page_add_concept()
        time.sleep(10)  
        st.experimental_rerun()  