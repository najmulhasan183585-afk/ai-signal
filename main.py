import streamlit as st
import sqlite3

# ১. ডাটাবেজ এবং সেশন সেটআপ
conn = sqlite3.connect('signals_pro.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS signals (pattern TEXT, period TEXT)')
conn.commit()

if 'pattern_list' not in st.session_state:
    st.session_state.pattern_list = []

# বাটন ক্লিক হ্যান্ডলার (URL এর মাধ্যমে ডাটা নেওয়া যাতে রিফ্রেশে সমস্যা না হয়)
params = st.query_params
if "add" in params:
    val = params["add"]
    if len(st.session_state.pattern_list) < 10:
        st.session_state.pattern_list.append(str(val))
    st.query_params.clear()

st.set_page_config(page_title="AI Signal Fix", layout="centered")

# ২. কাস্টম CSS: যা বাটনকে নিচে নামতে দেবে না
st.markdown("""
    <style>
    .fixed-grid {
        display: flex;
        flex-direction: column;
        gap: 8px;
        background-color: white;
        padding: 12px;
        border-radius: 12px;
        width: 100%;
    }
    .grid-row {
        display: flex;
        justify-content: space-between;
        gap: 4px;
        width: 100%;
    }
    .grid-btn {
        flex: 1;
        height: 40px;
        border-radius: 5px;
        color: white;
        text-decoration: none;
        font-weight: bold;
        font-size: 13px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: none;
    }
    .big-main { flex: 2; background-color: #3498db; }
    .small-main { flex: 2; background-color: #e67e22; }
    .c5 { background-color: #ff4d4d; } .c6 { background-color: #d63031; }
    .c7 { background-color: #8e44ad; } .c8 { background-color: #2c3e50; }
    .c9 { background-color: #34495e; } .c0 { background-color: #2ecc71; }
    .c1 { background-color: #27ae60; } .c2 { background-color: #16a085; }
    .c3 { background-color: #f1c40f; color: black; } .c4 { background-color: #f39c12; }
    </style>
    """, unsafe_allow_html=True)

st.subheader("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# ৩. HTML গ্রিড (এটিই বাটনগুলোকে পাশাপাশি রাখবে)
grid_html = f"""
<div class="fixed-grid">
    <div class="grid-row">
        <a href="/?add=Big" target="_self" class="grid-btn big-main">+Big</a>
        <a href="/?add=5" target="_self" class="grid-btn c5">5</a>
        <a href="/?add=6" target="_self" class="grid-btn c6">6</a>
        <a href="/?add=7" target="_self" class="grid-btn c7">7</a>
        <a href="/?add=8" target="_self" class="grid-btn c8">8</a>
        <a href="/?add=9" target="_self" class="grid-btn c9">9</a>
    </div>
    <div class="grid-row">
        <a href="/?add=Small" target="_self" class="grid-btn small-main">+Small</a>
        <a href="/?add=0" target="_self" class="grid-btn c0">0</a>
        <a href="/?add=1" target="_self" class="grid-btn c1">1</a>
        <a href="/?add=2" target="_self" class="grid-btn c2">2</a>
        <a href="/?add=3" target="_self" class="grid-btn c3">3</a>
        <a href="/?add=4" target="_self" class="grid-btn c4">4</a>
    </div>
</div>
"""
st.markdown(grid_html, unsafe_allow_html=True)

# ৪. ইনপুট ও আউটপুট এরিয়া
st.write("")
current_p = ",".join(st.session_state.pattern_list)
st.text_input(f"প্যাটার্ন ({len(st.session_state.pattern_list)}/10):", value=current_p)
period_val = st.text_input("পিরিয়ড নম্বর দিন:")

if st.button("🚀 GET SIGNAL & SAVE"):
    if current_p and period_val:
        c.execute("INSERT INTO signals VALUES (?, ?)", (current_p, period_val))
        conn.commit()
        st.success("ডাটাবেজে সেভ হয়েছে!")
        st.session_state.pattern_list = []
        st.rerun()
    else:
        st.error("ইনপুট খালি রাখা যাবে না!")

# ৫. কন্ট্রোল বাটন
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ UNDO"):
        if st.session_state.pattern_list:
            st.session_state.pattern_list.pop()
            st.rerun()
with col2:
    if st.button("🗑️ CLEAR ALL"):
        st.session_state.pattern_list = []
        st.rerun()

if st.checkbox("ডাটাবেজ রেকর্ড দেখুন"):
    rows = c.execute("SELECT * FROM signals ORDER BY rowid DESC LIMIT 5").fetchall()
    st.table(rows)
  
