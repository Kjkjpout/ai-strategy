import streamlit as st

# 1. 必須先 import 並且設定頁面，否則會報 NameError
st.set_page_config(page_title="HookFlow PRO", layout="centered")

# 2. 高級美工 CSS (包含 HookFlow 品牌配色)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(160deg, #020617 0%, #0f172a 100%);
        color: #f8fafc;
    }
    
    /* 標題漸層效果 */
    .main-title {
        font-size: 50px;
        font-weight: 800;
        background: -webkit-linear-gradient(#fff, #64748b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }

    /* 統一按鈕樣式 */
    div[data-testid="stHorizontalBlock"] button {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #94a3b8 !important;
        width: 100% !important;
        border-radius: 10px !important;
    }

    /* 開始分析按鈕：強勢橘紅漸層 */
    .stButton > button:first-child {
        background: linear-gradient(90deg, #f97316 0%, #ef4444 100%) !important;
        height: 55px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(239, 68, 68, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 介面內容
st.markdown('<h1 class="main-title">🌊 HookFlow <span style="font-size:20px; color:#ef4444;">PRO</span></h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-top:-10px;'>全平台爆款內容拆解引擎</p>", unsafe_allow_html=True)

st.write("---")

# 平台選擇按鈕
cols = st.columns(5)
platforms = ["TikTok", "抖音", "YouTube", "Instagram", "小紅書"]
for i, p in enumerate(platforms):
    with cols[i]:
        st.button(p)

st.write("") 

# 輸入連結
url = st.text_input("🔗 貼上您想分析的影片連結", placeholder="例如：https://v.douyin.com/...")

# 分析執行
if st.button("🚀 啟動 AI 深度分析"):
    if url:
        st.toast("專家小組已就緒！")
        st.success(f"正在拆解 {url} 的爆火基因...")
        # 這裡之後會放分析結果
    else:
        st.error("請先提供影片連結喔！")
