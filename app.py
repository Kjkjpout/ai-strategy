import streamlit as st

# 1. 介面基礎設定
st.set_page_config(page_title="ViralAI Pro", layout="centered")

# 2. 高級美工 CSS (這一段是讓介面變高級的關鍵)
st.markdown("""
    <style>
    /* 設定深藍色背景 */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: white;
    }
    
    /* 輸入框毛玻璃質感 */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
    }

    /* 開始分析按鈕：紅色漸層發光 */
    .stButton > button {
        background: linear-gradient(90deg, #FF4B2B 0%, #FF416C 100%) !important;
        color: white !important;
        border: none !important;
        padding: 15px 0px !important;
        border-radius: 12px !important;
        width: 100% !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 畫面顯示內容
st.title("🔥 ViralAI")
st.write("全平台爆款引擎 - AI 驅動深度分析")

# 平台按鈕區
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.button("TikTok")
with col2: st.button("抖音")
with col3: st.button("YouTube")
with col4: st.button("IG")
with col5: st.button("小紅書")

# 輸入框
url = st.text_input("請輸入影片連結：", placeholder="http://...")

# 分析按鈕
if st.button("🚀 開始 AI 深度分析"):
    if url:
        st.success(f"已接收連結！正在啟動【爆款專家團】進行拆解...")
        # 這裡之後會放入分析結果
    else:
        st.warning("請先輸入連結喔！")
