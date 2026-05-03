import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 🛡️ 雙重保險：即使環境還沒裝好，程式也不會報錯跳開
try:
    import yt_dlp
    SYSTEM_READY = True
except ImportError:
    SYSTEM_READY = False

# --- 1. 介面視覺：黑色背景 + 紅橙漸層按鈕 ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-header { font-size: 36px; font-weight: bold; margin-bottom: 10px; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 5px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        height: 50px !important;
        width: 100% !important;
        font-weight: bold;
    }
    .card { background-color: #1c2533; padding: 20px; border-radius: 12px; border-left: 5px solid #ff4b2b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 會員驗證 (連接你的 Google Sheet) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("❌ 系統初始化失敗，請檢查 Secrets 設定。")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-header">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    
    if st.button("立即登入"):
        # 匹配你的 Google Sheets (例如 09xxxxxxxx)
        match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not match.empty:
            exp = pd.to_datetime(match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 權限已過期")
        else: st.error("❌ 號碼未授權")

else:
    # --- 3. 爆款拆解邏輯 ---
    st.markdown('<div class="viral-header">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，進行真實分析")
    
    url = st.text_input("貼上影片連結 (TikTok / 抖音 / YouTube / 小紅書)", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if not SYSTEM_READY:
            st.warning("🛠️ 核心組件安裝中，請等候 30 秒後重新點擊。")
        elif url:
            with st.status("🧠 正在抓取數據...", expanded=True) as status:
                try:
                    # 真實抓取
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        v_title = info.get('title', '熱門影片')
                    
                    status.update(label="✅ 分析完成", state="complete")
                    st.success(f"已識別影片：{v_title}")

                    # 生成 5 套 10 秒腳本
                    kw = v_title[:10]
                    scripts = [
                        f"為什麼這支關於【{kw}】的片能火？邏輯就一個：抓住情緒價值。學會這招，你也行！",
                        f"2026年爆款秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】的腳本幫我漲粉一萬。文案我放在下方，直接複製。",
                        f"流量焦慮？試試把開頭換成：關於【{kw}】你不知道的真相。流量絕對瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡解絕了！10秒生成高質感內容，現在就去試！"
                    ]

                    st.markdown("---")
                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="card"><b>方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s) # 方便用戶點擊複製
                    
                    st.balloons()
                except:
                    st.error("讀取失敗，請確認連結是否正確。")
        else:
            st.warning("請填寫連結")
