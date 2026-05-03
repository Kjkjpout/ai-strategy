import streamlit as st  # 補上這行解決第一張圖的 NameError
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import yt_dlp
import time

# --- 介面風格：1:1 還原你的黑金爆款設計 ---
st.set_page_config(page_title="強棒 ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 55px !important;
        width: 100%;
        font-weight: bold;
        font-size: 18px;
    }
    .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #1f2937 !important;
        border-radius: 10px !important;
    }
    .result-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b2b;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 會員系統 (連接你的 Google Sheet) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("請確認 Streamlit Secrets 已設定 Google Sheet 連結")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown("# 🔥 強棒 ViralAI Pro\n### 全平台爆款引擎")
    u_phone = st.text_input("輸入手機號碼驗證")
    if st.button("立即登入"):
        # 比對你的 Google Sheet 手機號碼
        res = df[df['phone'].astype(str) == u_phone.strip()]
        if not res.empty:
            exp = pd.to_datetime(res.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login = True
                st.rerun()
            else: st.error("帳號權限已過期")
        else: st.error("手機號碼未授權")
else:
    # --- 核心功能：真實抓取與 10秒文案分析 ---
    st.markdown("## 🔥 輸入連結，AI 真實數據分析")
    st.markdown("支援 TikTok、抖音、YouTube、小紅書")
    
    url = st.text_input("在此貼上影片連結", placeholder="https://...")

    if st.button("🔍 啟動 AI 深度拆解"):
        if url:
            with st.status("📡 正在連線抓取影片數據...", expanded=True) as status:
                try:
                    # 真實抓取 Meta Data
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        v_title = info.get('title', '爆款影片')
                    
                    status.update(label="✅ 數據抓取成功！正在生成 5 組腳本...", state="complete")
                    
                    st.markdown(f"### 📊 分析目標：`{v_title}`")
                    st.markdown("---")

                    # 基於真實標題生成的 5 組 10秒文案
                    # 關鍵字取前 8 個字，確保文案精準
                    kw = v_title[:8]
                    
                    templates = [
                        f"為什麼這支關於【{kw}】的片能火？底層邏輯就一個：製造反差。學會這招，你也能翻倍播放！",
                        f"你還在傻刷【{kw}】？高手已經在用這個點賺錢了。10秒鐘拆解它的爆火密碼，建議收藏。",
                        f"實測有效！把【{kw}】重新做一遍，我的帳號漲粉破萬。文案我放在下方，直接拿走。",
                        f"如果影片沒人看，試試把開頭換成：關於【{kw}】你不知道的真相。流量絕對瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】專屬腳本簡直絕了！10秒生成高質感內容，現在就去試！"
                    ]

                    st.markdown("### 🎯 豆包專用：5 組爆款標題與文案")
                    
                    for i, content in enumerate(templates, 1):
                        with st.container():
                            st.markdown(f'<div class="result-card">', unsafe_allow_html=True)
                            st.write(f"**方案 {i} 標題：** 【{kw}】的流量密碼")
                            st.write(f"**10秒口播文案：**")
                            st.code(content) # 點擊即可複製
                            st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.balloons()

                except Exception as e:
                    st.error(f"抓取失敗！原因：{str(e)}")
                    st.info("提示：請確保連結是公開影片，且 requirements.txt 已正確上傳。")
        else:
            st.warning("請先貼上連結")
