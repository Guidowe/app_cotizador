from supabase import create_client, Client
import pandas as pd

# Initialize Supabase client
url: str = "https://qwmvlhjgqrrxecefcldm.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF3bXZsaGpncXJyeGVjZWZjbGRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQzOTUxNTIsImV4cCI6MjA2OTk3MTE1Mn0.2US4PiD-IauMJp7JMCEnvaw3Q5gb--D6dpYIHX4Qpug"
supabase: Client = create_client(url, key)

def get_previous_cotizations():
    tabla_supabase = supabase.table("cotizaciones").select("*").execute()
    cotizaciones_previas = pd.DataFrame(tabla_supabase.data)
    return cotizaciones_previas

def get_cotization_number():
    cotizaciones_previas = get_previous_cotizations()
    cotizacion_actual = cotizaciones_previas.iloc[-1]["cotizacion"]+1
    return cotizacion_actual

def save_cotization(in_cotizacion,in_fecha,in_empresa_cliente,in_total):
    response = supabase.table('cotizaciones').insert({
        'cotizacion': int(in_cotizacion),
        'empresa_cliente': in_empresa_cliente,
        'total': float(in_total)
    }).execute()
    
    return response