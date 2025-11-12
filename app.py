import streamlit as st
from better_profanity import profanity

# Kutubxonani sozlash
profanity.load_censor_words()

# Sarlavha
st.title("🧠 Ingliz tilidagi nomaqbul so‘zlarni aniqlovchi dastur")

# Qo‘shimcha tavsif (dizayn uchun)
st.markdown("### ✍️ Inglizcha matnda **vulgar yoki nomaqbul so‘zlarni** aniqlovchi model")
st.info("Matnni kiriting va natijani real vaqtda ko‘rishingiz mumkin.")

# Foydalanuvchidan matn kiritish
text = st.text_area("Matn kiriting:", placeholder="Bu yerga inglizcha gap yozing...")

# Tugma bosilganda tahlil qilish
if st.button("Tahlil qilish"):
    if text.strip():
        if profanity.contains_profanity(text):
            st.error("⚠️ Matnda nomaqbul so‘zlar bor!")
            st.write("**Tozalangan versiya:**")
            st.code(profanity.censor(text))
        else:
            st.success("✅ Matn toza, nomaqbul so‘zlar aniqlanmadi.")
    else:
        st.warning("Iltimos, tahlil qilish uchun matn kiriting.")
