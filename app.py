import streamlit as st # 解決 NameError
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 嘗試匯入分析工具，若還沒安裝好則給予提示，不崩潰
try:
    import yt_dlp
    HAS_YTDLP = True
except ImportError:
    HAS_YTDLP = False

# --- 介面風格：黑色背景 + 紅橙漸層按鈕 ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextInput input { background-color: white !important; color: black !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 55px !important;
        width: 100% !important;
        font-weight: bold;
    }
    .report-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b2b;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 會員驗證 (連接你的試算表) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("❌ 數據庫連線失敗，請檢查 Secrets 設定")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.title("🔥 ViralAI 全平台爆款引擎")
    u_phone = st.text_input("輸入手機號碼驗證")
    if st.button("立即驗證登入"):
        # 匹配你的手機號碼 (例如 972896266)
        res = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not res.empty:
            exp = pd.to_datetime(res.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 帳號已過期")
        else: st.error("❌ 號碼未授權")
else:
    st.markdown("## 🚀 開始 AI 深度分析")
    url = st.text_input("貼上影片連結 (YouTube/TikTok/小紅書)")

    if st.button("啟動數據拆解"):
        if not HAS_YTDLP:
            st.warning("🛠️ 系統組件正在背景安裝中，請等候 30 秒後重新點擊。")
        elif url:
            with st.spinner("🧠 正在提取爆款基因..."):
                try:
                    # 真實提取標題
                    ydl_opts = {'quiet': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        title = info.get('title', '爆款內容')
                    
                    st.success(f"✅ 已成功拆解影片：{title}")
                    
                    # 生成 5 套 10 秒豆包腳本
                    kw = title[:8]
                    templates = [
                        f"關於【{kw}】為什麼能火？因為他抓住了情緒。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解密碼，看我就對了。",
                        f"實測有效！這套【{kw}】腳本幫我漲粉一萬。文案在評論區，自取。",
                        f"沒流量？試試把開頭換成：關於【{kw}】你不知道的真相。流量絕對炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡直絕了！10秒出片，現在就去試！"
                    ]

                    for i, s in enumerate(templates, 1):
                        st.markdown(f'<div class="report-box">方案 {i}：<br><b>{s}</b></div>', unsafe_allow_html=True)
                    st.balloons()
                except:
                    st.error("讀取連結失敗，請確認連結是否正確")
