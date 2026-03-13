import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Konfigurasi Otak AI (Aqualens Engine)
# Masukkan API Key kamu di sini nanti
genai.configure(api_key="AIzaSyCzyoDqRUHt8nQ61ytWSDMeLVrC0LKBrds")
model = genai.GenerativeModel('models/gemini-1.5-flash')

st.title("💧 Aqualens Tester")
st.write("Ambil foto air kamu untuk cek kelayakan visual.")

# 2. Fitur Kamera
img_file = st.camera_input("Jepret Gelas Air")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="Foto Berhasil Diambil", use_column_width=True)
    
    with st.spinner('Aqualens sedang menganalisis...'):
        # 3. Instruksi Khusus (Prompt) agar AI jadi Spesialis Air
        prompt = """
        Kamu adalah sistem AI Aqualens. Analisis foto air ini:
        1. Berikan Skor Kualitas Visual (0-100).
        2. Deteksi warna dan kekeruhan.
        3. Berikan status: [AMAN / WASPADA / BAHAYA].
        4. Berikan saran singkat (misal: perlu difilter atau direbus).
        Gunakan bahasa Indonesia yang santai tapi jelas.
        """
        
        response = model.generate_content([prompt, img])
        
        # 4. Tampilkan Hasil
        st.subheader("Hasil Analisis Aqualens:")
        st.success(response.text)

st.divider()
st.caption("Aqualens v1.0 - Low Budget Tester")
