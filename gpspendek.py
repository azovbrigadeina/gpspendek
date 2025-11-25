# Simpan sebagai app.py

import streamlit as st

st.title("Koordinat Converter")
st.caption("Hasil: latitude 7 digit ▪ longitude 7 digit (persis seperti yang kamu mau)")

coord = st.text_input(
    "Paste koordinat panjang di sini",
    placeholder="-1.4476399912727798, 103.5149938637734"
)

if coord:
    try:
        lat_str, lon_str = [x.strip() for x in coord.replace(" ", "").split(",")]
        lat = float(lat_str)
        lon = float(lon_str)

        # DIPAKSA 7 + 7 seperti yang kamu inginkan
        short_lat = f"{lat:.7f}"
        short_lon = f"{lon:.7f}"   # ← longitude juga 7 digit

        # Bersihkan nol di belakang biar lebih rapi (opsional)
        short_lat = short_lat.rstrip("0").rstrip(".") if "." in short_lat else short_lat
        short_lon = short_lon.rstrip("0").rstrip(".") if "." in short_lon else short_lon

        hasil = f"{short_lat}, {short_lon}"

        st.success("Berhasil dikonversi!")
        st.code(hasil, language=None)
        st.write(f"**Latitude**  : {short_lat} (7 digit)  \n**Longitude** : {short_lon} (7 digit)")

        # Tombol copy
        st.markdown(f"""
        <button onclick="navigator.clipboard.writeText('{hasil}'); alert('Tercopy!')" 
        style="padding:12px 24px; font-size:18px; background:#4CAF50; color:white; border:none; border-radius:8px; cursor:pointer; margin-top:10px;">
        📋 Copy Koordinat
        </button>
        """, unsafe_allow_html=True)

        # Link Google Maps (tetap pakai koordinat asli biar akurat)
        st.markdown(f"[Buka di Google Maps](https://www.google.com/maps?q={lat},{lon})")

    except Exception as e:
        st.error("Format salah! Contoh benar: -6.175110, 106.8650395")
