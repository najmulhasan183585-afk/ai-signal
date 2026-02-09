import streamlit as st

# ১. বাটনগুলোর জন্য ছবির মতো কাস্টম CSS
st.markdown("""
<style>
    /* মেইন কন্টেইনার স্টাইল */
    .main-container {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        max-width: 500px;
        margin: auto;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    
    /* বাটন বিন্যাস */
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }

    .stButton > button {
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        height: 45px !important;
    }

    /* Big Row Colors (আপনার ছবি অনুযায়ী) */
    div[data-testid="column"]:nth-of-type(1) button { background: #3498db !important; } /* +Big */
    div[data-testid="column"]:nth-of-type(2) button { background: #ff5733 !important; } /* 5 */
    div[data-testid="column"]:nth-of-type(3) button { background: #c70039 !important; } /* 6 */
    div[data-testid="column"]:nth-of-type(4) button { background: #900c3f !important; } /* 7 */
    div[data-testid="column"]:nth-of-type(5) button { background: #581845 !important; } /* 8 */
    div[data-testid="column"]:nth-of-type(6) button { background: #2c3e50 !important; } /* 9 */

    /* Small Row Colors (আপনার ছবি অনুযায়ী) */
    div[data-testid="column"]:nth-of-type(7) button { background: #e67e22 !important; } /* +Small */
    div[data-testid="column"]:nth-of-type(8) button { background: #2ecc71 !important; } /* 0 */
    div[data-testid="column"]:nth-of-type(9) button { background: #27ae60 !important; } /* 1 */
    div[data-testid="column"]:nth-of-type(10) button { background: #16a085 !important; } /* 2 */
    div[data-testid="column"]:nth-of-type(11) button { background: #f1c40f !important; } /* 3 */
    div[data-testid="column"]:nth-of-type(12) button { background: #f39c12 !important; } /* 4 */

    /* ইনপুট রেজাল্ট ডিসপ্লে */
    .input-display {
        background-color: #1a1a1a;
        color: #00ff41;
        padding: 15px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        margin-top: 20px;
        min-height: 80px;
        word-wrap: break-word;
    }
</style>
""", unsafe_allow_html=True)

# ২. সেশন স্টেট (ডাটা মনে রাখার জন্য)
if "input_list" not in st.session_state:
    st.session_state.input_list = []

# ৩. ইন্টারফেস (UI) সাজানো
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.write("### AI Analysis Dashboard")
st.write("Pattern Input Row")

# --- Big Row ---
col_b = st.columns([1.5, 1, 1, 1, 1, 1])
col_b[0].button("+Big", key="label_b")
if col_b[1].button("5", key="b5"): st.session_state.input_list.append("B-5")
if col_b[2].button("6", key="b6"): st.session_state.input_list.append("B-6")
if col_b[3].button("7", key="b7"): st.session_state.input_list.append("B-7")
if col_b[4].button("8", key="b8"): st.session_state.input_list.append("B-8")
if col_b[5].button("9", key="b9"): st.session_state.input_list.append("B-9")

# --- Small Row ---
col_s = st.columns([1.5, 1, 1, 1, 1, 1])
col_s[0].button("+Small", key="label_s")
if col_s[1].button("0", key="s0"): st.session_state.input_list.append("S-0")
if col_s[2].button("1", key="s1"): st.session_state.input_list.append("S-1")
if col_s[3].button("2", key="s2"): st.session_state.input_list.append("S-2")
if col_s[4].button("3", key="s3"): st.session_state.input_list.append("S-3")
if col_s[5].button("4", key="s4"): st.session_state.input_list.append("S-4")

# ৪. কালো বক্সে ইনপুটগুলো দেখানো (ছবির মতো)
st.markdown(f'<div class="input-display">{" , ".join(st.session_state.input_list)}</div>', unsafe_allow_html=True)

# Reset এবং Undo বাটন (ঐচ্ছিক)
c1, c2 = st.columns(2)
if c1.button("UNDO"):
    if st.session_state.input_list: 
        st.session_state.input_list.pop()
        st.rerun()
if c2.button("RESET"):
    st.session_state.input_list = []
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
