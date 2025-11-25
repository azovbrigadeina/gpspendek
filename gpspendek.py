import streamlit as st

st.title("🔄 Koordinat Converter: Panjang → Pendek")
st.write("Ubah koordinat desimal panjang jadi pendek (7-8 digit) seperti yang biasa dipakai di Maps/WhatsApp")

# Input dari user
coord = st.text_input(
    "Masukkan koordinat (pisahkan latitude & longitude dengan koma)",
    placeholder="-1.4476399912727798, 103.5149938637734"
)

if coord:
    try:
        # Bersihkan spasi dan pisah
        lat_str, lon_str = [x.strip() for x in coord.replace(" ", "").split(",")]
        lat = float(lat_str)
        lon = float(lon_str)

        # Opsi tingkat pemendekan
        option = st.radio("Pilih tingkat pemendekan:", 
                         ["Pendek banget (5-6 digit → ±10m)", 
                          "Standar WhatsApp/Maps (7 digit → ±1-3m) ⭐ Rekomendasi",
                          "Super akurat (8 digit → <1m)",
                          "Sama persis seperti contohmu"])

        if option == "Pendek banget (5-6 digit → ±10m)":
            short_lat = f"{lat:.6f}".rstrip("0").rstrip(".")
            short_lon = f"{lon:.6f}".rstrip("0").rstrip(".")
        elif option == "Super akurat (8 digit → <1m)":
            short_lat = f"{lat:.8f}"
            short_lon = f"{lon:.8f}"
        elif option == "Sama persis seperti contohmu":
            short_lat = f"{lat:.7f}"   # -1.4477143 → 7 digit setelah titik
            short_lon = f"{lon:.8f}"   # 103.5150653 → 8 digit setelah titik
        else:  # Rekomendasi 7 digit
            short_lat = f"{lat:.7f}"
            short_lon = f"{lon:.7f}"

        short_coord = f"{short_lat}, {short_lon}"

        st.markdown("### Hasil Koordinat Pendek:")
        st.code(short_coord, language=None)

        # Tombol copy otomatis
        st.markdown(f"""
        <script>
        function copyToClipboard() {{
            navigator.clipboard.writeText("{short_coord}");
            alert("Sudah dicopy ke clipboard!");
        }}
        </script>
        <button onclick="copyToClipboard()" style="padding:10px; font-size:16px; background:#1E88E5; color:white; border:none; border-radius:5px; cursor:pointer;">
        📋 Copy ke Clipboard
        </button>
        """, unsafe_allow_html=True)

        # Link langsung ke Google Maps
        maps_url = f"https://www.google.com/maps?q={lat},{lon}"
        st.markdown(f"[📍 Buka di Google Maps]({maps_url})")

    except:
        st.error("Format salah! Contoh yang benar: -1.44763999, 103.51499386")
