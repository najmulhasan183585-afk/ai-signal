import streamlit as st

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal Pro", layout="centered")

# সেশন স্টেট (ডাটা সেভ রাখার জন্য)
if 'results' not in st.session_state:
    st.session_state.results = []

# বাটন ক্লিক ফাংশন
def add_val(v):
    if len(st.session_state.results) < 10:
        st.session_state.results.append(str(v))

# কাস্টম CSS (মোবাইলে পাশাপাশি রাখা এবং কালার দেওয়ার জন্য)
st.markdown("""
    <style>
    /* কন্টেইনার স্টাইল */
    .button-container {
        display: flex;
        flex-wrap: nowrap; /* যাতে ভেঙে নিচে না যায় */
        justify-content: space-between;
        gap: 5px;
        margin-bottom: 10px;
        background-color: white;
        padding: 10px;
        border-radius: 10px;
    }
    
    /* সব বাটনের কমন স্টাইল */
    .stButton > button {
        border-radius: 5px;
        color: white !important;
        font-weight: bold;
        border: none;
        padding: 5px;
        height: 40px;
        width: 100%;
        font-size: 14px;
    }

    /* আলাদা আলাদা কালার কোড */
    div[data-testid="column"]:nth-of-type(1) button { background-color: #2196F3 !important; } /* Big/Small */
    .c5 button { background-color: #FF5722 !important; }
    .c6 button { background-color: #E91E63 !important; }
    .c7 button { background-color: #9C27B0 !important; }
    .c8 button { background-color: #673AB7 !important; }
    .c9 button { background-color: #3F51B5 !important; }
    
    .c0 button { background-color: #4CAF50 !important; }
    .c1 button { background-color: #009688 !important; }
    .c2 button { background-color: #00BCD4 !important; }
    .c3 button { background-color: #FFC107 !important; color: black !important; }
    .c4 button { background-color: #FF9800 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# --- প্রথম সারি (Big + 5 6 7 8 9) ---
col_b, c5, c6, c7, c8, c9 = st.columns([2, 1, 1, 1, 1, 1])
with col_b: 
    if st.button("+Big", key="big"): add_val("B")
with c5:
    st.markdown('<div class="c5">', unsafe_allow_html=True)
    if st.button("5"): add_val(5)
    st.markdown('</div>', unsafe_allow_html=True)
with c6:
    st.markdown('<div class="c6">', unsafe_allow_html=True)
    if st.button("6"): add_val(6)
    st.markdown('</div>', unsafe_allow_html=True)
with c7:
    st.markdown('<div class="c7">', unsafe_allow_html=True)
    if st.button("7"): add_val(7)
    st.markdown('</div>', unsafe_allow_html=True)
with c8:
    st.markdown('<div class="c8">', unsafe_allow_html=True)
    if st.button("8"): add_val(8)
    st.markdown('</div>', unsafe_allow_html=True)
with c9:
    st.markdown('<div class="c9">', unsafe_allow_html=True)
    if st.button("9"): add_val(9)
    st.markdown('</div>', unsafe_allow_html=True)

# --- দ্বিতীয় সারি (Small + 0 1 2 3 4) ---
col_s, c0, c1, c2, c3, c4 = st.columns([2, 1, 1, 1, 1, 1])
with col_s:
    st.markdown('<div class="small-box">', unsafe_allow_html=True) # আলাদা CSS ক্লাস দরকার নেই, col-1 ধরবে
    if st.button("+Small", key="small"): add_val("S")
    st.markdown('</div>', unsafe_allow_html=True)
with c0:
    st.markdown('<div class="c0">', unsafe_allow_html=True)
    if st.button("0"): add_val(0)
    st.markdown('</div>', unsafe_allow_html=True)
with c1:
    st.markdown('<div class="c1">', unsafe_allow_html=True)
    if st.button("1"): add_val(1)
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="c2">', unsafe_allow_html=True)
    if st.button("2"): add_val(2)
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="c3">', unsafe_allow_html=True)
    if st.button("3"): add_val(3)
    st.markdown('</div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="c4">', unsafe_allow_html=True)
    if st.button("4"): add_val(4)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# আউটপুট এবং পিরিয়ড বক্স
res_text = ",".join(st.session_state.results)
st.text_input(f"প্যাটার্ন ({len(st.session_state.results)}/10):", value=res_text)
st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

if st.button("🚀 GET SIGNAL"):
    st.success("সিগন্যাল তৈরি হচ্ছে...")
    
