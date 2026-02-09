import streamlit as st

# --- বাটনগুলোর জন্য কাস্টম CSS (ছবির মতো কালার ও বিন্যাস) ---
st.markdown("""
<style>
    /* বাটনগুলোকে এক সারিতে আনার জন্য বিন্যাস */
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
        padding: 0px !important;
    }

    /* Big Row Colors (ছবির সাথে মিল রেখে) */
    div[data-testid="column"]:nth-of-type(1) button { background: #4AA3DF !important; } /* +Big */
    div[data-testid="column"]:nth-of-type(2) button { background: #FF5733 !important; } /* 5 */
    div[data-testid="column"]:nth-of-type(3) button { background: #C70039 !important; } /* 6 */
    div[data-testid="column"]:nth-of-type(4) button { background: #900C3F !important; } /* 7 */
    div[data-testid="column"]:nth-of-type(5) button { background: #581845 !important; } /* 8 */
    div[data-testid="column"]:nth-of-type(6) button { background: #2C3E50 !important; } /* 9 */

    /* Small Row Colors (ছবির সাথে মিল রেখে) */
    div[data-testid="column"]:nth-of-type(7) button { background: #E67E22 !important; } /* +Small */
    div[data-testid="column"]:nth-of-type(8) button { background: #2ECC71 !important; } /* 0 */
    div[data-testid="column"]:nth-of-type(9) button { background: #27AE60 !important; } /* 1 */
    div[data-testid="column"]:nth-of-type(10) button { background: #16A085 !important; } /* 2 */
    div[data-testid="column"]:nth-of-type(11) button { background: #F1C40F !important; } /* 3 */
    div[data-testid="column"]:nth-of-type(12) button { background: #F39C12 !important; } /* 4 */
    
    /* ইনপুট ডিসপ্লে বক্সের স্টাইল */
    .input-box {
        background-color: #1E1E1E;
        color: #00FF00;
        padding: 15px;
        border-radius: 15px;
        font-family: 'Courier New', monospace;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# সেশন স্টেট চেক (যদি আগে না থাকে)
if "temp_input" not in st.session_state:
    st.session_state.temp_input = []

# --- UI সাজানো ---
st.markdown('<div style="background-color: white; padding: 20px; border-radius: 20px; color: black; text-align: center;">', unsafe_allow_html=True)
st.write("### AI Analysis Dashboard")

# ১. Big Row সাজানো
st.write("**Pattern Input Row**")
col_b = st.columns([1.5, 1, 1, 1, 1, 1])
col_b[0].button("+Big", key="b_label")
if col_b[1].button("5", key="b5"): st.session_state.temp_input.append("B-5")
if col_b[2].button("6", key="b6"): st.session_state.temp_input.append("B-6")
if col_b[3].button("7", key="b7"): st.session_state.temp_input.append("B-7")
if col_b[4].button("8", key="b8"): st.session_state.temp_input.append("B-8")
if col_b[5].button("9", key="b9"): st.session_state.temp_input.append("B-9")

st.write("") # গ্যাপ

# ২. Small Row সাজানো
col_s = st.columns([1.5, 1, 1, 1, 1, 1])
col_s[0].button("+Small", key="s_label")
if col_s[1].button("0", key="s0"): st.session_state.temp_input.append("S-0")
if col_s[2].button("1", key="s1"): st.session_state.temp_input.append("S-1")
if col_s[3].button("2", key="s2"): st.session_state.temp_input.append("S-2")
if col_s[4].button("3", key="s3"): st.session_state.temp_input.append("S-3")
if col_s[5].button("4", key="s4"): st.session_state.temp_input.append("S-4")

# ৩. ইনপুট ডিসপ্লে বক্স (ছবির মতো সবুজ টেক্সট)
input_text = ", ".join(st.session_state.temp_input)
st.markdown(f'<div class="input-box">Input: <br>{input_text}</div>', unsafe_allow_html=True)

if st.button("Reset Display"):
    st.session_state.temp_input = []
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
    
