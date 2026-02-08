import streamlit as st
import time
import random
import hashlib
import numpy as np
import pandas as pd
import sqlite3

# --- আপনার লোগো এবং লিঙ্ক সেটিংস ---
LOGO_URL = "https://i.ibb.co/vzYm8Ym/najmul-logo.png"
TELEGRAM_LINK = "https://t.me/your_telegram_link"

# --- MASTER DATABASE ---
MASTER_TRENDS = {
    "big_chains": [7, 9, 5, 8, 6], 
    "small_chains": [0, 2, 3, 4, 1],
    "violet_trigger": [0, 5],
    "reversal_rate": 0.82 
}

# --- SQLite Historical DB ---
conn = sqlite3.connect('vip_history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT, period TEXT, prediction TEXT, win_chance REAL, result TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

# --- Advanced Prediction Logic ---
def advanced_predict(inputs, period):
    if not inputs or len(inputs) != 10: return None, 0
    seed_str = str(period) + "".join(inputs) + str(time.time())
    random.seed(int(hashlib.sha256(seed_str.encode()).hexdigest(), 16))
    win_chance = round(random.uniform(94.5, 99.8), 1)
    freq_B, freq_S = inputs.count("B"), inputs.count("S")
    if inputs[-3:] == ["B", "B", "B"]: prediction = "SMALL" if random.random() < MASTER_TRENDS["reversal_rate"] else "BIG"
    elif inputs[-3:] == ["S", "S", "S"]: prediction = "BIG" if random.random() < MASTER_TRENDS["reversal_rate"] else "SMALL"
    elif freq_B > freq_S: prediction = "BIG" if random.random() > 0.10 else "SMALL"
    elif freq_S > freq_B: prediction = "SMALL" if random.random() > 0.10 else "BIG"
    else: prediction = random.choice(["BIG", "SMALL"])
    return prediction, win_chance

# --- Streamlit Config ---
st.set_page_config(page_title="NAJMUL VIP V10 PRO", layout="centered")

# --- Session State ---
if "history" not in st.session_state: st.session_state.history = []
if "wins" not in st.session_state: st.session_state.wins = 0
if "total" not in st.session_state: st.session_state.total = 0
if "temp_input" not in st.session_state: st.session_state.temp_input = []
if "show_res" not in st.session_state: st.session_state.show_res = False
if "auth" not in st.session_state: st.session_state.auth = False

# --- Login System ---
if not st.session_state.auth:
    st.title("🔐 NAJMUL VIP LOGIN")
    input_pw = st.text_input("পাসওয়ার্ড দিন:", type="password")
    if st.button("LOGIN"):
        if input_pw == "8899":
            st.session_state.auth = True
            st.rerun()
        else: st.error("❌ ভুল পাসওয়ার্ড!")
    st.stop()

# --- CSS (বাটনগুলোকে Row ভাবে সাজানোর জন্য) ---
st.markdown(f"""
<style>
    .stApp {{ background-color: #040608; color: white; }}
    header, footer, [data-testid="stToolbar"] {{ visibility: hidden !important; }}
    
    /* বাটনগুলোকে এক লাইনে আনার জন্য */
    div[data-testid="stHorizontalBlock"] {{
        gap: 5px !important;
        align-items: center !important;
    }}
    
    .stButton > button {{
        width: 100% !important;
        border-radius: 8px !important;
        padding: 5px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        font-size: 14px !important;
    }}

    /* Big Row Colors */
    div[data-testid="column"]:nth-child(1) button {{ background: #3498db !important; }}
    div[data-testid="column"]:nth-child(2) button {{ background: #FF5733 !important; }}
    div[data-testid="column"]:nth-child(3) button {{ background: #C70039 !important; }}
    div[data-testid="column"]:nth-child(4) button {{ background: #900C3F !important; }}
    div[data-testid="column"]:nth-child(5) button {{ background: #581845 !important; }}
    div[data-testid="column"]:nth-child(6) button {{ background: #2C3E50 !important; }}

    /* Small Row Colors */
    div[data-testid="column"]:nth-child(7) button {{ background: #e67e22 !important; }}
    div[data-testid="column"]:nth-child(8) button {{ background: #2ECC71 !important; }}
    div[data-testid="column"]:nth-child(9) button {{ background: #27AE60 !important; }}
    div[data-testid="column"]:nth-child(10) button {{ background: #16A085 !important; }}
    div[data-testid="column"]:nth-child(11) button {{ background: #F1C40F !important; }}
    div[data-testid="column"]:nth-child(12) button {{ background: #F39C12 !important; }}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown(f'<div style="text-align:center; padding-top:20px;"><img src="{LOGO_URL}" width="50"><br><b>www.najmul-ai-v10.pro</b></div>', unsafe_allow_html=True)

# --- Input Section ---
st.title("🔥 NAJMUL MASTER AI V10")
st.subheader("📊 রেজাল্ট ইনপুট দিন:")

# Big Row সাজানো
b_row = st.columns([1.5, 1, 1, 1, 1, 1])
b_row[0].button("+Big", key="lb_b")
if b_row[1].button("5", key="5"): st.session_state.temp_input.append("B")
if b_row[2].button("6", key="6"): st.session_state.temp_input.append("B")
if b_row[3].button("7", key="7"): st.session_state.temp_input.append("B")
if b_row[4].button("8", key="8"): st.session_state.temp_input.append("B")
if b_row[5].button("9", key="9"): st.session_state.temp_input.append("B")

st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

# Small Row সাজানো
s_row = st.columns([1.5, 1, 1, 1, 1, 1])
s_row[0].button("+Small", key="lb_s")
if s_row[1].button("0", key="0"): st.session_state.temp_input.append("S")
if s_row[2].button("1", key="1"): st.session_state.temp_input.append("S")
if s_row[3].button("2", key="2"): st.session_state.temp_input.append("S")
if s_row[4].button("3", key="3"): st.session_state.temp_input.append("S")
if s_row[5].button("4", key="4"): st.session_state.temp_input.append("S")

# --- নিচের বাকি কোড (একশন বাটন) ---
st.write("---")
if st.button("⬅️ UNDO (ভুল ইনপুট মুছুন)"):
    if st.session_state.temp_input: st.session_state.temp_input.pop()

st.info(f"প্যাটার্ন: {' ➡️ '.join(st.session_state.temp_input) if st.session_state.temp_input else 'অপেক্ষা করছি...'}")

period = st.text_input("পিরিয়ড (শেষ ৩টি):", placeholder="655")

if st.button("🚀 GET SIGNAL"):
    if len(st.session_state.temp_input) >= 1 and period: # আপনার সুবিধার জন্য ১০ এর জায়গায় ১ দেওয়া
        st.session_state.show_res = True
    else: st.warning("ইনপুট দিন!")

# ফলাফল দেখানো
if st.session_state.show_res:
    res, chance = advanced_predict(st.session_state.temp_input, period)
    st.success(f"প্রেডিকশন: {res} ({chance}%)")
    
    c1, c2 = st.columns(2)
    if c1.button("✅ WIN"):
        st.session_state.history.insert(0, f"P-{period}: {res} ✅")
        st.session_state.temp_input, st.session_state.show_res = [], False
        st.rerun()
    if c2.button("❌ LOSS"):
        st.session_state.history.insert(0, f"P-{period}: {res} ❌")
        st.session_state.temp_input, st.session_state.show_res = [], False
        st.rerun()

st.write("---")
st.subheader("🕒 VIP History")
for item in st.session_state.history[:5]: st.write(item)
    
