import streamlit as st

# মোবাইল স্ক্রিন অপ্টিমাইজেশন
st.set_page_config(page_title="AI Signal Mobile", layout="centered")

# সেশন স্টেট ডাটা স্টোর করার জন্য
if 'results' not in st.session_state:
    st.session_state.results = []

def add_val(v):
    if len(st.session_state.results) < 10:
        st.session_state.results.append(str(v))

# কাস্টম CSS যা বাটনগুলোকে মোবাইলেও পাশাপাশি রাখবে
st.markdown("""
    <style>
    /* মেইন কন্টেইনার */
    .mobile-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr; /* প্রথম কলাম বড়, বাকিরা সমান */
        gap: 4px;
        margin-bottom: 8px;
        background-color: #ffffff;
        padding: 8px;
        border-radius: 10px;
    }
    
    /* সব বাটনের সাধারণ স্টাইল */
    .stButton > button {
        width: 100% !important;
        height: 45px !important;
        padding: 0px !important;
        border-radius: 6px !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 14px !important;
        border: none !important;
    }

    /* আলাদা আলাদা বাটন কালার */
    div[data-testid="column"]:nth-child(1) button { background-color: #3498db !important; } /* Big/Small */
    
    /* স্পেসিফিক নম্বর বাটন কালার (ছবির মতো) */
    .c5 button { background-color: #ff4d4d !important; }
    .c6 button { background-color: #d63031 !important; }
    .c7 button { background-color: #8e44ad !important; }
    .c8 button { background-color: #2c3e50 !important; }
    .c9 button { background-color: #34495e !important; }
    
    .c0 button { background-color: #2ecc71 !important; }
    .c1 button { background-color: #27ae60 !important; }
    .c2 button { background-color: #16a085 !important; }
    .c3 button { background-color: #f1c40f !important; color: black !important; }
    .c4 button { background-color: #f39c12 !important; }

    /* মোবাইলের সাদা ইনপুট বক্সের মতো লুক */
    .input-area {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# --- প্রথম সারি (Big + 5, 6, 7, 8, 9) ---
col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
with col1: st.button("+Big", key="big", on_click=add_val, args=("B",))
with col2: st.markdown('<div class="c5">', unsafe_allow_html=True); st.button("5", key="n5", on_click=add_val, args=(5,)); st.markdown('</div>', unsafe_allow_html=True)
with col3: st.markdown('<div class="c6">', unsafe_allow_html=True); st.button("6", key="n6", on_click=add_val, args=(6,)); st.markdown('</div>', unsafe_allow_html=True)
with col4: st.markdown('<div class="c7">', unsafe_allow_html=True); st.button("7", key="n7", on_click=add_val, args=(7,)); st.markdown('</div>', unsafe_allow_html=True)
with col5: st.markdown('<div class="c8">', unsafe_allow_html=True); st.button("8", key="n8", on_click=add_val, args=(8,)); st.markdown('</div>', unsafe_allow_html=True)
with col6: st.markdown('<div class="c9">', unsafe_allow_html=True); st.button("9", key="n9", on_click=add_val, args=(9,)); st.markdown('</div>', unsafe_allow_html=True)

# --- দ্বিতীয় সারি (Small + 0, 1, 2, 3, 4) ---
sc1, sc2, sc3, sc4, sc5, sc6 = st.columns([2, 1, 1, 1, 1, 1])
with sc1: st.button("+Small", key="small", on_click=add_val, args=("S",))
with sc2: st.markdown('<div class="c0">', unsafe_allow_html=True); st.button("0", key="n0", on_click=add_val, args=(0,)); st.markdown('</div>', unsafe_allow_html=True)
with sc3: st.markdown('<div class="c1">', unsafe_allow_html=True); st.button("1", key="n1", on_click=add_val, args=(1,)); st.markdown('</div>', unsafe_allow_html=True)
with sc4: st.markdown('<div class="c2">', unsafe_allow_html=True); st.button("2", key="n2", on_click=add_val, args=(2,)); st.markdown('</div>', unsafe_allow_html=True)
with sc5: st.markdown('<div class="c3">', unsafe_allow_html=True); st.button("3", key="n3", on_click=add_val, args=(3,)); st.markdown('</div>', unsafe_allow_html=True)
with sc6: st.markdown('<div class="c4">', unsafe_allow_html=True); st.button("4", key="n4", on_click=add_val, args=(4,)); st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# আউটপুট বক্স
res_display = ",".join(st.session_state.results)
st.text_input(f"প্যাটার্ন ({len(st.session_state.results)}/10): ইনপুট দিন...", value=res_display)

# পিরিয়ড ইনপুট
st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# সিগন্যাল বাটন
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    st.info("আপনার ডাটা প্রসেস করা হচ্ছে...")
    
