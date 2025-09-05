import streamlit as st
import pandas as pd
from services.supabase_service import get_cotization_number
from funciones.pdf_generator import generate_pdf
from datetime import datetime
from services.supabase_service import save_cotization
from services.supabase_service import save_cotization_detail
from services.supabase_service import retrieve_clients
import time
from datetime import datetime


# Load client data from Excel
#CLIENTS_PATH = "src/data/Base de datos cientes - contactos MAGAYA.xlsx"
CONCEPTS_PATH = "src/data/MAGAYA Products and Services list.xlsx"
#clients_df = pd.read_excel(CLIENTS_PATH)
conceptos_df = pd.read_excel(CONCEPTS_PATH)
clients_df = retrieve_clients()
def show_page_cotizar():
    st.title("Create a new quote")

    col1, col2 = st.columns(2)

    with col1:
    # --- Información del cliente con autocompletado ---
        st.subheader("CLIENT")
        empresa_list = clients_df["client"].astype(str).unique().tolist()
        empresa_cliente = st.selectbox("Select Client", empresa_list, key="empresa_cliente")

    # Buscar datos del cliente seleccionado
        cliente_info = clients_df[clients_df["client"] == empresa_cliente].iloc[0] if empresa_cliente in clients_df["client"].values else None

        contacto_cliente = cliente_info["contact"] if cliente_info is not None else ""
        referencia_cliente = cliente_info["reference"] if cliente_info is not None else ""

        st.text_input("Client mail", value=contacto_cliente, key="contacto_cliente", disabled=True)
        st.text_input("Reference Client", value=referencia_cliente, key="referencia_cliente", disabled=True)

    with col2:

    # --- Lista de conceptos editable ---
        st.subheader("ITEMS TO QUOTE")

        tipos_disponibles = conceptos_df["type"].unique().tolist()
        tipos_seleccionados = st.multiselect(
        "Pick items to be quoted",
        tipos_disponibles
        )

    # Filtra los conceptos seleccionados
        conceptos_seleccionados_df = conceptos_df[conceptos_df["type"].isin(tipos_seleccionados)].copy()

    # Permite editar VALOR y DESCRIPCIÓN
        if not conceptos_seleccionados_df.empty:
            conceptos_seleccionados_df = st.data_editor(
                conceptos_seleccionados_df[["type", "Amount", "description"]],
                num_rows="dynamic",
                use_container_width=True,
                key="conceptos_editor"
            )
            total = conceptos_seleccionados_df["Amount"].sum()
            #st.write(f"**Total quoted:** ${total:,.2f}")
        else:
            st.info("Pick at least one item to quote")

    # --- Términos y firma ---
    n_cotizacion = get_cotization_number()
    cotiz_formato = f"# {int(n_cotizacion):04d}"
    fecha = datetime.now().strftime("%d/%m/%Y")
    st.write(f"**Quote N°:** # {int(n_cotizacion):04d}")
    st.write(f"**Date:** {fecha}")
    refe_quote = st.text_input("Enter a reference for this quotation")
    seller = st.text_input("Seller. Specify who is making the quotation")

    # --- Botón para generar cotización ---
    if st.button("Generate quote"):
        if empresa_cliente and contacto_cliente and referencia_cliente and seller and refe_quote and not conceptos_seleccionados_df.empty:
            pdf_bytes = generate_pdf(cotiz_formato,empresa_cliente,fecha,seller,refe_quote, conceptos_seleccionados_df, total)
            save_cotization(n_cotizacion,fecha,empresa_cliente,total)
            save_cotization_detail(n_cotizacion,fecha,empresa_cliente,conceptos_seleccionados_df)

            st.success("Quote generated successfully!")
            st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name=f"Quote_{n_cotizacion}.pdf",
            mime="application/pdf"
        )

        else:
            st.error("Please complete all fields and check the items to be quoted.")
if __name__ == "__main__":
    while True:
        show_page_cotizar()
        time.sleep(60)  
        st.experimental_rerun() 