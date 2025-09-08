from supabase import create_client, Client
import pandas as pd
from tokens import url, key

#import os
#url = os.getenv("url_supabase")
#key = os.getenv("key_supabase")

supabase: Client = create_client(url, key)

def get_previous_cotizations():
    tabla_supabase = supabase.table("quotations").select("*").execute()
    cotizaciones_previas = pd.DataFrame(tabla_supabase.data)
    return cotizaciones_previas

def get_previous_cotizations_detail(number):
    supabase_detail = supabase.table("quotations_detail").select("*").eq("quotation", number).execute()
    previous_cotization_detail = pd.DataFrame(supabase_detail.data)
    return previous_cotization_detail

def get_cotization_number():
    cotizaciones_previas = get_previous_cotizations()
    cotizacion_actual = cotizaciones_previas.iloc[-1]["quotation"]+1
    return cotizacion_actual

def save_cotization(in_cotizacion,in_fecha,in_empresa_cliente,in_total,refe_quote,seller):
    response = supabase.table('quotations').insert({
        'quotation': int(in_cotizacion),
        'client': in_empresa_cliente,
        'date': in_fecha,
        'total': float(in_total),
        'reference_quote': refe_quote,
        'seller': seller
    }).execute()

def save_cotization_detail(in_cotizacion, in_fecha, in_empresa_cliente, in_conceptos_seleccionados_df,refe_quote,seller):
    # Prepare a list of dicts for bulk insert
    rows = []
    for _, row in in_conceptos_seleccionados_df.iterrows():
        rows.append({
            'quotation': int(in_cotizacion),
            'client': in_empresa_cliente,
            'date': in_fecha,
            'type': str(row['type']),
            'Amount': float(row['Amount']),
            'description': str(row['description']),
            'reference_quote': refe_quote,
            'seller': seller
        })
    response = supabase.table('quotations_detail').insert(rows).execute()
    return response

def save_concept(Code,account,type,amount,description):
    if not description:
        description = ""
    response = supabase.table('services').insert({
        'Code': Code,
        'Account Name': account,
        'type': type,
        'Amount': amount,
        'description': description
        
    }).execute()
    return response

def save_new_client(in_empresa_cliente,in_contacto_cliente,in_referencia_cliente):
    response = supabase.table('clients').insert({
        'client': in_empresa_cliente,
        'contact': in_contacto_cliente,
        'reference': in_referencia_cliente
    }).execute()
    return response

def retrieve_clients():
    clients_supabase = supabase.table("clients").select("*").execute()
    clients = pd.DataFrame(clients_supabase.data)
    return clients

def retrieve_concepts():
    concepts_supabase = supabase.table("services").select("*").execute()
    concepts = pd.DataFrame(concepts_supabase.data)
    return concepts