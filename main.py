import streamlit as st
import sqlite3

# ১. ডাটাবেজ সেটআপ
conn = sqlite3.connect('ai_final_db.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS results (pattern TEXT, period TEXT)')
conn.commit()

# ২. সেশন স্টেট হ্যান্ডলিং
if 'final_pattern' not in st.session_state:
    st.session_state.final_pattern = []

# বাটন ক্লিক ফাংশন
def handle_click(val):
    if len(st.session_state.final_pattern) < 10:
        st.session_state.final_pattern.append(str(val))

st.set_page_config(page_title="AI Signal Final", layout="centered")

# ৩. কাস্টম CSS (মোবাইলে বাটন পাশাপাশি রাখার জন্য)
st.markdown("""
    <style>
    /* কলামগুলোকে মোবাইলেও পাশাপাশি রাখা */
    [data-testid="column"] {
        width: calc(16.6% - 1rem) !important;
        flex: 1 1 calc(16.6% - 1rem) !important;
        min-width: calc(16.6% - 1rem) !important;
    }
    /* বড় বাটন দুটির জন্য বিশেষ প্রশস্ততা */
    div[data-testid="column"]:nth-child(1), div[data-testid="column"]:nth-child(7) {
        width: calc(33% - 1rem) !important;
        flex: 2 1 calc(33% - 1rem) !important;
        min-width: calc(33% - 1rem) !important;
    }
    .stButton button {
        width: 100%;
        height: 45px;
        padding: 0px;
        font-weight: bold;
        color: white;
        border-radius: 8px;
        border: none;
    }
    /* কালার কোড */
    .big-btn button { background-color: #3498db !important; }
    .small-btn button { background-color: #e67e22 !important; }
    .c5 button { background-color: #ff4d4d !important; } .c6 button { background-color: #d63031 !important; }
    .c7 button { background-color: #8e44ad !important; } .c8 button { background-color: #2c3e50 !important; }
    .c9 button { background-color: #34495e !important; } .c0 button { background-color: #2ecc71 !important; }
    .c1 button { background-color: #27ae60 !important; } .c2 button { background-color: #16a085 !important; }
    .c3 button { background-color: #f1c40f !important; color: black !important; } .c4 button { background-color: #f39c12 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h3>", unsafe_allow_html=True)

# ৪. বাটন ইন্টারফেস (একদম আপনার ছবির মতো)
# প্রথম সারি
r1_c1, r1_c2, r1_c3, r1_c4, r1_c5, r1_c6 = st.columns([2, 1, 1, 1, 1, 1])
with r1_c1: st.markdown('<div class="big-btn">', unsafe_allow_html=True); st.button("+Big", on_click=handle_click, args=("Big",)); st.markdown('</div>', unsafe_allow_html=True)
with r1_c2: st.markdown('<div class="c5">', unsafe_allow_html=True); st.button("5", on_click=handle_click, args=(5,)); st.markdown('</div>', unsafe_allow_html=True)
with r1_c3: st.markdown('<div class="c6">', unsafe_allow_html=True); st.button("6", on_click=handle_click, args=(6,)); st.markdown('</div>', unsafe_allow_html=True)
with r1_c4: st.markdown('<div class="c7">', unsafe_allow_html=True); st.button("7", on_click=handle_click, args=(7,)); st.markdown('</div>', unsafe_allow_html=True)
with r1_c5: st.markdown('<div class="c8">', unsafe_allow_html=True); st.button("8", on_click=handle_click, args=(8,)); st.markdown('</div>', unsafe_allow_html=True)
with r1_c6: st.markdown('<div class="c9">', unsafe_allow_html=True); st.button("9", on_click=handle_click, args=(9,)); st.markdown('</div>', unsafe_allow_html=True)

# দ্বিতীয় সারি
r2_c1, r2_c2, r2_c3, r2_c4, r2_c5, r2_c6 = st.columns([2, 1, 1, 1, 1, 1])
with r2_c1: st.markdown('<div class="small-btn">', unsafe_allow_html=True); st.button("+Small", on_click=handle_click, args=("Small",)); st.markdown('</div>', unsafe_allow_html=True)
with r2_c2: st.markdown('<div class="c0">', unsafe_allow_html=True); st.button("0", on_click=handle_click, args=(0,)); st.markdown('</div>', unsafe_allow_html=True)
with r2_c3: st.markdown('<div class="c1">', unsafe_allow_html=True); st.button("1", on_click=handle_click, args=(1,)); st.markdown('</div>', unsafe_allow_html=True)
with r2_c4: st.markdown('<div class="c2">', unsafe_allow_html=True); st.button("2", on_click=handle_click, args=(2,)); st.markdown('</div>', unsafe_allow_html=True)
with r2_c5: st.markdown('<div class="c3">', unsafe_allow_html=True); st.button("3", on_click=handle_click, args=(3,)); st.markdown('</div>', unsafe_allow_html=True)
with r2_c6: st.markdown('<div class="c4">', unsafe_allow_html=True); st.button("4", on_click=handle_click, args=(4,)); st.markdown('</div>', unsafe_allow_html=True)

# ৫. ইনপুট এরিয়া
st.write("")
display_pattern = ",".join(st.session_state.final_pattern)
st.text_input(f"প্যাটার্ন ({len(st.session_state.final_pattern)}/10):", value=display_pattern, disabled=True)

period = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# সেভ এবং সিগন্যাল
if st.button("🚀 GET SIGNAL & SAVE"):
    if display_pattern and period:
        c.execute("INSERT INTO results VALUES (?, ?)", (display_pattern, period))
        conn.commit()
        st.success("সেভ হয়েছে!")
        st.session_state.final_pattern = [] # রিসেট
        st.rerun()
    else:
        st.error("ইনপুট দিন!")

# কন্ট্রোল বাটন
col_u, col_c = st.columns(2)
with col_u:
    if st.button("⬅️ UNDO"):
        if st.session_state.final_pattern:
            st.session_state.final_pattern.pop()
            st.rerun()
with col_c:
    if st.button("🗑️ CLEAR ALL"):
        st.session_state.final_pattern = []
        st.rerun()
        
