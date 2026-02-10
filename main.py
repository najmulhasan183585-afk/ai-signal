import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="AI Signal Mobile", layout="centered")

st.markdown("<h3 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h3>", unsafe_allow_html=True)

# JavaScript এবং HTML দিয়ে তৈরি কাস্টম ইন্টারফেস
# এটি রিফ্রেশ ছাড়াই সরাসরি প্যাটার্ন বক্স আপডেট করবে
custom_component = """
<div id="ui-root" style="background-color: white; padding: 12px; border-radius: 12px; display: flex; flex-direction: column; gap: 8px; font-family: sans-serif;">
    <div style="display: flex; gap: 4px;">
        <button onclick="press('Big')" style="flex: 2; background: #3498db; color: white; border: none; height: 42px; border-radius: 6px; font-weight: bold;">+Big</button>
        <button onclick="press('5')" style="flex: 1; background: #ff4d4d; color: white; border: none; border-radius: 6px; font-weight: bold;">5</button>
        <button onclick="press('6')" style="flex: 1; background: #d63031; color: white; border: none; border-radius: 6px; font-weight: bold;">6</button>
        <button onclick="press('7')" style="flex: 1; background: #8e44ad; color: white; border: none; border-radius: 6px; font-weight: bold;">7</button>
        <button onclick="press('8')" style="flex: 1; background: #2c3e50; color: white; border: none; border-radius: 6px; font-weight: bold;">8</button>
        <button onclick="press('9')" style="flex: 1; background: #34495e; color: white; border: none; border-radius: 6px; font-weight: bold;">9</button>
    </div>
    <div style="display: flex; gap: 4px;">
        <button onclick="press('Small')" style="flex: 2; background: #e67e22; color: white; border: none; height: 42px; border-radius: 6px; font-weight: bold;">+Small</button>
        <button onclick="press('0')" style="flex: 1; background: #2ecc71; color: white; border: none; border-radius: 6px; font-weight: bold;">0</button>
        <button onclick="press('1')" style="flex: 1; background: #27ae60; color: white; border: none; border-radius: 6px; font-weight: bold;">1</button>
        <button onclick="press('2')" style="flex: 1; background: #16a085; color: white; border: none; border-radius: 6px; font-weight: bold;">2</button>
        <button onclick="press('3')" style="flex: 1; background: #f1c40f; color: black; border: none; border-radius: 6px; font-weight: bold;">3</button>
        <button onclick="press('4')" style="flex: 1; background: #f39c12; color: white; border: none; border-radius: 6px; font-weight: bold;">4</button>
    </div>
</div>

<script>
    let pattern = [];
    function press(val) {
        if (pattern.length < 10) {
            pattern.push(val);
            // মেইন উইন্ডোর টেক্সট ইনপুট খুঁজে আপডেট করা
            const inputs = window.parent.document.querySelectorAll('input[type="text"]');
            if (inputs.length > 0) {
                inputs[0].value = pattern.join(',');
                inputs[0].dispatchEvent(new Event('input', { bubbles: true }));
            }
        }
    }
</script>
"""

# কাস্টম UI রেন্ডার করা (হাইট সেট করা হয়েছে যাতে মোবাইলে ঠিক দেখায়)
components.html(custom_component, height=130)

# প্যাটার্ন ডিসপ্লে বক্স
st.write("")
pattern_input = st.text_input("প্যাটার্ন (উপরে বাটনে ক্লিক করুন):", placeholder="যেমন: 5,6,Small", key="p_box")

# পিরিয়ড ইনপুট
period = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# সিগন্যাল বাটন
if st.button("🚀 GET SIGNAL (AI বিশ্লেষণ করুন)"):
    if pattern_input:
        st.success(f"বিশ্লেষণ করা হচ্ছে: {pattern_input}")
    else:
        st.error("দয়া করে আগে সংখ্যা ইনপুট দিন!")

# ক্লিয়ার বাটন (যদি ভুল হয়)
if st.button("🗑️ সব মুছুন (Clear All)"):
    st.rerun()
    
