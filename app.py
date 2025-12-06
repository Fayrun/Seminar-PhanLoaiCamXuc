import streamlit as st
from model import SentimentModel
from database import Database

# Basic page config
st.set_page_config(page_title="Phân Loại Cảm Xúc", layout="centered")

# Minimal styling
st.markdown("""
    <style>
        .stTextArea textarea {
            font-size: 16px;
            padding: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎭 Phân Loại Cảm Xúc Tiếng Việt")

# Load models
@st.cache_resource
def load_models():
    return SentimentModel(), Database()

model, db = load_models()

# Input
st.write("**Nhập một câu tiếng Việt:**")
text = st.text_area(
    "Câu tiếng Việt",
    placeholder="Ví dụ: Sản phẩm này rất tuyệt vời!",
    height=100,
    label_visibility="collapsed"
)

if st.button("🔍 Phân Tích", use_container_width=True):
    if not text.strip():
        st.error("Vui lòng nhập một câu!")
    else:
        with st.spinner("Đang phân tích..."):
            result = model.predict(text)
        
        if "error" in result:
            st.error(f"Lỗi: {result['error']}")
        else:
            label = result.get("label", "Unknown")
            score = result.get("score", 0.0)
            db.save_result(text, label, float(score))
            
            st.success("✅ Thành công!")
            col1, col2 = st.columns(2)
            col1.metric("Kết Quả", label)
            col2.metric("Độ Tin Cậy", f"{score*100:.1f}%")

# History
st.divider()
st.write("**Lịch Sử Phân Tích:**")

history = db.get_history(limit=10)
if history:
    for rid, rtext, rsent, rconf, rtime in history:
        emoji = "😊" if "POSITIVE" in rsent.upper() or "5" in rsent else "😞" if "NEGATIVE" in rsent.upper() or "1" in rsent else "😐"
        st.write(f"{emoji} **{rsent}** ({rconf*100:.0f}%) - *{rtext[:60]}...* ({rtime})")
else:
    st.info("Chưa có dữ liệu")



