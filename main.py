import streamlit as st

# ১. পেজ এবং সবুজ ব্যাকগ্রাউন্ড সেটআপ
st.set_page_config(page_title="AI Signal Pro Max", layout="centered")

# CSS দিয়ে ব্যাকগ্রাউন্ড সবুজ করা
st.markdown("""
    <style>
    .stApp {
        background-color: #9ACD32;
    }
    </style>
    """, unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Security Login")
    pw = st.text_input("পাসওয়ার্ড দিন:", type="password")
    if st.button("Login"):
        if pw == "123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("ভুল পাসওয়ার্ড!")
else:
    # ২. ২৫০টি ডাটা
    if 'history' not in st.session_state:
        st.session_state.history = ['S', 'S', 'S', 'S', 'B', 'S', 'B', 'S', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'B', 'B', 'S', 'B', 'S', 'B', 'S', 'S', 'B', 'S', 'B', 'S', 'B', 'S', 'S', 'S', 'S', 'B', 'B', 'S', 'B', 'B', 'S', 'B', 'S', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'B', 'S', 'S', 'B', 'B', 'B', 'S', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'B', 'S', 'S', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'B', 'S', 'S', 'S', 'S', 'B', 'B', 'S', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'B', 'B', 'S', 'B', 'B', 'B', 'S', 'S', 'B', 'S', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'S', 'S', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'S', 'S', 'B', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'B', 'B', 'S', 'S', 'B', 'S', 'B', 'S', 'S', 'B', 'S', 'S', 'B', 'B', 'S', 'S', 'S', 'B', 'S', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'B', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'B', 'B', 'S', 'S', 'B', 'B', 'B', 'B']
        st.session_state.wins = 0
        st.session_state.losses = 0

    st.title("📊 AI Number & Signal Predictor")

    # ৩. সাইডবার (টেলিগ্রাম ও রেফার লিঙ্ক)
    with st.sidebar:
        st.header("📢 আমাদের সাথে থাকুন")
        # নিচের লিঙ্কে আপনার নিজের লিঙ্ক বসিয়ে দিন
        st.link_button("✈️ Join Telegram", "https://t.me/your_telegram")
        st.link_button("🔗 Create Account", "https://your_link.com")
        st.write("---")
        if st.button("🧹 সব রিসেট করুন"):
            st.session_state.history = []
            st.rerun()

    # ৪. নম্বর ইনপুট লজিক (০-৪ Small, ৫-৯ Big)
    st.subheader("🔢 নম্বর দিন (০-৯):")
    input_num = st.number_input("পিরিয়ডের শেষ সংখ্যাটি দিন", min_value=0, max_value=9, step=1)
    
    if input_num >= 0:
        if input_num in [0, 1, 2, 3, 4]:
            p1, p2 = "SMALL 🔵", "BIG 🔴"
        else:
            p1, p2 = "BIG 🔴", "SMALL 🔵"
        
        st.success(f"Primary: {p1}")
        st.warning(f"Secondary: {p2}")

    # ৫. হিস্ট্রি
    st.write("---")
    st.subheader("🕒 সাম্প্রতিক হিস্ট্রি:")
    recent = st.session_state.history[-10:]
    st.code(" ➡️ ".join(recent).replace('B', '🔴 BIG').replace('S', '🔵 SMALL'))
                                    
