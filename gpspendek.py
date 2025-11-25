# app.py — versi FINAL yang bener-bener sesuai keinginanmu

import streamlit as st

st.title("Koordinat Converter (7 + 7 Digit)")
st.caption("Hasil pasti 7 digit setelah titik desimal untuk latitude & longitude")

coord = st.text_input(
    "Masukkan koordinat panjang",
    placeholder="-1.4476399912727798, 103.5149938637734"
)

if coord:
    try:
        lat_str, lon_str = [x.strip() for x in coord.replace(" ", "").split(",")]
        lat = float(lat_str)
        lon = float(lon_str)

        # DIPAKSA 7 digit setelah titik, nol belakang TIDAK dihapus
        short_lat = f"{lat:.7f}"    # contoh: -1.4476400
        short_lon = f"{lon:.7f}"    # contoh: 103.5149939

        hasil = f"{short_lat}, {short_lon}"

        st.success("Sukses!")
        st.code(hasil, language=None)
        st.write(f"**Latitude**  → {short_lat} ← pasti 7 digit  \n**Longitude** → {short_lon} ← pasti 7 digit")

        # Tombol copy
        st.markdown(f"""
        <button onclick="navigator.clipboard.writeText('{hasil}'); alert('Sudah tercopy!')" 
        style="padding:15px 30px; font-size:18px; background:#0066ff; color:white; border:none; border-radius:10px; cursor:pointer; margin-top:15px;">
        📋 Copy Koordinat
        </button>
        """, unsafe_allow_html=True)

        # Link Maps
        st.markdown(f"[Buka di Google Maps](https://www.google.com/maps?q={short_lat},{short_lon})")

    except:
        st.error("Format salah! Contoh: -1.44763999, 103.51499386")
