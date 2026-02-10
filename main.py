import streamlit as st
import sqlite3

# ১. ডাটাবেজ সেটআপ (SQLite)
conn = sqlite3.connect('signals.db', check_same_thread=False)
c = conn.cursor()

# টেবিল তৈরি (যদি আগে না থাকে)
c.execute('''CREATE TABLE IF NOT EXISTS pattern_data 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, pattern TEXT, period TEXT)''')
conn.commit()

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal Database", layout="centered")

# সেশন স্টেট (সাময়িকভাবে ইনপুট দেখানোর জন্য)
if 'temp_pattern' not in st.session_state:
    st.session_state.temp_pattern = []

# বাটন ক্লিক ফাংশন
def add_val(v):
    if len(st.session_state.temp_pattern) < 10:
        st.session_state.temp_pattern.append(str(v))

# কাস্টম CSS (মোবাইল গ্রিড এবং কালার)
st.markdown("""
    <style>
    .stButton > button {
        width: 100% !important;
        height: 45px !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
    }
    /* কালার কোডসমূহ */
    div[data-testid="column"]:nth-child(1) button { background-color: #3498db !important; }
    .c5 button { background-color: #ff4d4d !important; } .c6 button { background-color: #d63031 !important; }
    .c7 button { background-color: #8e44ad !important; } .c8 button { background-color: #2c3e50 !important; }
    .c9 button { background-color: #34495e !important; } .c0 button { background-color: #2ecc71 !important; }
    .c1 button { background-color: #27ae60 !important; } .c2 button { background-color: #16a085 !important; }
    .c3 button { background-color: #f1c40f !important; color: black !important; } .c4 button { background-color: #f39c12 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 AI সিগন্যাল ডাটাবেজ")

# --- বাটন ইন্টারফেস (ছবির মতো পাশাপাশি) ---
col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
with col1: st.button("+Big", key="big", on_click=add_val, args=("Big",))
with col2: st.markdown('<div class="c5">', unsafe_allow_html=True); st.button("5", key="n5", on_click=add_val, args=(5,)); st.markdown('</div>', unsafe_allow_html=True)
with col3: st.markdown('<div class="c6">', unsafe_allow_html=True); st.button("6", key="n6", on_click=add_val, args=(6,)); st.markdown('</div>', unsafe_allow_html=True)
with col4: st.markdown('<div class="c7">', unsafe_allow_html=True); st.button("7", key="n7", on_click=add_val, args=(7,)); st.markdown('</div>', unsafe_allow_html=True)
with col5: st.markdown('<div class="c8">', unsafe_allow_html=True); st.button("8", key="n8", on_click=add_val, args=(8,)); st.markdown('</div>', unsafe_allow_html=True)
with col6: st.markdown('<div class="c9">', unsafe_allow_html=True); st.button("9", key="n9", on_click=add_val, args=(9,)); st.markdown('</div>', unsafe_allow_html=True)

sc1, sc2, sc3, sc4, sc5, sc6 = st.columns([2, 1, 1, 1, 1, 1])
with sc1: st.button("+Small", key="small", on_click=add_val, args=("Small",))
with sc2: st.markdown('<div class="c0">', unsafe_allow_html=True); st.button("0", key="n0", on_click=add_val, args=(0,)); st.markdown('</div>', unsafe_allow_html=True)
with sc3: st.markdown('<div class="c1">', unsafe_allow_html=True); st.button("1", key="n1", on_click=add_val, args=(1,)); st.markdown('</div>', unsafe_allow_html=True)
with sc4: st.markdown('<div class="c2">', unsafe_allow_html=True); st.button("2", key="n2", on_click=add_val, args=(2,)); st.markdown('</div>', unsafe_allow_html=True)
with sc5: st.markdown('<div class="c3">', unsafe_allow_html=True); st.button("3", key="n3", on_click=add_val, args=(3,)); st.markdown('</div>', unsafe_allow_html=True)
with sc6: st.markdown('<div class="c4">', unsafe_allow_html=True); st.button("4", key="n4", on_click=add_val, args=(4,)); st.markdown('</div>', unsafe_allow_html=True)

# প্যাটার্ন বক্স
current_p = ",".join(st.session_state.temp_pattern)
st.text_input(f"প্যাটার্ন ({len(st.session_state.temp_pattern)}/10):", value=current_p)

# পিরিয়ড ইনপুট
period_input = st.text_input("পিরিয়ড নম্বর দিন:")

# ২. ডাটাবেজে ডাটা সেভ করা
if st.button("🚀 GET SIGNAL & SAVE"):
    if current_p and period_input:
        c.execute("INSERT INTO pattern_data (pattern, period) VALUES (?, ?)", (current_p, period_input))
        conn.commit()
        st.success("ডাটাবেজে সফলভাবে সেভ হয়েছে!")
        st.session_state.temp_pattern = [] # ইনপুট বক্স খালি করা
    else:
        st.error("প্যাটার্ন এবং পিরিয়ড দুটোই প্রয়োজন!")

# ৩. ডাটাবেজ থেকে ডাটা দেখা (ঐচ্ছিক)
if st.checkbox("আগের জমানো ডাটা দেখুন"):
    data = c.execute("SELECT * FROM pattern_data ORDER BY id DESC LIMIT 5").fetchall()
    for row in data:
        st.write(f"ID: {row[0]} | প্যাটার্ন: {row[1]} | পিরিয়ড: {row[2]}")

if st.button("🗑️ সব মুছুন (Clear All)"):
    st.session_state.temp_pattern = []
    st.rerun()
