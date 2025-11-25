# Simpan sebagai app.py

import streamlit as st

st.title("Koordinat Converter")
st.write("Ubah koordinat panjang jadi format pendek **persis seperti contoh kamu** (-1.4477143, 103.5150653)")

coord = st.text_input(
    "Paste koordinat panjang di sini",
    placeholder="-1.4476399912727798, 103.5149938637734"
)

if coord:
    try:
        lat_str, lon_str = [x.strip() for x in coord.replace(" ", "").split(",")]
        lat = float(lat_str)
        lon = float(lon_str)

        # SESUAI POLA CONTOHMU: latitude 7 digit, longitude 8 digit
        short_lat = f"{lat:.7f}"   # -1.4477143
        short_lon = f"{lon:.8f}"   # 103.5150653

        # Hilangkan nol di belakang kalau ada (biar lebih rapi)
        short_lat = short_lat.rstrip("0").rstrip(".") if "." in short_lat else short_lat
        short_lon = short_lon.rstrip("0").rstrip(".") if "." in short_lon else short_lon

        hasil = f"{short_lat}, {short_lon}"

        st.success("✅ Berhasil!")
        st.code(hasil, language=None)
        st.write(f"**Latitude**: {short_lat} ← 7 digit setelah titik  \n**Longitude**: {short_lon} ← 8 digit setelah titik")

        # Tombol copy otomatis
        st.markdown(f"""
        <button onclick="navigator.clipboard.writeText('{hasil}'); alert('Sudah dicopy!')" 
        style="padding:12px 20px; font-size:18px; background:#00C853; color:white; border:none; border-radius:8px; cursor:pointer;">
        📋 Copy Koordinat
        </button>
        """, unsafe_allow_html=True)

        # Langsung buka Google Maps
        st.markdown(f"[Buka lokasi ini di Google Maps](https://www.google.com/maps?q={short_lat},{short_lon})")

    except:
        st.error("Format salah! Harus pakai koma, contoh: -1.44763999, 103.51499386")
