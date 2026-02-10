import streamlit as st

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal Mobile", layout="wide")

# সেশন স্টেট
if 'results' not in st.session_state:
    st.session_state.results = []

# বাটন ক্লিক হলে ডাটা যোগ করার লজিক
query_params = st.query_params
if "clicked" in query_params:
    val = query_params["clicked"]
    if len(st.session_state.results) < 10:
        st.session_state.results.append(val)
    st.query_params.clear()

# কাস্টম CSS (একদম আপনার ছবির মতো ডিজাইন)
st.markdown("""
    <style>
    /* মেইন কন্টেইনার */
    .button-grid {
        display: flex;
        flex-direction: column;
        gap: 8px;
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        max-width: 100%;
    }
    
    /* সারি সেটআপ */
    .row {
        display: flex;
        width: 100%;
        gap: 5px;
    }
    
    /* বাটন স্টাইল */
    .btn {
        flex: 1;
        height: 40px;
        border: none;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        font-size: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        cursor: pointer;
    }

    .btn-big-main { flex: 2; background-color: #3498db; }
    .btn-small-main { flex: 2; background-color: #e67e22; }

    /* নম্বর বাটন কালার */
    .c5 { background-color: #ff4d4d; }
    .c6 { background-color: #d63031; }
    .c7 { background-color: #8e44ad; }
    .c8 { background-color: #2c3e50; }
    .c9 { background-color: #34495e; }
    
    .c0 { background-color: #2ecc71; }
    .c1 { background-color: #27ae60; }
    .c2 { background-color: #16a085; }
    .c3 { background-color: #f1c40f; color: black; }
    .c4 { background-color: #f39c12; }

    /* ইনপুট ফিল্ড স্টাইল */
    .stTextInput input {
        background-color: #1e272e;
        color: white;
        border: 1px solid #34495e;
    }
    </style>
    """, unsafe_allow_html=True)

st.subheader("📊 আগের ১০টি রেজাল্ট ইনপুট দিন:")

# HTML দিয়ে বাটন গ্রিড তৈরি (যাতে মোবাইলে না ভাঙে)
# এখানে বাটনগুলোতে ক্লিক করলে পেজ রিফ্রেশ হয়ে ডাটা ইনপুট হবে
button_html = f"""
<div class="button-grid">
    <div class="row">
        <a href="/?clicked=Big" target="_self" class="btn btn-big-main">+Big</a>
        <a href="/?clicked=5" target="_self" class="btn c5">5</a>
        <a href="/?clicked=6" target="_self" class="btn c6">6</a>
        <a href="/?clicked=7" target="_self" class="btn c7">7</a>
        <a href="/?clicked=8" target="_self" class="btn c8">8</a>
        <a href="/?clicked=9" target="_self" class="btn c9">9</a>
    </div>
    <div class="row">
        <a href="/?clicked=Small" target="_self" class="btn btn-small-main">+Small</a>
        <a href="/?clicked=0" target="_self" class="btn c0">0</a>
        <a href="/?clicked=1" target="_self" class="btn c1">1</a>
        <a href="/?clicked=2" target="_self" class="btn c2">2</a>
        <a href="/?clicked=3" target="_self" class="btn c3">3</a>
        <a href="/?clicked=4" target="_self" class="btn c4">4</a>
    </div>
</div>
"""
st.markdown(button_html, unsafe_allow_html=True)

st.write("") # গ্যাপ

# ডাটা ডিসপ্লে এবং বাকি অংশ
current_pattern = ",".join(st.session_state.results)
st.text_input(f"প্যাটার্ন ({len(st.session_state.results)}/10):", value=current_pattern)

st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    st.info("বিশ্লেষণ করা হচ্ছে...")
    
