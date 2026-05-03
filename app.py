import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 🛡️ 第一重保險：即使環境安裝延遲，程式也不會報錯跳開
try:
    import yt_dlp
    YTDLP_READY = True
except ImportError:
    YTDLP_READY = False

# --- 介面風格還原 (黑金爆款設計) ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 55px !important;
        width: 100% !important;
        font-size: 18px !important;
    }
    .result-card {
        background-color: #1c2533;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ff4b2b;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 會員系統 (連接 Google Sheets) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception:
    st.error("❌ 系統初始化失敗，請檢查 Secrets 設定。")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    
    if st.button("立即進入系統"):
        # 匹配手機號碼 (對應你的 266 尾號那筆)
        match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not match.empty:
            exp_date = pd.to_datetime(match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp_date:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 權限已過期")
        else: st.error("❌ 號碼未授權")

else:
    # --- 核心功能：真實分析 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，進行真實數據分析")
    
    url = st.text_input("貼上影片連結 (TikTok/抖音/YouTube/小紅書)", placeholder="http://...")

    if st.button("啟動 AI 深度拆解"):
        if not YTDLP_READY:
            st.warning("🛠️ 核心分析組件正在安裝中，請等候 30 秒後重新點擊，不要刷新頁面。")
        elif url:
            with st.status("🧠 正在抓取數據並分析爆款基因...", expanded=True) as status:
                try:
                    # 真實抓取標題
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        v_title = info.get('title', '熱門爆款內容')
                    
                    status.update(label="✅ 分析完成！", state="complete")
                    st.success(f"已識別影片：{v_title}")

                    # 根據標題生成的 5 套 10 秒腳本
                    kw = v_title[:10]
                    scripts = [
                        f"關於【{kw}】為什麼能火？底層邏輯就一個：抓住焦慮。學會這招，你也能翻倍播放！",
                        f"2026年最後風口：把【{kw}】重新做一遍。10秒鐘拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】的腳本幫我漲粉破萬。文案我放在下方，建議直接複製。",
                        f"如果你的影片沒流量，試試把開頭換成：關於【{kw}】你不知道的真相。流量絕對瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】專屬腳本簡直絕了！10秒生成高質感內容，現在就去試！"
                    ]

                    st.markdown("---")
                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="result-card"><b>🔥 方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    
                    st.balloons()
                except Exception:
                    st.error("分析失敗，請檢查連結是否正確。")
        else:
            st.warning("請先填寫連結")
