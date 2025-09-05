import streamlit as st
from services.supabase_service import save_concept
import time

def show_page_add_concept():
    st.title("Add a new concept to the database")

    Code = st.text_input("Enter code of the concept")
    account = st.text_input("Enter account name")
    type = st.text_input("Enter type of concept")
    ammount = st.text_input("Enter default ammount")
    description = st.text_input("Enter description")

    if st.button("Save concept in database"):
        if Code and account and type and ammount:
            save_concept(Code,account,type,ammount,description)
            st.success("Concept saved successfully!")            
        else:
            st.error("Please complete all fields")

if __name__ == "__main__":
    while True:
        show_page_add_concept()
        time.sleep(10)  
        st.experimental_rerun() 