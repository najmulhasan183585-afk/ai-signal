import streamlit as st

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal VIP", layout="centered")

# সেশন স্টেট ইনিশিয়ালাইজ করা
if 'pattern_list' not in st.session_state:
    st.session_state.pattern_list = []

# বাটন ক্লিকের লজিক (পাইথন অংশ)
# query_params ব্যবহার করা হয়েছে যাতে রিলোড হলেও ডাটা হারিয়ে না যায়
q_params = st.query_params
if "add" in q_params:
    new_val = q_params["add"]
    if len(st.session_state.pattern_list) < 10:
        st.session_state.pattern_list.append(new_val)
    st.query_params.clear() # প্যারামিটার মুছে ফেলা যাতে লুপ না হয়

# হেডিং
st.markdown("<h2 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h2>", unsafe_allow_html=True)

# কাস্টম বাটন ডিজাইন (HTML/CSS)
# এখানে প্রতিটি লিঙ্কে target="_self" ব্যবহার করা হয়েছে যাতে একই উইন্ডোতে থাকে
button_style = """
<style>
    .btn-container {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 20px;
    }
    .btn-row {
        display: flex;
        gap: 5px;
    }
    .btn {
        flex: 1;
        height: 45px;
        border: none;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        line-height: 45px;
        text-decoration: none;
        cursor: pointer;
    }
    .big { flex: 2; background-color: #3498db; }
    .small { flex: 2; background-color: #e67e22; }
    .c5 { background-color: #ff4d4d; } .c6 { background-color: #d63031; }
    .c7 { background-color: #8e44ad; } .c8 { background-color: #2c3e50; }
    .c9 { background-color: #34495e; } .c0 { background-color: #2ecc71; }
    .c1 { background-color: #27ae60; } .c2 { background-color: #16a085; }
    .c3 { background-color: #f1c40f; color: black; } .c4 { background-color: #f39c12; }
</style>

<div class="btn-container">
    <div class="btn-row">
        <a href="/?add=Big" target="_self" class="btn big">+Big</a>
        <a href="/?add=5" target="_self" class="btn c5">5</a>
        <a href="/?add=6" target="_self" class="btn c6">6</a>
        <a href="/?add=7" target="_self" class="btn c7">7</a>
        <a href="/?add=8" target="_self" class="btn c8">8</a>
        <a href="/?add=9" target="_self" class="btn c9">9</a>
    </div>
    <div class="btn-row">
        <a href="/?add=Small" target="_self" class="btn small">+Small</a>
        <a href="/?add=0" target="_self" class="btn c0">0</a>
        <a href="/?add=1" target="_self" class="btn c1">1</a>
        <a href="/?add=2" target="_self" class="btn c2">2</a>
        <a href="/?add=3" target="_self" class="btn c3">3</a>
        <a href="/?add=4" target="_self" class="btn c4">4</a>
    </div>
</div>
"""
st.markdown(button_style, unsafe_allow_html=True)

# ডাটা প্রসেসিং
current_pattern = ",".join(st.session_state.pattern_list)
count = len(st.session_state.pattern_list)

# ইনপুট বক্স (যেখানে ১-১০ পর্যন্ত সংখ্যা উঠবে)
st.text_input(f"প্যাটার্ন ({count}/10):", value=current_pattern, key="pattern_display")

# পিরিয়ড ইনপুট
st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# সিগন্যাল বাটন
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if count > 0:
        st.success(f"আপনার ইনপুট '{current_pattern}' প্রসেস হচ্ছে...")
    else:
        st.warning("দয়া করে আগে বাটন চেপে ইনপুট দিন!")

# UNDO এবং CLEAR বাটন (সুবিধার জন্য)
col_un, col_cl = st.columns(2)
with col_un:
    if st.button("⬅️ UNDO"):
        if st.session_state.pattern_list:
            st.session_state.pattern_list.pop()
            st.rerun()
with col_cl:
    if st.button("🗑️ CLEAR ALL"):
        st.session_state.pattern_list = []
        st.rerun()
        
