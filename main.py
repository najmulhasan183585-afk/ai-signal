import streamlit as st

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal VIP", layout="centered")

# সেশন স্টেট ইনিশিয়ালাইজ করা (যাতে ডাটা হারিয়ে না যায়)
if 'pattern' not in st.session_state:
    st.session_state.pattern = []

# বাটন ক্লিক ফাংশন
def add_to_pattern(value):
    if len(st.session_state.pattern) < 10:
        st.session_state.pattern.append(str(value))

def undo_last():
    if st.session_state.pattern:
        st.session_state.pattern.pop()

# CSS দিয়ে ছবির মতো লুক আনা
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        color: white;
        font-weight: bold;
    }
    /* Big/Small কালার */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button { background-color: #3498db; }
    /* নম্বর বাটনগুলোর কালার সেট করা */
    </style>
    """, unsafe_allow_html=True)

st.title("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# বাটন গ্রিড (সাদা ব্যাকগ্রাউন্ড কন্টেইনারের মতো)
with st.container():
    # সারি ১: Big + (5-9)
    cols1 = st.columns([2, 1, 1, 1, 1, 1])
    if cols1[0].button("+Big"): add_to_pattern("B")
    for i, num in enumerate(range(5, 10)):
        if cols1[i+1].button(str(num)): add_to_pattern(num)

    # সারি ২: Small + (0-4)
    cols2 = st.columns([2, 1, 1, 1, 1, 1])
    if cols2[0].button("+Small"): add_to_pattern("S")
    for i, num in enumerate(range(0, 5)):
        if cols2[i+1].button(str(num)): add_to_pattern(num)

st.write("---")

# UNDO বাটন
if st.button("⬅️ ভুল হয়েছে? শেষ ইনপুট কাটুন (UNDO)"):
    undo_last()

# প্যাটার্ন বক্স (অটোমেটিক আপডেট হবে)
current_pattern = ",".join(st.session_state.pattern)
st.text_input(f"প্যাটার্ন ({len(st.session_state.pattern)}/10): ইনপুট দিন...", value=current_pattern)

# পিরিয়ড ইনপুট
st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# সিগন্যাল বাটন
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if len(st.session_state.pattern) > 0:
        st.info("আপনার প্যাটার্ন বিশ্লেষণ করা হচ্ছে...")
    else:
        st.error("দয়া করে আগে কিছু নম্বর ইনপুট দিন!")
        
