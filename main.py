import streamlit as st
import random
import time
import sqlite3
import hashlib
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(page_title="NAJMUL NUMBER AI", layout="centered")

LOGO_URL = "https://i.ibb.co/vzYm8Ym/najmul-logo.png"
LOGIN_PASSWORD = "8899"

# ---------------- DATABASE ----------------
conn = sqlite3.connect("vip_history.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    period TEXT,
    big_small TEXT,
    numbers TEXT,
    probability REAL,
    result TEXT,
    time DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# ---------------- SESSION ----------------
if "auth" not in st.session_state: st.session_state.auth = False
if "inputs" not in st.session_state: st.session_state.inputs = []
if "show" not in st.session_state: st.session_state.show = False

# ---------------- LOGIN ----------------
if not st.session_state.auth:
    st.title("🔐 NAJMUL VIP LOGIN")
    pw = st.text_input("Password", type="password")
    if st.button("LOGIN"):
        if pw == LOGIN_PASSWORD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Wrong Password")
    st.stop()

# ---------------- HEADER + STYLE ----------------
st.markdown(f"""
<style>
header, footer {{display:none;}}
.stApp {{background:#05070b;color:white;}}
.stButton>button {{width:100%;height:42px;font-weight:bold;border-radius:10px;}}
.input-box {{background:#111;padding:12px;border-radius:12px;color:#00ff99;}}
</style>

<div style="display:flex;align-items:center;gap:10px;">
<img src="{LOGO_URL}" width="45">
<h3>NAJMUL NUMBER AI (NO COLOR)</h3>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT UI ----------------
st.write("### 🔢 Last Results Input")

cols = st.columns(5)
for i in range(10):
    if cols[i % 5].button(str(i)):
        st.session_state.inputs.append(i)
        st.session_state.show = False

st.markdown(
    f"<div class='input-box'>Input: {st.session_state.inputs}</div>",
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)
if c1.button("⬅️ UNDO"):
    if st.session_state.inputs:
        st.session_state.inputs.pop()
        st.rerun()

if c2.button("♻️ RESET"):
    st.session_state.inputs = []
    st.rerun()

period = st.text_input("Period (Last 3 digit)")

# ---------------- AI ENGINE ----------------
def ai_analyse(data, period):
    seed = str(data) + str(period) + str(time.time())
    random.seed(int(hashlib.sha256(seed.encode()).hexdigest(), 16))

    big = sum(1 for x in data if x >= 5)
    small = len(data) - big

    big_small = "BIG" if big >= small else "SMALL"

    if big_small == "BIG":
        nums = random.sample([5,6,7,8,9], 3)
    else:
        nums = random.sample([0,1,2,3,4], 3)

    probability = round(random.uniform(75, 99), 1)
    return big_small, nums, probability

# ---------------- GET SIGNAL ----------------
if st.button("🚀 GET AI SIGNAL"):
    if len(st.session_state.inputs) >= 5 and period:
        st.session_state.show = True
    else:
        st.warning("⚠️ Minimum 5 input & period required")

# ---------------- RESULT ----------------
if st.session_state.show:
    with st.spinner("AI analysing..."):
        time.sleep(2)

    bs, nums, prob = ai_analyse(st.session_state.inputs, period)

    st.success("✅ AI SIGNAL READY")
    st.markdown(f"""
    ### 📊 RESULT
    - **BIG / SMALL:** `{bs}`
    - **POSSIBLE NUMBERS:** `{nums}`
    - **PROBABILITY:** `{prob}%`
    """)

    w, l = st.columns(2)
    if w.button("✅ WIN"):
        c.execute(
            "INSERT INTO history(period,big_small,numbers,probability,result) VALUES (?,?,?,?,?)",
            (period, bs, str(nums), prob, "WIN")
        )
        conn.commit()
        st.session_state.inputs = []
        st.rerun()

    if l.button("❌ LOSS"):
        c.execute(
            "INSERT INTO history(period,big_small,numbers,probability,result) VALUES (?,?,?,?,?)",
            (period, bs, str(nums), prob, "LOSS")
        )
        conn.commit()
        st.session_state.inputs = []
        st.rerun()

# ---------------- HISTORY ----------------
st.write("---")
st.subheader("🕒 VIP HISTORY")
df = pd.read_sql(
    "SELECT period,big_small,numbers,probability,result,time FROM history ORDER BY id DESC LIMIT 5",
    conn
)
st.dataframe(df, use_container_width=True)
