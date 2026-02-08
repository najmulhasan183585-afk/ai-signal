import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="AI Pattern Input", layout="centered")

# মূল ডিজাইন (HTML, CSS & JS)
html_code = """
<div style="font-family: 'Segoe UI', sans-serif; background: #ffffff; padding: 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 450px; margin: auto;">
    <h3 style="text-align: center; color: #333; margin-bottom: 20px;">AI Analysis Dashboard</h3>
    
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
        <div style="background: #3498db; color: white; padding: 12px; border-radius: 10px; font-weight: bold; min-width: 70px; text-align: center; box-shadow: 0 4px 6px rgba(52, 152, 219, 0.3);">+Big</div>
        <div style="display: flex; gap: 6px;">
            <button onclick="sendData('B-5')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #FF5733; color: white; font-weight: bold;">5</button>
            <button onclick="sendData('B-6')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #C70039; color: white; font-weight: bold;">6</button>
            <button onclick="sendData('B-7')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #900C3F; color: white; font-weight: bold;">7</button>
            <button onclick="sendData('B-8')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #581845; color: white; font-weight: bold;">8</button>
            <button onclick="sendData('B-9')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #2C3E50; color: white; font-weight: bold;">9</button>
        </div>
    </div>

    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <div style="background: #e67e22; color: white; padding: 12px; border-radius: 10px; font-weight: bold; min-width: 70px; text-align: center; box-shadow: 0 4px 6px rgba(230, 126, 34, 0.3);">+Small</div>
        <div style="display: flex; gap: 6px;">
            <button onclick="sendData('S-0')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #2ECC71; color: white; font-weight: bold;">0</button>
            <button onclick="sendData('S-1')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #27AE60; color: white; font-weight: bold;">1</button>
            <button onclick="sendData('S-2')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #16A085; color: white; font-weight: bold;">2</button>
            <button onclick="sendData('S-3')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #F1C40F; color: white; font-weight: bold;">3</button>
            <button onclick="sendData('S-4')" style="padding: 10px 14px; border: none; border-radius: 8px; cursor: pointer; background: #F39C12; color: white; font-weight: bold;">4</button>
        </div>
    </div>

    <div id="output" style="padding: 20px; background: #1e1e1e; color: #00ff00; border-radius: 12px; min-height: 50px; font-family: 'Courier New', monospace; font-size: 18px; word-break: break-all; box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);">
    </div>
</div>

<script>
    function sendData(val) {
        const out = document.getElementById('output');
        // প্রথম এন্ট্রির আগে কমা বসবে না
        if(out.innerText.trim() === "") {
            out.innerText = val;
        } else {
            out.innerText += ", " + val;
        }
    }
</script>
"""

# Streamlit এ রেন্ডার করা
components.html(html_code, height=450)
