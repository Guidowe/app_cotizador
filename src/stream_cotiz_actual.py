import streamlit as st
import pandas as pd
from services.supabase_service import save_cotization
from services.supabase_service import get_cotization_number
from funciones.pdf_generator import generate_pdf
from datetime import datetime
from services.supabase_service import save_cotization
from services.supabase_service import get_cotization_number
import time
from datetime import datetime


# Load client data from Excel
CLIENTS_PATH = "src/data/Base de datos cientes - contactos MAGAYA.xlsx"
CONCEPTS_PATH = "src/data/MAGAYA Products and Services list.xlsx"
clients_df = pd.read_excel(CLIENTS_PATH)
conceptos_df = pd.read_excel(CONCEPTS_PATH)

def show_page_cotizar():
    st.title("Cotizador")

    col1, col2 = st.columns(2)

    with col1:
    # --- Información del cliente con autocompletado ---
        st.subheader("EMPRESA CLIENTE")
        empresa_list = clients_df["EMPRESA CLIENTE"].astype(str).unique().tolist()
        empresa_cliente = st.selectbox("EMPRESA CLIENTE", empresa_list, key="empresa_cliente")

    # Buscar datos del cliente seleccionado
        cliente_info = clients_df[clients_df["EMPRESA CLIENTE"] == empresa_cliente].iloc[0] if empresa_cliente in clients_df["EMPRESA CLIENTE"].values else None

        contacto_cliente = cliente_info["CONTACTO CLIENTE"] if cliente_info is not None else ""
        referencia_cliente = cliente_info["REFERENCIA CLIENTE"] if cliente_info is not None else ""

        st.subheader("CONTACTO CLIENTE")
        st.text_input("CONTACTO CLIENTE", value=contacto_cliente, key="contacto_cliente", disabled=True)
        st.subheader("REFERENCIA CLIENTE")
        st.text_input("REFERENCIA CLIENTE", value=referencia_cliente, key="referencia_cliente", disabled=True)

    with col2:

    # --- Lista de conceptos editable ---
        st.subheader("CONCEPTOS A COTIZAR")

        tipos_disponibles = conceptos_df["type"].unique().tolist()
        tipos_seleccionados = st.multiselect(
        "Selecciona los conceptos a agregar",
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
            st.write(f"**Total cotizado:** ${total:,.2f}")
        else:
            st.info("Selecciona al menos un concepto para editar.")

    # --- Términos y firma ---
    n_cotizacion = get_cotization_number()
    cotiz_formato = f"# {int(n_cotizacion):04d}"
    fecha = datetime.now().strftime("%d/%m/%Y")
    st.write(f"**N° DE COTIZACIÓN:** # {int(n_cotizacion):04d}")
    st.write(f"**FECHA:** {fecha}")
    firma_usuario = st.text_input("FIRMA (usuario)")

    # --- Botón para generar cotización ---
    if st.button("Generar Cotización"):
        if empresa_cliente and contacto_cliente and referencia_cliente and not conceptos_seleccionados_df.empty:
            pdf_bytes = generate_pdf(cotiz_formato,empresa_cliente, conceptos_seleccionados_df, total)
            save_cotization(n_cotizacion,fecha,empresa_cliente,total)

            st.success("¡Cotización generada correctamente!")
            st.download_button(
            label="Descargar PDF de Cotización",
            data=pdf_bytes,
            file_name=f"Cotizacion_{n_cotizacion}.pdf",
            mime="application/pdf"
        )

        else:
            st.error("Por favor, completa todos los campos y revisa la lista de conceptos.")
if __name__ == "__main__":
    while True:
        show_page_cotizar()
        time.sleep(60)  
        st.experimental_rerun() 