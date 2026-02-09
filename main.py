import streamlit as st
import time
import random
import hashlib
import sqlite3
import pandas as pd

# --- আপনার অরিজিনাল সেটিংস ---
LOGO_URL = "https://i.ibb.co/vzYm8Ym/najmul-logo.png"
TELEGRAM_LINK = "https://t.me/your_telegram_link"

MASTER_TRENDS = {
    "big_chains": [7, 9, 5, 8, 6], 
    "small_chains": [0, 2, 3, 4, 1],
    "violet_trigger": [0, 5],
    "reversal_rate": 0.82 
}

# --- ডাটাবেস কানেকশন ---
conn = sqlite3.connect('vip_history.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS history 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, period TEXT, prediction TEXT, win_chance REAL, result TEXT)''')
conn.commit()

# --- প্রেডিকশন লজিক (আপনার অরিজিনাল) ---
def advanced_predict(inputs, period):
    if not inputs or len(inputs) != 10: return None, 0
    clean_inputs = [i.split('-')[0] if '-' in i else i for i in inputs]
    seed_str = str(period) + "".join(clean_inputs) + str(time.time())
    random.seed(int(hashlib.sha256(seed_str.encode()).hexdigest(), 16))
    win_chance = round(random.uniform(94.5, 99.8), 1)
    freq_B = clean_inputs.count("B"); freq_S = clean_inputs.count("S")
    if clean_inputs[-3:] == ["B", "B", "B"]:
        prediction = "SMALL" if random.random() < MASTER_TRENDS["reversal_rate"] else "BIG"
    elif clean_inputs[-3:] == ["S", "S", "S"]:
        prediction = "BIG" if random.random() < MASTER_TRENDS["reversal_rate"] else "SMALL"
    elif freq_B > freq_S: prediction = "BIG" if random.random() > 0.10 else "SMALL"
    elif freq_S > freq_B: prediction = "SMALL" if random.random() > 0.10 else "BIG"
    else: prediction = random.choice(["BIG", "SMALL"])
    return prediction, win_chance

# --- Streamlit Config ---
st.set_page_config(page_title="Najmul Master AI V10 Pro", layout="centered")

# --- সেশন স্টেট ---
if "temp_input" not in st.session_state: st.session_state.temp_input = []
if "history" not in st.session_state: st.session_state.history = []
if "show_res" not in st.session_state: st.session_state.show_res = False

# --- আপনার দেওয়া HTML স্টাইল (CSS) ---
st.markdown(f"""
<style>
    header, footer, [data-testid="stToolbar"] {{ display: none !important; }}
    .stApp {{ background-color: #0b0f19; color: white; }}
    
    /* কন্টেইনার স্টাইল */
    .main-container {{ max-width: 400px; margin: auto; background: #111; padding: 20px; border-radius: 15px; border: 1px solid #333; text-align: center; }}
    
    /* বাটন স্টাইল */
    .stButton>button {{ width: 100%; border-radius: 8px; font-weight: bold; border: none; }}
    
    /* BIG বাটন */
    .big-btn button {{ background-color: #00e676 !important; color: black !important; height: 50px; }}
    /* SMALL বাটন */
    .small-btn button {{ background-color: #ff1744 !important; color: white !important; height: 50px; }}
    /* সংখ্যা বাটন */
    .num-btn button {{ background-color: #222 !important; color: white !important; border: 1px solid #444 !important; height: 40px; }}
    /* UNDO বাটন */
    .undo-btn button {{ background-color: #2c3e50 !important; color: white !important; }}
    /* SIGNAL বাটন */
    .signal-btn button {{ background: linear-gradient(to right, #1e3c72, #2a5298) !important; color: white !important; height: 50px; font-size: 16px; }}

    /* প্যাটার্ন বক্স */
    .pattern-box {{ background: #1a1a2e; border: 1px solid #00d2ff; padding: 15px; border-radius: 8px; color: #00d2ff; font-weight: bold; text-align: center; margin: 15px 0; }}
</style>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.markdown("## 🔥 NAJMUL MASTER AI V10 PRO")
st.markdown("<p style='color: #bbb;'>আগের ১০টি রেজাল্ট ইনপুট দিন:</p>", unsafe_allow_html=True)

# BIG Section
st.markdown('<div class="big-btn">', unsafe_allow_html=True)
if st.button("+ BIG (B)"):
    if len(st.session_state.temp_input) < 10: 
        st.session_state.temp_input.append("B")
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

cols_b = st.columns(5)
for i, n in enumerate([5,6,7,8,9]):
    with cols_b[i]:
        st.markdown('<div class="num-btn">', unsafe_allow_html=True)
        if st.button(str(n), key=f"b{n}"):
            if len(st.session_state.temp_input) < 10:
                st.session_state.temp_input.append(f"B-{n}")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# SMALL Section
st.markdown('<div class="small-btn">', unsafe_allow_html=True)
if st.button("+ SMALL (S)"):
    if len(st.session_state.temp_input) < 10:
        st.session_state.temp_input.append("S")
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

cols_s = st.columns(5)
for i, n in enumerate([0,1,2,3,4]):
    with cols_s[i]:
        st.markdown('<div class="num-btn">', unsafe_allow_html=True)
        if st.button(str(n), key=f"s{n}"):
            if len(st.session_state.temp_input) < 10:
                st.session_state.temp_input.append(f"S-{n}")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# UNDO Button
st.markdown('<div class="undo-btn">', unsafe_allow_html=True)
if st.button("⬅ ভুল হয়েছে? শেষ ইনপুট কাটুন (UNDO)"):
    if st.session_state.temp_input:
        st.session_state.temp_input.pop()
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Pattern Display
p_text = f"প্যাটার্ন ({len(st.session_state.temp_input)}/10): " + (", ".join(st.session_state.temp_input) if st.session_state.temp_input else "ইনপুট দিন...")
st.markdown(f'<div class="pattern-box">{p_text}</div>', unsafe_allow_html=True)

# Period Input
period = st.text_input("", placeholder="পিরিয়ড নম্বর দিন (যেমন: 655)")

# SIGNAL Button
st.markdown('<div class="signal-btn">', unsafe_allow_html=True)
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if len(st.session_state.temp_input) == 10 and period:
        st.session_state.show_res = True
    else:
        st.warning("⚠️ ১০টি রেজাল্ট এবং পিরিয়ড প্রয়োজন!")
st.markdown('</div>', unsafe_allow_html=True)

# --- রেজাল্ট প্রদর্শন ---
if st.session_state.show_res:
    prediction, win_chance = advanced_predict(st.session_state.temp_input, period)
    st.markdown(f"### Result: {prediction} ({win_chance}%)")
    
    col1, col2 = st.columns(2)
    if col1.button("✅ WIN"):
        st.session_state.history.insert(0, f"Period {period}: {prediction} ✅")
        c.execute("INSERT INTO history (period, prediction, win_chance, result) VALUES (?,?,?,?)", (period, prediction, win_chance, "WIN"))
        conn.commit()
        st.session_state.temp_input, st.session_state.show_res = [], False
        st.rerun()
    if col2.button("❌ LOSS"):
        st.session_state.history.insert(0, f"Period {period}: {prediction} ❌")
        c.execute("INSERT INTO history (period, prediction, win_chance, result) VALUES (?,?,?,?)", (period, prediction, win_chance, "LOSS"))
        conn.commit()
        st.session_state.temp_input, st.session_state.show_res = [], False
        st.rerun()

# History
st.write("---")
st.subheader("🕒 VIP History")
for h in st.session_state.history[:5]:
    st.write(h)
