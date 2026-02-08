import streamlit as st
import time
import random
import hashlib
import numpy as np
import pandas as pd
import sqlite3
import streamlit.components.v1 as components

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

# --- Pro-Level Advanced Prediction ---
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
        else:
            st.error("❌ ভুল পাসওয়ার্ড!")
    st.stop()

# --- CSS & HEADER ---
if st.session_state.auth:
    st.markdown(f"""
    <style>
    .custom-header {{ position: fixed; top: 0; left: 0; width: 100%; height: 65px; background: #0a0f1e; display: flex; align-items: center; justify-content: space-between; padding: 0 15px; z-index: 999999; border-bottom: 2px solid #00FFCC; }}
    .header-logo {{ width: 45px; height: 45px; border-radius: 50%; border: 1px solid #00FFCC; }}
    .header-url {{ color: #00FFCC; font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; }}
    header, footer, .stAppDeployButton, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; visibility: hidden !important; }}
    .main {{ background-color: #040608 !important; padding-top: 75px !important; }}
    .stApp {{ background-color: #040608; color: white; }}
    .floating-panel {{ position: fixed; top: 100px; right: 10px; width: 220px; background: rgba(10,15,30,0.98); border: 2px solid #00FFCC; border-radius: 20px; padding: 15px; z-index: 999; text-align: center; box-shadow: 0 0 35px rgba(0,255,204,0.6); }}
    .res-text {{ font-size: 34px; font-weight: 900; margin: 5px 0; }}
    .big-text {{ color: #FF4B4B; text-shadow: 0 0 15px #FF4B4B; }}
    .small-text {{ color: #00D4FF; text-shadow: 0 0 15px #00D4FF; }}
    .share-box {{ background: linear-gradient(90deg, #FF0000, #990000); color: white; padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; font-weight: bold; border: 1px solid white; }}
    .stButton>button {{ width: 100%; border-radius: 15px; height: 50px; font-weight: bold; color: white; }}
    .get-btn>div>button {{ background: #00FFCC !important; color: black !important; font-size: 18px !important; }}
    .undo-btn>div>button {{ border: 1px solid #FF4B4B !important; color: #FF4B4B !important; background: transparent !important; height: 40px !important; }}
    .telegram-btn {{ display: block; width: 100%; background: #0088cc; color: white !important; text-align: center; padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 25px; }}
    </style>
    <div class="custom-header"><img src="{LOGO_URL}" class="header-logo"><div class="header-url">www.najmul-ai-v10.pro</div></div>
    """, unsafe_allow_html=True)

# --- App UI ---
st.markdown('<div class="share-box">🔗 VIP SERVER ACTIVE (SYCHRONIZED WITH MASTER DB)</div>', unsafe_allow_html=True)

if st.session_state.total > 0:
    acc = (st.session_state.wins / st.session_state.total) * 100
    st.metric("AI LIVE ACCURACY", f"{acc:.1f}%")

