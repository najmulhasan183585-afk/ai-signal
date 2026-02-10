import streamlit as st
import sqlite3

# ১. ডাটাবেজ সেটআপ
conn = sqlite3.connect('ai_final_db.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS history (pattern TEXT, period TEXT)')
conn.commit()

# ২. সেশন স্টেট (ডাটা জমা রাখার জন্য)
if 'pattern_list' not in st.session_state:
    st.session_state.pattern_list = []

# বাটন ক্লিকের লজিক (URL প্যারামিটার ব্যবহার করে যাতে রিফ্রেশে সমস্যা না হয়)
params = st.query_params
if "val" in params:
    clicked_val = params["val"]
    if len(st.session_state.pattern_list) < 10:
        st.session_state.pattern_list.append(str(clicked_val))
    st.query_params.clear()

st.set_page_config(page_title="AI Signal Mobile Fix", layout="centered")

# ৩. CSS গ্রিড: এটিই বাটনকে এক লাইনে আটকে রাখবে
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr; /* প্রথমটি বড়, বাকি ৫টি সমান */
        gap: 5px;
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        width: 100%;
        box-sizing: border-box;
    }
    .grid-btn {
        height: 40px;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        font-size: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        border: none;
    }
    /* কালার কোডসমূহ */
    .big { background-color: #3498db; }
    .small { background-color: #e67e22; }
    .c5 { background-color: #ff4d4d; } .c6 { background-color: #d63031; }
    .c7 { background-color: #8e44ad; } .c8 { background-color: #2c3e50; }
    .c9 { background-color: #34495e; } .c0 { background-color: #2ecc71; }
    .c1 { background-color: #27ae60; } .c2 { background-color: #16a085; }
    .c3 { background-color: #f1c40f; color: black; } .c4 { background-color: #f39c12; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h3>", unsafe_allow_html=True)

# ৪. বাটন গ্রিড (HTML এর মাধ্যমে)
grid_html = f"""
<div class="grid-container">
    <a href="/?val=Big" target="_self" class="grid-btn big">+Big</a>
    <a href="/?val=5" target="_self" class="grid-btn c5">5</a>
    <a href="/?val=6" target="_self" class="grid-btn c6">6</a>
    <a href="/?val=7" target="_self" class="grid-btn c7">7</a>
    <a href="/?val=8" target="_self" class="grid-btn c8">8</a>
    <a href="/?val=9" target="_self" class="grid-btn c9">9</a>
</div>
<div class="grid-container">
    <a href="/?val=Small" target="_self" class="grid-btn small">+Small</a>
    <a href="/?val=0" target="_self" class="grid-btn c0">0</a>
    <a href="/?val=1" target="_self" class="grid-btn c1">1</a>
    <a href="/?val=2" target="_self" class="grid-btn c2">2</a>
    <a href="/?val=3" target="_self" class="grid-btn c3">3</a>
    <a href="/?val=4" target="_self" class="grid-btn c4">4</a>
</div>
"""
st.markdown(grid_html, unsafe_allow_html=True)

# ৫. ইনপুট ও সেভ এরিয়া
st.write("")
current_p = ",".join(st.session_state.pattern_list)
st.text_input(f"প্যাটার্ন ({len(st.session_state.pattern_list)}/10):", value=current_p)

period = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

if st.button("🚀 GET SIGNAL & SAVE TO DB"):
    if current_p and period:
        c.execute("INSERT INTO history (pattern, period) VALUES (?, ?)", (current_p, period))
        conn.commit()
        st.success("সেভ হয়েছে!")
        st.session_state.pattern_list = []
        st.rerun()
    else:
        st.error("ইনপুট দিন!")

# কন্ট্রোল বাটন
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
        
