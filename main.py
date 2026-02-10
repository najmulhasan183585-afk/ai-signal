import streamlit as st
import sqlite3
import streamlit.components.v1 as components

# ১. ডাটাবেজ সেটআপ
conn = sqlite3.connect('ai_database.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS history (pattern TEXT, period TEXT)')
conn.commit()

st.set_page_config(page_title="AI Signal Pro", layout="centered")

st.markdown("<h3 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h3>", unsafe_allow_html=True)

# ২. কাস্টম রিফ্রেশ-মুক্ত UI (HTML + JavaScript)
# এটি মোবাইলে বাটন পাশাপাশি রাখবে এবং ক্লিক করলে রিফ্রেশ হবে না
custom_ui = """
<div id="wrapper" style="background: white; padding: 10px; border-radius: 12px; display: flex; flex-direction: column; gap: 8px;">
    <div style="display: flex; gap: 4px;">
        <button onclick="send('Big')" style="flex: 2; background: #3498db; color: white; border: none; height: 40px; border-radius: 5px; font-weight: bold;">+Big</button>
        <button onclick="send('5')" style="flex: 1; background: #ff4d4d; color: white; border: none; border-radius: 5px;">5</button>
        <button onclick="send('6')" style="flex: 1; background: #d63031; color: white; border: none; border-radius: 5px;">6</button>
        <button onclick="send('7')" style="flex: 1; background: #8e44ad; color: white; border: none; border-radius: 5px;">7</button>
        <button onclick="send('8')" style="flex: 1; background: #2c3e50; color: white; border: none; border-radius: 5px;">8</button>
        <button onclick="send('9')" style="flex: 1; background: #34495e; color: white; border: none; border-radius: 5px;">9</button>
    </div>
    <div style="display: flex; gap: 4px;">
        <button onclick="send('Small')" style="flex: 2; background: #e67e22; color: white; border: none; height: 40px; border-radius: 5px; font-weight: bold;">+Small</button>
        <button onclick="send('0')" style="flex: 1; background: #2ecc71; color: white; border: none; border-radius: 5px;">0</button>
        <button onclick="send('1')" style="flex: 1; background: #27ae60; color: white; border: none; border-radius: 5px;">1</button>
        <button onclick="send('2')" style="flex: 1; background: #16a085; color: white; border: none; border-radius: 5px;">2</button>
        <button onclick="send('3')" style="flex: 1; background: #f1c40f; color: black; border: none; border-radius: 5px;">3</button>
        <button onclick="send('4')" style="flex: 1; background: #f39c12; color: white; border: none; border-radius: 5px;">4</button>
    </div>
</div>

<script>
    let currentPattern = [];
    function send(val) {
        if (currentPattern.length < 10) {
            currentPattern.push(val);
            // মেইন পাইথন ইনপুট বক্স খুঁজে সেখানে ডাটা পাঠানো
            const inputs = window.parent.document.querySelectorAll('input[type="text"]');
            if (inputs.length > 0) {
                inputs[0].value = currentPattern.join(',');
                inputs[0].dispatchEvent(new Event('input', { bubbles: true }));
            }
        }
    }
</script>
"""

# UI রেন্ডার করা
components.html(custom_ui, height=120)

# ৩. পাইথন ইনপুট বক্স (যেখানে ডাটা জমা হবে)
st.write("")
pattern_data = st.text_input("প্যাটার্ন (বক্স আপডেট হবে):", key="main_pattern")
period_data = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# ৪. ডাটাবেজে সেভ করার লজিক
if st.button("🚀 GET SIGNAL & SAVE TO DB"):
    if pattern_data and period_data:
        c.execute("INSERT INTO history (pattern, period) VALUES (?, ?)", (pattern_data, period_data))
        conn.commit()
        st.success(f"সফলভাবে ডাটাবেজে সেভ হয়েছে: {pattern_data}")
    else:
        st.error("দয়া করে প্যাটার্ন এবং পিরিয়ড উভয়ই ইনপুট দিন!")

# ৫. আগের ডাটা দেখার অপশন
if st.checkbox("আগের জমানো ডাটা দেখুন"):
    rows = c.execute("SELECT * FROM history ORDER BY rowid DESC LIMIT 5").fetchall()
    st.table(rows)

# ক্লিয়ার বাটন
if st.button("🗑️ সব মুছুন (Refresh App)"):
    st.rerun()
    
