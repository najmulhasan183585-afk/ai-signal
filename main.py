import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="AI Pattern Input", layout="centered")

# মূল ডিজাইন (HTML & CSS)
html_code = """
<div style="font-family: sans-serif; background: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); max-width: 450px; margin: auto;">
    <h3 style="text-align: center; color: #333;">Pattern Input Row</h3>
    
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
        <div style="background: #5dade2; color: white; padding: 10px; border-radius: 8px; font-weight: bold; min-width: 70px; text-align: center;">+Big</div>
        <div style="display: flex; gap: 5px;">
            <button onclick="sendData('B-5')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">5</button>
            <button onclick="sendData('B-6')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">6</button>
            <button onclick="sendData('B-7')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">7</button>
            <button onclick="sendData('B-8')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">8</button>
            <button onclick="sendData('B-9')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">9</button>
        </div>
    </div>

    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
        <div style="background: #eb984e; color: white; padding: 10px; border-radius: 8px; font-weight: bold; min-width: 70px; text-align: center;">+Small</div>
        <div style="display: flex; gap: 5px;">
            <button onclick="sendData('S-0')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">0</button>
            <button onclick="sendData('S-1')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">1</button>
            <button onclick="sendData('S-2')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">2</button>
            <button onclick="sendData('S-3')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">3</button>
            <button onclick="sendData('S-4')" style="padding: 10px 14px; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; background: #f9f9f9; font-weight: bold;">4</button>
        </div>
    </div>

    <div id="output" style="margin-top: 20px; padding: 15px; background: #1e1e1e; color: #00ff00; border-radius: 8px; min-height: 40px; font-family: monospace; word-break: break-all;">
        Input: 
    </div>
    <button onclick="document.getElementById('output').innerText = 'Input: '" style="width: 100%; margin-top: 10px; padding: 8px; border: none; border-radius: 5px; background: #ddd; cursor: pointer;">Reset Display</button>
</div>

<script>
    function sendData(val) {
        const out = document.getElementById('output');
        if(out.innerText === "Input: ") {
            out.innerText += val;
        } else {
            out.innerText += ", " + val;
        }
    }
</script>
"""

# Streamlit এ কোড রেন্ডার করা
st.markdown("### AI Analysis Dashboard")
components.html(html_code, height=500)
