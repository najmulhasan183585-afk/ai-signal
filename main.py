st.markdown("""
<style>
    /* বাটনগুলোকে এক সারিতে (Row) সুন্দরভাবে সেট করা */
    div[data-testid="column"] {
        display: flex; align-items: center; justify-content: center;
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
    /* Big Row এর কালার */
    div[data-testid="column"]:nth-of-type(1) button { background: #3498db !important; } /* +Big */
    div[data-testid="column"]:nth-of-type(2) button { background: #FF5733 !important; } /* 5 */
    div[data-testid="column"]:nth-of-type(3) button { background: #C70039 !important; } /* 6 */
    div[data-testid="column"]:nth-of-type(4) button { background: #900C3F !important; } /* 7 */
    div[data-testid="column"]:nth-of-type(5) button { background: #581845 !important; } /* 8 */
    div[data-testid="column"]:nth-of-type(6) button { background: #2C3E50 !important; } /* 9 */

    /* Small Row এর কালার (ইন্ডেক্স অনুযায়ী) */
    div[data-testid="column"]:nth-of-type(7) button { background: #e67e22 !important; } /* +Small */
    div[data-testid="column"]:nth-of-type(8) button { background: #2ECC71 !important; } /* 0 */
    div[data-testid="column"]:nth-of-type(9) button { background: #27AE60 !important; } /* 1 */
    div[data-testid="column"]:nth-of-type(10) button { background: #16A085 !important; } /* 2 */
    div[data-testid="column"]:nth-of-type(11) button { background: #F1C40F !important; } /* 3 */
    div[data-testid="column"]:nth-of-type(12) button { background: #F39C12 !important; } /* 4 */
</style>
""", unsafe_allow_html=True)
