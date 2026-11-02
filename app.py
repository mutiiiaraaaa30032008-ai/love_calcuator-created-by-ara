import streamlit as st
import hashlib
import time

st.set_page_config(page_title="Love Calculator 💗", page_icon="💘", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f7 0%, #f3eaff 100%);
}
.main-title {
    text-align: center;
    padding: 22px 12px;
    border-radius: 24px;
    background: linear-gradient(135deg, #ff6fae, #a78bfa);
    color: white;
    box-shadow: 0 8px 22px rgba(180, 100, 160, .18);
}
.result-card {
    text-align: center;
    background: rgba(255,255,255,.85);
    border: 1px solid #f6cde2;
    padding: 24px;
    border-radius: 22px;
    margin-top: 18px;
}
.heart {
    font-size: 42px;
    animation: pulse 1s infinite;
}
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.15); }
}
</style>
<div class="main-title">
<h1>💗 LOVE CALCULATOR 💗</h1>
<h3>Seberapa cocok kalian berdua?</h3>
<p>Masukkan dua nama dan lihat hasilnya ✨</p>
</div>
""", unsafe_allow_html=True)

st.write("")
col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("Nama kamu", placeholder="Contoh: Ara")
with col2:
    name2 = st.text_input("Nama pasangan", placeholder="Contoh: Isan")

if st.button("💘 HITUNG KECOCOKAN", use_container_width=True):
    a = name1.strip()
    b = name2.strip()

    if not a or not b:
        st.warning("Isi kedua nama dulu ya! 😊")
    else:
        # Angka dibuat konsisten untuk pasangan nama yang sama.
        pair = "|".join(sorted([a.casefold(), b.casefold()]))
        digest = hashlib.sha256(pair.encode("utf-8")).hexdigest()
        percentage = int(digest[:8], 16) % 101

        with st.spinner("💞 Menghitung kecocokan..."):
            time.sleep(1.2)

        if percentage >= 90:
            comment, emoji = "WADUHH, cocok banget! 💍", "💘"
        elif percentage >= 75:
            comment, emoji = "Chemistry-nya kuat nih! 🥰", "💕"
        elif percentage >= 50:
            comment, emoji = "Lumayan cocok, siapa tahu makin dekat! ✨", "💓"
        elif percentage >= 25:
            comment, emoji = "Masih misteri, coba kenalan lebih jauh! 😆", "💌"
        else:
            comment, emoji = "Plot twist! Cinta memang penuh kejutan 😂", "🤣"

        st.markdown(f"""
        <div class="result-card">
            <div class="heart">{emoji}</div>
            <h2>{a} ❤️ {b}</h2>
            <h1 style="font-size:64px;color:#e84393;margin:8px 0;">{percentage}%</h1>
            <h3>{comment}</h3>
            <p>✨ Love Calculator ✨</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(percentage / 100)
        st.caption("Persentase ini hanya untuk hiburan, bukan ukuran kecocokan hubungan yang sebenarnya.")

        share_text = f"💗 LOVE CALCULATOR 💗\\n{a} + {b} = {percentage}%\\n{comment}\\nCuma buat seru-seruan ya! ✨"
        st.text_area("Kartu hasil (bisa disalin)", value=share_text, height=120)

st.markdown("<p style='text-align:center;color:#b56b98;'>Made with 💗</p>", unsafe_allow_html=True)
