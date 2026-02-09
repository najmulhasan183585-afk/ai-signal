import streamlit as st

# --- ১. অ্যাপ কনফিগারেশন ---
st.set_page_config(page_title="AI Analysis Dashboard", layout="centered")

# --- ২. কাস্টম CSS (ছবির মতো হুবহু কালার ও ডিজাইন) ---
st.markdown("""
<style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp {
        background-color: #0d1117;
    }
    
    /* বাটন কন্টেইনার স্টাইল */
    .main-box {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
    }

    /* বাটনগুলোকে এক সারিতে (Row) আনার জন্য বিন্যাস */
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .stButton > button {
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        height: 40px !important;
        font-size: 14px !important;
    }

    /* --- Big Row এর কালার সেট --- */
    div[data-testid="column"]:nth-of-type(1) button { background: #3498db !important; } /* +Big */
    div[data-testid="column"]:nth-of-type(2) button { background: #ff5733 !important; } /* 5 */
    div[data-testid="column"]:nth-of-type(3) button { background: #c70039 !important; } /* 6 */
    div[data-testid="column"]:nth-of-type(4) button { background: #900c3f !important; } /* 7 */
    div[data-testid="column"]:nth-of-type(5) button { background: #581845 !important; } /* 8 */
    div[data-testid="column"]:nth-of-type(6) button { background: #2c3e50 !important; } /* 9 */

    /* --- Small Row এর কালার সেট --- */
    div[data-testid="column"]:nth-of-type(7) button { background: #e67e22 !important; } /* +Small */
    div[data-testid="column"]:nth-of-type(8) button { background: #2ecc71 !important; } /* 0 */
    div[data-testid="column"]:nth-of-type(9) button { background: #27ae60 !important; } /* 1 */
    div[data-testid="column"]:nth-of-type(10) button { background: #16a085 !important; } /* 2 */
    div[data-testid="column"]:nth-of-type(11) button { background: #f1c40f !important; } /* 3 */
    div[data-testid="column"]:nth-of-type(12) button { background: #f39c12 !important; } /* 4 */

    /* ইনপুট বক্স ডিসপ্লে (কালো ব্যাকগ্রাউন্ড ও সবুজ টেক্সট) */
    .input-display {
        background-color: #1a1a1a;
        color: #00ff41;
        padding: 15px;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        margin-top: 20px;
        min-height: 100px;
        text-align: left;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# --- ৩. ডাটা স্টোরেজ (Session State) ---
if "input_data" not in st.session_state:
    st.session_state.input_data = []

# --- ৪. ইউজার ইন্টারফেস (UI) ---
st.title("📊 AI Analysis Dashboard")

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.write("### Pattern Input Row")
    
    # --- BIG ROW সাজানো ---
    col_b = st.columns([1.5, 1, 1, 1, 1, 1])
    col_b[0].button("+Big", key="label_big")
    if col_b[1].button("5", key="b5"): st.session_state.input_data.append("B-5")
    if col_b[2].button("6", key="b6"): st.session_state.input_data.append("B-6")
    if col_b[3].button("7", key="b7"): st.session_state.input_data.append("B-7")
    if col_b[4].button("8", key="b8"): st.session_state.input_data.append("B-8")
    if col_b[5].button("9", key="b9"): st.session_state.input_data.append("B-9")

    st.write("") # সামান্য গ্যাপ

    # --- SMALL ROW সাজানো ---
    col_s = st.columns([1.5, 1, 1, 1, 1, 1])
    col_s[0].button("+Small", key="label_small")
    if col_s[1].button("0", key="s0"): st.session_state.input_data.append("S-0")
    if col_s[2].button("1", key="s1"): st.session_state.input_data.append("S-1")
    if col_s[3].button("2", key="s2"): st.session_state.input_data.append("S-2")
    if col_s[4].button("3", key="s3"): st.session_state.input_data.append("S-3")
    if col_s[5].button("4", key="s4"): st.session_state.input_data.append("S-4")

    # --- ইনপুট ডিসপ্লে ---
    display_text = " , ".join(st.session_state.input_data)
    st.markdown(f'<div class="input-display">Input:<br>{display_text}</div>', unsafe_allow_html=True)

    # --- কন্ট্রোল বাটন ---
    st.write("")
    c1, c2 = st.columns(2)
    if c1.button("⬅️ UNDO"):
        if st.session_state.input_data:
            st.session_state.input_data.pop()
            st.rerun()
    if c2.button("🔄 RESET"):
        st.session_state.input_data = []
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    
