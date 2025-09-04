from supabase import create_client, Client
import pandas as pd
#from tokens import url, key
#supabase_client = create_client(url, key)
import os
url = os.getenv("url_supabase")
key = os.getenv("key_supabase")

supabase: Client = create_client(url, key)

def get_previous_cotizations():
    tabla_supabase = supabase.table("quotations").select("*").execute()
    cotizaciones_previas = pd.DataFrame(tabla_supabase.data)
    return cotizaciones_previas

def get_cotization_number():
    cotizaciones_previas = get_previous_cotizations()
    cotizacion_actual = cotizaciones_previas.iloc[-1]["quotation"]+1
    return cotizacion_actual

def save_cotization(in_cotizacion,in_fecha,in_empresa_cliente,in_total):
    response = supabase.table('quotations').insert({
        'quotation': int(in_cotizacion),
        'client': in_empresa_cliente,
        'date': in_fecha,
        'total': float(in_total)
    }).execute()
    
    return response