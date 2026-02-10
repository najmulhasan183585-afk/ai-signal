import streamlit as st
import sqlite3
import streamlit.components.v1 as components

# ১. ডাটাবেজ সেটআপ
conn = sqlite3.connect('ai_database.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS history (pattern TEXT, period TEXT)')
conn.commit()

st.set_page_config(page_title="AI Signal VIP", layout="centered")

st.markdown("<h3 style='text-align: center;'>📊 আগের ১০টি রেজাল্ট ইনপুট দিন:</h3>", unsafe_allow_html=True)

# ২. কাস্টম UI (HTML + JavaScript)
# এখানে 'setInterval' ব্যবহার করা হয়েছে যাতে পেজ রিফ্রেশ হলেও এটি সবসময় ইনপুট বক্সের সাথে কানেক্ট থাকে
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
    
    // মেইন উইন্ডোর ইনপুট বক্স খুঁজে ডাটা পাঠানোর ফাংশন
    function send(val) {
        if (currentPattern.length < 10) {
            currentPattern.push(val);
            updateInput();
        }
    }

    function updateInput() {
        const inputs = window.parent.document.querySelectorAll('input[type="text"]');
        if (inputs.length > 0) {
            inputs[0].value = currentPattern.join(',');
            inputs[0].dispatchEvent(new Event('input', { bubbles: true }));
        }
    }

    // প্রতি ক্লিকে ডাটা রিসেট হওয়া রোধ করতে (যদি প্রয়োজন হয়)
    window.parent.document.addEventListener('keydown', function(e) {
        if (e.key === "Enter") { currentPattern = []; }
    });
</script>
"""

# UI রেন্ডার করা
components.html(custom_ui, height=125)

# ৩. মেইন ইন্টারফেস
st.write("")
# এখানে value হিসেবে কিছুই দিব না যাতে রিফ্রেশ হওয়ার পর বক্স খালি হয়ে নতুন করে ইনপুট নিতে পারে
pattern_data = st.text_input("প্যাটার্ন (বক্স আপডেট হবে):", key="main_input")
period_data = st.text_input("পিরিয়ড নম্বর দিন (শেষ ৩টি):", placeholder="যেমন: 655")

# ৪. ডাটা সেভ লজিক
if st.button("🚀 GET SIGNAL & SAVE TO DB"):
    if pattern_data and period_data:
        # ডাটাবেজে সেভ করা
        c.execute("INSERT INTO history (pattern, period) VALUES (?, ?)", (pattern_data, period_data))
        conn.commit()
        
        st.success(f"সেভ হয়েছে! পিরিয়ড: {period_data}")
        st.info("নতুন ইনপুটের জন্য বাটনগুলো আবার কাজ করবে।")
        
        # প্রেডিকশন লজিক এখানে দিতে পারেন
        # st.write("Next Result: BIG") 
    else:
        st.error("দয়া করে প্যাটার্ন এবং পিরিয়ড ইনপুট দিন!")

# ৫. হিস্টোরি টেবিল
if st.checkbox("আগের জমানো ডাটা দেখুন"):
    rows = c.execute("SELECT * FROM history ORDER BY rowid DESC LIMIT 5").fetchall()
    st.table(rows)

# সব মুছার বাটন
if st.button("🗑️ সব মুছুন (Refresh App)"):
    st.rerun()
    