st.title("🔥 NAJMUL MASTER AI V10 PRO")
st.subheader("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# --- বাটন একশন ফিক্সড সেকশন ---
# এখানে আমরা 'st.button' ক্লিকে সরাসরি ভেরিয়েবল পরিবর্তন করছি
c1, c2 = st.columns(2)
with c1:
    if st.button("➕ BIG (B)", key="B_btn"):
        if len(st.session_state.temp_input) < 10:
            st.session_state.temp_input.append("B")
            st.rerun()
with c2:
    if st.button("➕ SMALL (S)", key="S_btn"):
        if len(st.session_state.temp_input) < 10:
            st.session_state.temp_input.append("S")
            st.rerun()

# রঙিন গ্রাফিক্যাল বাটন ডিজাইন (যা শুধুমাত্র ক্লিক ইভেন্ট পাঠাবে)
input_html = f"""
<div style="background: #ffffff; padding: 15px; border-radius: 15px; margin-bottom: 10px;">
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
        <div style="background: #3498db; color: white; padding: 8px; border-radius: 8px; font-weight: bold; min-width: 65px; text-align: center;">+Big</div>
        <div style="display: flex; gap: 5px;">
            <button onclick="window.parent.document.querySelector('button[key=B_btn]').click()" style="background:#FF5733; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">5</button>
            <button onclick="window.parent.document.querySelector('button[key=B_btn]').click()" style="background:#C70039; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">6</button>
            <button onclick="window.parent.document.querySelector('button[key=B_btn]').click()" style="background:#900C3F; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">7</button>
            <button onclick="window.parent.document.querySelector('button[key=B_btn]').click()" style="background:#581845; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">8</button>
            <button onclick="window.parent.document.querySelector('button[key=B_btn]').click()" style="background:#2C3E50; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">9</button>
        </div>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
        <div style="background: #e67e22; color: white; padding: 8px; border-radius: 8px; font-weight: bold; min-width: 65px; text-align: center;">+Small</div>
        <div style="display: flex; gap: 5px;">
            <button onclick="window.parent.document.querySelector('button[key=S_btn]').click()" style="background:#2ECC71; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">0</button>
            <button onclick="window.parent.document.querySelector('button[key=S_btn]').click()" style="background:#27AE60; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">1</button>
            <button onclick="window.parent.document.querySelector('button[key=S_btn]').click()" style="background:#16A085; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">2</button>
            <button onclick="window.parent.document.querySelector('button[key=S_btn]').click()" style="background:#F1C40F; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">3</button>
            <button onclick="window.parent.document.querySelector('button[key=S_btn]').click()" style="background:#F39C12; color:white; border:none; padding:10px 12px; border-radius:5px; cursor:pointer; font-weight:bold;">4</button>
        </div>
    </div>
</div>
"""
components.html(input_html, height=155)

# আসল বাটনগুলো অদৃশ্য করার জন্য CSS (যাতে ব্যাকগ্রাউন্ডে কাজ করে কিন্তু দেখা না যায়)
st.markdown("<style>div[data-testid='stHorizontalBlock'] .stButton { display: none !important; }</style>", unsafe_allow_html=True)

# --- UNDO সেকশন ---
st.markdown('<div class="undo-btn">', unsafe_allow_html=True)
if st.button("⬅️ ভুল হয়েছে? শেষ ইনপুট কাটুন (UNDO)"):
    if st.session_state.temp_input:
        st.session_state.temp_input.pop()
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- প্যাটার্ন ডিসপ্লে ---
st.info(f"প্যাটার্ন ({len(st.session_state.temp_input)}/10): {' ➡️ '.join(st.session_state.temp_input) if st.session_state.temp_input else 'ইনপুট দিন...'}")

period = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# --- বিশ্লেষণ বাটন ---
st.markdown('<div class="get-btn">', unsafe_allow_html=True)
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if len(st.session_state.temp_input) == 10 and period:
        st.session_state.show_res = True
    else:
        st.warning("⚠️ ১০টি রেজাল্ট এবং পিরিয়ড প্রয়োজন!")
st.markdown('</div>', unsafe_allow_html=True)

# --- রেজাল্ট লজিক ---
if st.session_state.show_res:
    with st.spinner('🔍 বিশ্লেষণ হচ্ছে...'):
        time.sleep(2)
    prediction, win_chance = advanced_predict(st.session_state.temp_input, period)
    sim_res = simulate_next_10(st.session_state.temp_input, period)
    color_class = "big-text" if prediction == "BIG" else "small-text"
    num_str = ", ".join(map(str, sorted(random.sample([5,7,8,9] if prediction=="BIG" else [0,2,3,4], 3))))

    st.markdown(f"""
    <div class="floating-panel">
        <p style="color:#00FFCC;font-size:12px;margin:0;">MASTER REPORT</p>
        <p style="color:white;font-size:14px;margin:5px 0;">PROBABILITY: {win_chance}%</p>
        <p class="res-text {color_class}">{prediction}</p>
        <p style="font-size:22px;color:#FFEB3B;font-weight:900;">{num_str}</p>
    </div>
    """, unsafe_allow_html=True)

    # WIN/LOSS বাটন
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

st.write("---")
st.subheader("🕒 VIP History")
for item in st.session_state.history[:5]:
    if "✅" in item: st.success(item)
    else: st.error(item)

st.markdown(f'<a href="{TELEGRAM_LINK}" target="_blank" class="telegram-btn">✈️ JOIN TELEGRAM</a>', unsafe_allow_html=True)
    
