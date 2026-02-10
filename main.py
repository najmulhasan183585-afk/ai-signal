import streamlit as st

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal Mobile", layout="centered")

# টাইটেল
st.markdown("<h3 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h3>", unsafe_allow_html=True)

# কাস্টম HTML, CSS এবং JS
# এটি বাটনগুলোকে পাশাপাশি রাখবে এবং রিফ্রেশ ছাড়াই ডাটা ইনপুট বক্সে পাঠাবে
custom_ui = """
<div id="container" style="background-color: white; padding: 15px; border-radius: 15px; display: flex; flex-direction: column; gap: 10px;">
    <div style="display: flex; gap: 5px;">
        <button onclick="addValue('Big')" style="flex: 2; background-color: #3498db; color: white; border: none; height: 40px; border-radius: 5px; font-weight: bold;">+Big</button>
        <button onclick="addValue('5')" style="flex: 1; background-color: #ff4d4d; color: white; border: none; border-radius: 5px; font-weight: bold;">5</button>
        <button onclick="addValue('6')" style="flex: 1; background-color: #d63031; color: white; border: none; border-radius: 5px; font-weight: bold;">6</button>
        <button onclick="addValue('7')" style="flex: 1; background-color: #8e44ad; color: white; border: none; border-radius: 5px; font-weight: bold;">7</button>
        <button onclick="addValue('8')" style="flex: 1; background-color: #2c3e50; color: white; border: none; border-radius: 5px; font-weight: bold;">8</button>
        <button onclick="addValue('9')" style="flex: 1; background-color: #34495e; color: white; border: none; border-radius: 5px; font-weight: bold;">9</button>
    </div>
    <div style="display: flex; gap: 5px;">
        <button onclick="addValue('Small')" style="flex: 2; background-color: #e67e22; color: white; border: none; height: 40px; border-radius: 5px; font-weight: bold;">+Small</button>
        <button onclick="addValue('0')" style="flex: 1; background-color: #2ecc71; color: white; border: none; border-radius: 5px; font-weight: bold;">0</button>
        <button onclick="addValue('1')" style="flex: 1; background-color: #27ae60; color: white; border: none; border-radius: 5px; font-weight: bold;">1</button>
        <button onclick="addValue('2')" style="flex: 1; background-color: #16a085; color: white; border: none; border-radius: 5px; font-weight: bold;">2</button>
        <button onclick="addValue('3')" style="flex: 1; background-color: #f1c40f; color: black; border: none; border-radius: 5px; font-weight: bold;">3</button>
        <button onclick="addValue('4')" style="flex: 1; background-color: #f39c12; color: white; border: none; border-radius: 5px; font-weight: bold;">4</button>
    </div>
</div>

<script>
    let pattern = [];
    function addValue(val) {
        if (pattern.length < 10) {
            pattern.push(val);
            // Streamlit এর মেইন ইনপুট বক্সে ডাটা পাঠানো
            const inputField = window.parent.document.querySelectorAll('input[type="text"]')[0];
            const labelField = window.parent.document.querySelectorAll('label')[0];
            
            inputField.value = pattern.join(',');
            inputField.dispatchEvent(new Event('input', { bubbles: true }));
        }
    }
</script>
"""

# HTML কম্পোনেন্ট রেন্ডার করা
st.components.v1.html(custom_ui, height=140)

# আউটপুট এরিয়া
st.write("")
pattern_val = st.text_input("প্যাটার্ন (উপরে বাটনে ক্লিক করুন):", key="pattern_box")
period_val = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# সিগন্যাল বাটন
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if pattern_val:
        st.success(f"আপনার ইনপুট: {pattern_val}. বিশ্লেষণ করা হচ্ছে...")
    else:
        st.error("দয়া করে আগে সংখ্যা ইনপুট দিন!")
        
