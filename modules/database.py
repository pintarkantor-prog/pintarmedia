import streamlit as st
from supabase import create_client, Client

# Ini 'kabel' utama kita
url: str = st.secrets["supabase"]["url"]
key: str = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

def validasi_user(username, password):
    try:
        # Kita cari di tabel 'Staff' yang Nama dan Password-nya cocok
        res = supabase.table("Staff").select("*").eq("Nama", username.upper()).eq("Password", password).execute()
        
        if len(res.data) > 0:
            return res.data[0] # Kembalikan data user (Nama, Level, dll)
        return None
    except Exception as e:
        st.error(f"Error Database: {e}")
        return None
