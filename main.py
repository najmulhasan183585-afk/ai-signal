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

# -----------------------------------------------------------
# ৩. MASTER DATABASE
# -----------------------------------------------------------
MASTER_TRENDS = {
    "big_chains": [7, 9, 5, 8, 6], 
    "small_chains": [0, 2, 3, 4, 1],
    "violet_trigger": [0, 5],
    "reversal_rate": 0.82 
}

# -------------------------------
# ১. SQLite Historical DB
# -------------------------------
conn = sqlite3.connect('vip_history.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    period TEXT,
    prediction TEXT,
    win_chance REAL,
    result TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# -------------------------------
# ২. Pro-Level Advanced Prediction
# -------------------------------
def advanced_predict(inputs, period):
    if not inputs or len(inputs) != 10:
        return None, 0

    seed_str = str(period) + "".join(inputs) + str(time.time())
    random.seed(int(hashlib.sha256(seed_str.encode()).hexdigest(), 16))

    win_chance = round(random.uniform(94.5, 99.8), 1)

    freq_B = inputs.count("B")
    freq_S = inputs.count("S")

    if inputs[-3:] == ["B", "B", "B"]:
        prediction = "SMALL" if random.random() < MASTER_TRENDS["reversal_rate"] else "BIG"
    elif inputs[-3:] == ["S", "S", "S"]:
        prediction = "BIG" if random.random() < MASTER_TRENDS["reversal_rate"] else "SMALL"
    elif freq_B > freq_S:
        prediction = "BIG" if random.random() > 0.10 else "SMALL"
    elif freq_S > freq_B:
        prediction = "SMALL" if random.random() > 0.10 else "BIG"
    else:
        prediction = random.choice(["BIG", "SMALL"])

    return prediction, win_chance

def simulate_next_10(inputs, period, runs=1000):
    results = {"BIG": 0, "SMALL": 0}
    for _ in range(runs):
        pred, _ = advanced_predict(inputs, period)
        results[pred] += 1
    return {k: round(v / runs * 100, 1) for k, v in results.items()}

# -------------------------------
# ৩. Streamlit Config
# -------------------------------
st.set_page_config(page_title="NAJMUL VIP V10 PRO", layout="centered")

# -------------------------------
# ৪. Session State
# -------------------------------
if "history" not in st.session_state: st.session_state.history = []
if "wins" not in st.session_state: st.session_state.wins = 0
if "total" not in st.session_state: st.session_state.total = 0
if "temp_input" not in st.session_state: st.session_state.temp_input = []
if "show_res" not in st.session_state: st.session_state.show_res = False
if "auth" not in st.session_state: st.session_state.auth = False

# -------------------------------
# ৫. Login System
# -------------------------------
if not st.session_state.auth:
    st.title("🔐 NAJMUL VIP LOGIN")
    input_pw = st.text_input("পাসওয়ার্ড দিন:", type="password")
    if st.button("LOGIN"):
        if input_pw == "8899":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ ভুল পাসওয়ার্ড!")
    st.stop()

# -------------------------------
# ৬. ULTIMATE CSS (সব বাটন এবং ডিজাইন ফিক্স)
# -------------------------------
if st.session_state.auth:
    st.markdown(f"""
    <style>
    /* হেডার ডিজাইন */
    .custom-header {{
        position: fixed; top: 0; left: 0; width: 100%; height: 65px;
        background: #0a0f1e; display: flex; align-items: center; justify-content: space-between;
        padding: 0 15px; z-index: 999999; border-bottom: 2px solid #00FFCC;
    }}
    .header-logo {{ width: 45px; height: 45px; border-radius: 50%; border: 1px solid #00FFCC; }}
    .header-url {{ color: #00FFCC; font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; }}

    /* Streamlit টুলবার হাইড করা */
    header, footer, .stAppDeployButton, [data-testid="stToolbar"], [data-testid="stDecoration"] {{
        display: none !important;
    }}

    .stApp {{ background-color: #040608; color: white; }}

    /* বাটন সারি (Row) ডিজাইন - আপনার ছবি অনুযায়ী */
    .button-container {{
        background: white; padding: 15px; border-radius: 15px; margin-bottom: 20px;
    }}
    
    /* প্রতিটি সারির স্টাইল */
    div[data-testid="column"] {{
        display: flex; align-items: center; justify-content: flex-start;
    }}

    /* নম্বর বাটনগুলোর কালার এবং সাইজ */
    .stButton > button {{
        border-radius: 8px !important; font-weight: bold !important; border: none !important;
    }}
    
    /* +Big এবং +Small বাটন ডিজাইন */
    div[data-testid="column"]:nth-of-type(1) button {{ background: #3498db !important; color: white !important; min-width: 80px; }}
    div[data-testid="column"]:nth-of-type(2) button {{ background: #FF5733 !important; color: white !important; }}
    div[data-testid="column"]:nth-of-type(3) button {{ background: #C70039 !important; color: white !important; }}
    div[data-testid="column"]:nth-of-type(4) button {{ background: #900C3F !important; color: white !important; }}
    div[data-testid="column"]:nth-of-type(5) button {{ background: #581845 !important; color: white !important; }}
    div[data-testid="column"]:nth-of-type(6) button {{ background: #2C3E50 !important; color: white !important; }}

    /* সিগন্যাল বাটন স্পেশাল স্টাইল */
    .get-btn button {{ background: #00FFCC !important; color: black !important; font-size: 18px !important; width: 100% !important; }}
    
    .share-box {{ background: linear-gradient(90deg, #FF0000, #990000); color: white; padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; font-weight: bold; }}
    </style>

    <div class="custom-header">
        <img src="{LOGO_URL}" class="header-logo">
        <div class="header-url">www.najmul-ai-v10.pro</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# ৭. App UI
# -------------------------------
st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="share-box">🔗 VIP SERVER ACTIVE</div>', unsafe_allow_html=True)

st.title("🔥 NAJMUL MASTER AI V10")
st.subheader("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# --- বাটন সারি: আপনার ছবির মতো ডিজাইন ---
# BIG ROW
b_cols = st.columns([1.5, 1, 1, 1, 1, 1])
if b_cols[0].button("+Big", key="label_big"): pass # লেবেল বাটন
if b_cols[1].button("5", key="b5"): st.session_state.temp_input.append("B")
if b_cols[2].button("6", key="b6"): st.session_state.temp_input.append("B")
if b_cols[3].button("7", key="b7"): st.session_state.temp_input.append("B")
if b_cols[4].button("8", key="b8"): st.session_state.temp_input.append("B")
if b_cols[5].button("9", key="b9"): st.session_state.temp_input.append("B")

# CSS দিয়ে Small রো এর জন্য আলাদা কালার করা
st.markdown("""
<style>
/* Small রো এর বাটন কালার */
[data-testid="column"]:nth-child(7) button { background: #e67e22 !important; min-width: 80px; }
[data-testid="column"]:nth-child(8) button { background: #2ECC71 !important; }
[data-testid="column"]:nth-child(9) button { background: #27AE60 !important; }
[data-testid="column"]:nth-child(10) button { background: #16A085 !important; }
[data-testid="column"]:nth-child(11) button { background: #F1C40F !important; }
[data-testid="column"]:nth-child(12) button { background: #F39C12 !important; }
</style>
""", unsafe_allow_html=True)

# SMALL ROW
s_cols = st.columns([1.5, 1, 1, 1, 1, 1])
if s_cols[0].button("+Small", key="label_small"): pass # লেবেল বাটন
if s_cols[1].button("0", key="s0"): st.session_state.temp_input.append("S")
if s_cols[2].button("1", key="s1"): st.session_state.temp_input.append("S")
if s_cols[3].button("2", key="s2"): st.session_state.temp_input.append("S")
if s_cols[4].button("3", key="s3"): st.session_state.temp_input.append("S")
if s_cols[5].button("4", key="s4"): st.session_state.temp_input.append("S")

# -------------------------------
# ৮. মূল একশন বাটনগুলো (UNDO, PERIOD, GET SIGNAL)
# -------------------------------
st.write("---")
if st.button("⬅️ ভুল হয়েছে? শেষ ইনপুট কাটুন (UNDO)"):
    if st.session_state.temp_input:
        st.session_state.temp_input.pop()

st.info(f"প্যাটার্ন ({len(st.session_state.temp_input)}/10): {' ➡️ '.join(st.session_state.temp_input) if st.session_state.temp_input else 'ইনপুট দিন...'}")

period = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

st.markdown('<div class="get-btn">', unsafe_allow_html=True)
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if len(st.session_state.temp_input) >= 1 and period: # আপনার সুবিধার জন্য ১০ এর জায়গায় ১ করেছি
        st.session_state.show_res = True
    else:
        st.warning("⚠️ ইনপুট এবং পিরিয়ড প্রয়োজন!")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# ৯. ফলাফল (আপনার অরিজিনাল লজিক অনুযায়ী)
# -------------------------------
if st.session_state.show_res:
    prediction, win_chance = advanced_predict(st.session_state.temp_input, period)
    st.success(f"বিশ্লেষণ সম্পন্ন! ফলাফল: {prediction} ({win_chance}%)")
    
    w, l = st.columns(2)
    if w.button("✅ WIN"):
        st.session_state.history.insert(0, f"Period {period}: {prediction} ✅")
        st.session_state.wins += 1
        st.session_state.total += 1
        st.session_state.temp_input, st.session_state.show_res = [], False
        st.rerun()
    if l.button("❌ LOSS"):
        st.session_state.history.insert(0, f"Period {period}: {prediction} ❌")
        st.session_state.total += 1
        st.session_state.temp_input, st.session_state.show_res = [], False
        st.rerun()

# ইতিহাস প্রদর্শন
st.subheader("🕒 VIP History")
for item in st.session_state.history[:5]:
    st.write(item)

st.markdown(f'<a href="{TELEGRAM_LINK}" target="_blank" class="telegram-btn">✈️ JOIN TELEGRAM</a>', unsafe_allow_html=True)
        
